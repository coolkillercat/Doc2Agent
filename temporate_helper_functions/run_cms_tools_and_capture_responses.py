#!/usr/bin/env python3
"""
Script to run all CMS tools and capture their responses as _response.json files.
This will generate the missing response files needed for returns documentation regeneration.
"""

import os
import json
import subprocess
import sys
import time
from pathlib import Path

def ensure_response_directory():
    """
    Ensure the response directory exists.
    
    Returns:
        str: Path to the response directory
    """
    response_dir = "extractor/apidocs/concatnated-admin"
    os.makedirs(response_dir, exist_ok=True)
    return response_dir

def run_cms_tool(tool_path, tool_name, response_dir):
    """
    Run a single CMS tool and capture its response.
    
    Args:
        tool_path: Path to the tool .py file
        tool_name: Name of the tool (without .py extension)
        response_dir: Directory to save response files
    
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        print(f"  🔄 Running tool: {tool_name}")
        
        # Run the tool and capture output
        result = subprocess.run(
            [sys.executable, tool_path],
            capture_output=True,
            text=True,
            timeout=60,  # 60 second timeout
            cwd=os.getcwd()
        )
        
        print(f"  📊 Exit code: {result.returncode}")
        
        # Create response data structure
        response_data = {
            "status_code": result.returncode,
            "text": result.stdout,
            "json": None,
            "content": result.stdout,
            "stderr": result.stderr
        }
        
        # Try to parse stdout as JSON
        if result.stdout.strip():
            try:
                response_data["json"] = json.loads(result.stdout)
                print(f"  ✅ Successfully parsed JSON output")
            except json.JSONDecodeError as e:
                print(f"  ⚠️  Could not parse output as JSON: {str(e)}")
                print(f"  📝 Output preview: {result.stdout[:200]}...")
        
        # Save response file
        response_filename = f"{tool_name}_response.json"
        response_path = os.path.join(response_dir, response_filename)
        
        with open(response_path, 'w', encoding='utf-8') as f:
            json.dump(response_data, f, indent=2, ensure_ascii=False)
        
        print(f"  💾 Saved response to: {response_path}")
        
        if result.returncode == 0:
            print(f"  ✅ Tool executed successfully")
            return True
        else:
            print(f"  ⚠️  Tool returned non-zero exit code: {result.returncode}")
            if result.stderr:
                print(f"  🔍 Error output: {result.stderr[:200]}...")
            return True  # Still consider it successful as we captured the response
            
    except subprocess.TimeoutExpired:
        print(f"  ⏰ Tool timed out after 60 seconds")
        
        # Save timeout response
        response_data = {
            "status_code": -1,
            "text": "Tool execution timed out",
            "json": None,
            "content": "Tool execution timed out",
            "stderr": "Timeout after 60 seconds"
        }
        
        response_filename = f"{tool_name}_response.json"
        response_path = os.path.join(response_dir, response_filename)
        
        with open(response_path, 'w', encoding='utf-8') as f:
            json.dump(response_data, f, indent=2, ensure_ascii=False)
        
        return False
        
    except Exception as e:
        print(f"  ❌ Error running tool: {str(e)}")
        
        # Save error response
        response_data = {
            "status_code": -2,
            "text": f"Error running tool: {str(e)}",
            "json": None,
            "content": f"Error running tool: {str(e)}",
            "stderr": str(e)
        }
        
        response_filename = f"{tool_name}_response.json"
        response_path = os.path.join(response_dir, response_filename)
        
        with open(response_path, 'w', encoding='utf-8') as f:
            json.dump(response_data, f, indent=2, ensure_ascii=False)
        
        return False

def run_all_cms_tools():
    """
    Run all CMS tools and capture their responses.
    
    Returns:
        tuple: (success_count, error_count, total_count)
    """
    cms_dir = "webarena_tools_toRyan/cms"
    
    if not os.path.exists(cms_dir):
        print(f"❌ Error: Directory {cms_dir} not found!")
        return 0, 0, 0
    
    # Ensure response directory exists
    response_dir = ensure_response_directory()
    print(f"📁 Response files will be saved to: {response_dir}")
    
    # Find all Python files in the CMS directory
    tool_files = []
    for file in os.listdir(cms_dir):
        if file.endswith('.py'):
            tool_files.append(file)
    
    if not tool_files:
        print(f"❌ No Python files found in {cms_dir}")
        return 0, 0, 0
    
    print(f"🔍 Found {len(tool_files)} CMS tools to run")
    print("=" * 60)
    
    success_count = 0
    error_count = 0
    
    for i, tool_file in enumerate(sorted(tool_files), 1):
        tool_name = tool_file[:-3]  # Remove .py extension
        tool_path = os.path.join(cms_dir, tool_file)
        
        print(f"\n[{i}/{len(tool_files)}] Processing: {tool_file}")
        
        if run_cms_tool(tool_path, tool_name, response_dir):
            success_count += 1
        else:
            error_count += 1
        
        # Small delay between tools to avoid overwhelming the API
        time.sleep(1)
    
    return success_count, error_count, len(tool_files)

def check_existing_responses():
    """
    Check which response files already exist.
    
    Returns:
        tuple: (existing_files, missing_files)
    """
    cms_dir = "webarena_tools_toRyan/cms"
    response_dir = "extractor/apidocs/concatnated-admin"
    
    if not os.path.exists(cms_dir):
        return [], []
    
    tool_files = [f[:-3] for f in os.listdir(cms_dir) if f.endswith('.py')]
    existing_files = []
    missing_files = []
    
    for tool_name in tool_files:
        response_file = f"{tool_name}_response.json"
        response_path = os.path.join(response_dir, response_file)
        
        if os.path.exists(response_path):
            existing_files.append(tool_name)
        else:
            missing_files.append(tool_name)
    
    return existing_files, missing_files

def main():
    """Main function to run all CMS tools and capture responses."""
    print("CMS Tools Response Capture Script")
    print("=" * 60)
    
    # Check existing responses
    existing_files, missing_files = check_existing_responses()
    
    print(f"📊 Response File Status:")
    print(f"   ✅ Existing response files: {len(existing_files)}")
    print(f"   ❌ Missing response files: {len(missing_files)}")
    
    if missing_files:
        print(f"\n📝 Missing response files for:")
        for tool_name in missing_files[:10]:  # Show first 10
            print(f"   - {tool_name}")
        if len(missing_files) > 10:
            print(f"   ... and {len(missing_files) - 10} more")
    
    print("\n" + "=" * 60)
    
    # Ask user if they want to proceed
    print("⚠️  WARNING: This will execute all CMS tools and may take some time.")
    print("   Each tool will make API calls to the server.")
    print("   Make sure the server is running and accessible.")
    
    try:
        user_input = input("\nDo you want to proceed? (y/N): ").strip().lower()
    except:
        user_input = "n"
    
    if user_input not in ['y', 'yes']:
        print("❌ Operation cancelled by user.")
        return
    
    print("\n🚀 Starting CMS tools execution...")
    
    # Run all tools
    success_count, error_count, total_count = run_all_cms_tools()
    
    # Summary
    print("\n" + "=" * 60)
    print("EXECUTION SUMMARY")
    print("=" * 60)
    print(f"Total tools processed: {total_count}")
    print(f"✅ Successful executions: {success_count}")
    print(f"❌ Failed executions: {error_count}")
    
    if success_count > 0:
        print(f"\n🎉 Successfully captured responses from {success_count} tools!")
        print("📝 Response files have been saved and can now be used for returns documentation.")
        
        # Check how many response files we have now
        existing_files, missing_files = check_existing_responses()
        print(f"\n📊 Updated Response File Status:")
        print(f"   ✅ Total response files: {len(existing_files)}")
        print(f"   ❌ Still missing: {len(missing_files)}")
        
        if len(missing_files) == 0:
            print("\n🎯 All CMS tools now have response files!")
            print("   You can now run regenerate_cms_returns.py to update all documentation.")
    
    if error_count > 0:
        print(f"\n⚠️  {error_count} tools encountered errors during execution.")
        print("   Check the individual tool outputs above for details.")
        print("   Common causes: API server not running, network issues, or tool bugs.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nScript interrupted by user.")
    except Exception as e:
        print(f"\nUnexpected error: {str(e)}")
        import traceback
        traceback.print_exc()
        print("Please check your environment and try again.") 