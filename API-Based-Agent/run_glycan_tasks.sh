#!/bin/bash

# Script to run glycan tasks evaluation
# Usage: ./run_glycan_tasks.sh [start_task_id] [num_tasks]

# Set default values
START_TASK_ID=${1:-19}
NUM_TASKS=${2:-1}
AGENT_CLASS="CodeActAgent"
MAX_ITERATIONS=${3:-15}

echo "=== Glycan Tasks Evaluation ==="
echo "Start Task ID: $START_TASK_ID"
echo "Number of Tasks: $NUM_TASKS"
echo "Agent Class: $AGENT_CLASS"
echo "Max Iterations: $MAX_ITERATIONS"
echo "================================"

# Navigate to project directory
cd /Users/jianhaonan/Desktop/API-Based-Agent

# Check if required files exist
if [ ! -f "glycan/glycan_tasks.jsonl" ]; then
    echo "❌ ERROR: glycan/glycan_tasks.jsonl not found"
    exit 1
fi

if [ ! -f "evaluation/webarena/run_glycan_infer.py" ]; then
    echo "❌ ERROR: evaluation/webarena/run_glycan_infer.py not found"
    exit 1
fi

# Set up environment
export PYTHONPATH="/Users/jianhaonan/Desktop/API-Based-Agent:/Users/jianhaonan/Desktop/API-Based-Agent/evaluation/webarena:/Users/jianhaonan/Desktop/API-Based-Agent/workspace"
export GLYCAN_API_MODE="true"

# Set OpenAI API key if available
if [ -z "$OPENAI_API_KEY" ]; then
    echo "⚠️  WARNING: OPENAI_API_KEY not set. GPT evaluation may fail."
    echo "   Set it with: export OPENAI_API_KEY='your-key-here'"
fi

# Create output directory
OUTPUT_DIR="evaluation_outputs/glycan_$(date +%Y%m%d_%H%M%S)"
mkdir -p "$OUTPUT_DIR"

echo "Output directory: $OUTPUT_DIR"

# Run the evaluation
echo ""
echo "Starting glycan task evaluation..."
echo "This may take several minutes depending on the number of tasks."
echo ""

python3 evaluation/webarena/run_glycan_infer.py \
    --agent-cls "$AGENT_CLASS" \
    --llm-config llm \
    --model openai/gpt-4o \
    --glycan-start-task-id "$START_TASK_ID" \
    --glycan-num-tasks "$NUM_TASKS" \
    --max-iterations "$MAX_ITERATIONS" \
    --glycan-output-dir "$OUTPUT_DIR" \
    --glycan-tasks-file "glycan/glycan_tasks.jsonl"

EXIT_CODE=$?

if [ $EXIT_CODE -eq 0 ]; then
    echo ""
    echo "🎉 Evaluation completed successfully!"
    echo "Results saved in: $OUTPUT_DIR"
    echo ""
    echo "To view results:"
    echo "  cat $OUTPUT_DIR/glycan_evaluation_results_*.json"
    echo ""
    echo "To view logs:"
    echo "  ls $OUTPUT_DIR/logs/"
else
    echo ""
    echo "❌ Evaluation failed with exit code $EXIT_CODE"
    echo "Check the logs in: $OUTPUT_DIR/logs/"
fi

exit $EXIT_CODE