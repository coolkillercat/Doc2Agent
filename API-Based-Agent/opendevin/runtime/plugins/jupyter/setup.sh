#!/bin/bash

set -e

# Enable debugging
set -x

source ~/.bashrc
# ADD /opendevin/plugins to PATH to make `jupyter_cli` available
echo 'export PATH=$PATH:/opendevin/plugins/jupyter' >> ~/.bashrc
export PATH=/opendevin/plugins/jupyter:$PATH

# get current PythonInterpreter
OPENDEVIN_PYTHON_INTERPRETER=$(which python3)
echo "Using Python interpreter: $OPENDEVIN_PYTHON_INTERPRETER"

# Set up PATH based on user
if [ "$USER" = "opendevin" ]; then
    echo 'export PATH=$PATH:/home/opendevin/.local/bin' >> ~/.bashrc
    echo "export OPENDEVIN_PYTHON_INTERPRETER=$OPENDEVIN_PYTHON_INTERPRETER" >> ~/.bashrc
    export PATH=$PATH:/home/opendevin/.local/bin
    export PIP_CACHE_DIR=$HOME/.cache/pip
elif [ "$USER" = "root" ]; then
    echo 'export PATH=$PATH:/root/.local/bin' >> ~/.bashrc
    echo "export OPENDEVIN_PYTHON_INTERPRETER=$OPENDEVIN_PYTHON_INTERPRETER" >> ~/.bashrc
    export PATH=$PATH:/root/.local/bin
    export PIP_CACHE_DIR=$HOME/.cache/pip
fi

# Install dependencies with error checking
echo "Installing Jupyter dependencies..."
if ! pip install jupyterlab notebook jupyter_kernel_gateway; then
    echo "Failed to install Jupyter dependencies"
    exit 1
fi

# Create logs directory
sudo mkdir -p /opendevin/logs && sudo chmod 777 /opendevin/logs

# CRITICAL: Make execute_server executable before trying to run it
echo "Making execute_server executable..."
chmod +x /opendevin/plugins/jupyter/execute_server || {
    echo "Failed to make execute_server executable"
    exit 1
}

# Improved find_free_port function
find_free_port() {
    local start_port="${1:-20000}"
    local end_port="${2:-65535}"

    for port in $(seq $start_port $end_port); do
        # Use ss instead of netstat (more commonly available)
        if ! nc -z localhost $port 2>/dev/null && ! ss -tln | grep -q ":$port "; then
            echo $port
            return
        fi
    done

    echo "No free ports found in the range $start_port to $end_port" >&2
    return 1
}

# Find port for Jupyter Gateway
export JUPYTER_GATEWAY_PORT=$(find_free_port 20000 30000)
echo "Using Jupyter Gateway port: $JUPYTER_GATEWAY_PORT"

# Start Jupyter kernel gateway
echo "Starting Jupyter kernel gateway..."
jupyter kernelgateway --KernelGatewayApp.ip=0.0.0.0 --KernelGatewayApp.port=$JUPYTER_GATEWAY_PORT > /opendevin/logs/jupyter_kernel_gateway.log 2>&1 &
export JUPYTER_GATEWAY_PID=$!
echo "export JUPYTER_GATEWAY_PID=$JUPYTER_GATEWAY_PID" >> ~/.bashrc

# Check if kernel gateway started successfully
sleep 2
if ! ps -p $JUPYTER_GATEWAY_PID > /dev/null; then
    echo "Failed to start Jupyter kernel gateway"
    echo "Kernel gateway logs:"
    cat /opendevin/logs/jupyter_kernel_gateway.log
    exit 1
fi

export JUPYTER_GATEWAY_KERNEL_ID="default"
echo "export JUPYTER_GATEWAY_KERNEL_ID=$JUPYTER_GATEWAY_KERNEL_ID" >> ~/.bashrc
echo "JupyterKernelGateway started with PID: $JUPYTER_GATEWAY_PID"

