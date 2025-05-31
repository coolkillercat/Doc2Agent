# 🛠️ MCP Server Tool Registry

This project builds a minimal **Modular Command Processor (MCP)** system that can:
- Accept an API URL
- Extract tools from the API
- Register those tools
- Display them in a visual interface

---

## 📦 Components Built

### 1. `mcp_server.py`
A FastAPI server that:
- Exposes a POST endpoint at `/process-api/`
- Accepts `{ "api_url": "https://example.com/openapi.json" }`
- Runs the tool extractor and returns logs

### 2. `tool_registry.json`
A JSON file that stores metadata about extracted tools:
- `tool_name`, `method`, `url`, `description`, `required_parameters`, `example`
- Auto-updated every time tools are extracted

### 3. `tool_map.py`
A Streamlit-based dashboard to:
- Load tools from `tool_registry.json`
- Filter tools by method (GET/POST/etc.)
- Display usage examples and descriptions

### 4. `build_registry.py`
A script to create a `tool_registry.json` from existing `.py` tool files.
Useful for:
- Regenerating the registry
- Backfilling tools created earlier

---

## 🗂 Folder Structure

```
ToolFactory-review/
├── extractor/              # Tool generator logic
├── output/                 # Generated tool .py files
├── mcp_server.py           # FastAPI server
├── tool_registry.json      # All registered tools
├── tool_map.py             # Streamlit dashboard
├── build_registry.py       # Registry builder from existing tools
├── .env                    # Stores OPENAI_API_KEY
```

---

## 🚀 Usage Guide

### 1. Start the MCP Server
```bash
uvicorn mcp_server:app --reload
```

### 2. Send an API Extraction Request
```bash
curl -X POST "http://127.0.0.1:8000/process-api/" \
  -H "Content-Type: application/json" \
  -d '{"api_url": "https://petstore3.swagger.io/api/v3/openapi.json"}'
```

### 3. Run the Streamlit Viewer
```bash
streamlit run tool_map.py
```

### 4. Build a Tool Registry from Existing Files
```bash
python build_registry.py
```

---

## 📋 Sample tool_registry.json Entry
```json
{
  "tool_name": "get_emojis_by_name",
  "method": "GET",
  "url": "/emojis/name/{name}",
  "description": "Retrieve emojis by a specific name.",
  "required_parameters": ["name"],
  "example": "get_emojis_by_name(name='smile')"
}
```