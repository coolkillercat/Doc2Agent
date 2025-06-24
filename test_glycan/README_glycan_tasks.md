# Glycan Tool Task Generation

This repository contains scripts to generate research tasks for glycan tools using GPT-4o.

## Files

- `generate_glycan_tasks.py` - Python script that extracts information about the glycan tools and uses GPT-4o to generate tasks
- `generate_glycan_tasks_simple.py` - A simplified version that works with both old and new versions of the OpenAI Python package
- `run_task_generation.sh` - Shell script for Linux/Mac to set the OpenAI API key and run the Python script
- `run_task_generation.bat` - Batch file for Windows to set the OpenAI API key and run the Python script
- `glycan_tasks.jsonl` - Output file containing the generated tasks

## Requirements

- Python 3.6+
- `openai` Python package
- OpenAI API key

## How to Use

1. Make sure you have an OpenAI API key

2. Run the appropriate script with your API key:

   **For Windows:**
   ```
   run_task_generation.bat YOUR_OPENAI_API_KEY
   ```

   **For Linux/Mac:**
   ```bash
   ./run_task_generation.sh YOUR_OPENAI_API_KEY
   ```

   Or on Windows with Git Bash:
   ```bash
   bash run_task_generation.sh YOUR_OPENAI_API_KEY
   ```

3. The script will generate a file called `glycan_tasks.jsonl` containing 50 tasks:
   - 30 single tool tasks
   - 20 multi-step tool tasks

## Advanced Usage

If you encounter any issues with the default script, you can try using the other script version directly:

```bash
# Set the API key
export OPENAI_API_KEY="your-api-key"  # Linux/Mac
set OPENAI_API_KEY="your-api-key"     # Windows

# Run the original script
python generate_glycan_tasks.py

# Or run the simplified script
python generate_glycan_tasks_simple.py
```

## Task Format

Each task in the JSONL file has the following structure:

```json
{
  "question": "The research question",
  "expected_trajectory": "Step by step instructions for using the tool(s)",
  "expected_answer": "The expected answer format or description of the expected output"
}
```

## Example Task

```json
{
  "question": "What is the detailed information for glycan with GlyTouCan accession G17689DH?",
  "expected_trajectory": "Use glygen/glycan_detail_POST.py with glytoucan_ac='G17689DH'",
  "expected_answer": "A JSON response containing detailed information about the glycan G17689DH, including its chemical properties, biological associations, and other metadata."
}
``` 