# Find port for execution server
export JUPYTER_EXEC_SERVER_PORT=$(find_free_port 30000 40000)
echo "Using Jupyter Exec Server port: $JUPYTER_EXEC_SERVER_PORT"
echo "export JUPYTER_EXEC_SERVER_PORT=$JUPYTER_EXEC_SERVER_PORT" >> ~/.bashrc

# Start the jupyter_server
echo "Starting Jupyter execution server..."
/opendevin/plugins/jupyter/execute_server > /opendevin/logs/jupyter_execute_server.log 2>&1 &
export JUPYTER_EXEC_SERVER_PID=$!
echo "export JUPYTER_EXEC_SERVER_PID=$JUPYTER_EXEC_SERVER_PID" >> ~/.bashrc

# Check if execution server started successfully
sleep 2
if ! ps -p $JUPYTER_EXEC_SERVER_PID > /dev/null; then
    echo "Failed to start Jupyter execution server"
    echo "Execution server logs:"
    cat /opendevin/logs/jupyter_execute_server.log
    echo ""
    echo "Checking execute_server file permissions:"
    ls -la /opendevin/plugins/jupyter/execute_server
    echo ""
    echo "Trying to run execute_server directly to see error:"
    /opendevin/plugins/jupyter/execute_server --help || true
    exit 1
fi

echo "Execution server started with PID: $JUPYTER_EXEC_SERVER_PID"

# Wait for services to be ready with better pattern matching
echo "Waiting for Jupyter kernel gateway to be ready..."
TIMEOUT=30
COUNTER=0
while [ $COUNTER -lt $TIMEOUT ]; do
    if grep -E -q "(available at|running at|started at|Jupyter Kernel Gateway at)" /opendevin/logs/jupyter_kernel_gateway.log 2>/dev/null; then
        echo "Jupyter kernel gateway is ready"
        break
    fi
    echo "Waiting for Jupyter kernel gateway... ($COUNTER/$TIMEOUT)"
    sleep 1
    COUNTER=$((COUNTER + 1))
done

if [ $COUNTER -eq $TIMEOUT ]; then
    echo "Timeout waiting for Jupyter kernel gateway"
    echo "Kernel gateway logs:"
    tail -20 /opendevin/logs/jupyter_kernel_gateway.log
    exit 1
fi

# Wait for execution server to be ready
echo "Waiting for Jupyter execution server to be ready..."
COUNTER=0
while [ $COUNTER -lt $TIMEOUT ]; do
    if grep -E -q "(kernel created|kernel ready|started successfully|Kernel created)" /opendevin/logs/jupyter_execute_server.log 2>/dev/null; then
        echo "Jupyter execution server is ready"
        break
    fi
    echo "Waiting for Jupyter execution server... ($COUNTER/$TIMEOUT)"
    sleep 1
    COUNTER=$((COUNTER + 1))
done

if [ $COUNTER -eq $TIMEOUT ]; then
    echo "Timeout waiting for Jupyter execution server"
    echo "Execution server logs:"
    tail -20 /opendevin/logs/jupyter_execute_server.log
    exit 1
fi

# Verify services are running
echo "Verifying services are running..."
if ps -p $JUPYTER_GATEWAY_PID > /dev/null && ps -p $JUPYTER_EXEC_SERVER_PID > /dev/null; then
    echo "All services are running successfully"
    echo "Jupyter Gateway PID: $JUPYTER_GATEWAY_PID (port: $JUPYTER_GATEWAY_PORT)"
    echo "Execution Server PID: $JUPYTER_EXEC_SERVER_PID (port: $JUPYTER_EXEC_SERVER_PORT)"

    # Check if ports are actually listening (using ss instead of netstat)
    echo "Checking if services are listening on ports..."
    ss -tln | grep -E "(:$JUPYTER_GATEWAY_PORT|:$JUPYTER_EXEC_SERVER_PORT)" || true
else
    echo "One or more services failed to start"
    exit 1
fi

echo "Jupyter kernel ready."
