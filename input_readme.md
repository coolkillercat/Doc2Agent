# 🧠 MCP Tool Registry and Generator

This project is a modular Command Processor (MCP) that extracts tools from public API specifications (OpenAPI or HTML), converts them into executable code templates, and builds a searchable registry + visual map.

---

## 🔧 What We Created

### ✅ Backend Pipeline

* **FastAPI-based MCP Server** that accepts an API URL.
* **`Extractor` class** for parsing API HTML content using LLM (GPT-4o).
* **`convert_openapi_to_toolformat()`** to parse OpenAPI specs into a custom tool schema.
* **`Generator` class** that:

  * Parses structured API descriptions
  * Generates runnable Python code for each tool (GET/POST)
  * Saves tools to `output/`
  * Registers tools in `tool_registry.json`

### ✅ Frontend Viewer

* A **Streamlit dashboard** (`tool_map.py`) that:

  * Loads and filters tools by method
  * Displays tool name, description, endpoint URL
  * Shows Python example usage

---

## 🔄 What Was Changed

### 📁 `api_code_generator.py`

* Now detects whether the input is a URL or local path
* Downloads OpenAPI JSONs if needed
* Converts OpenAPI to a unified tool format
* Adds a new `save_to_registry()` method to log tools into a central file

### ⚙️ `Extractor`

* Continues to support HTML → tool conversion via GPT

### 🗂 Output Folder Structure

```
ToolFactory-review/
├── extractor/
│   └── api_code_generator.py
├── tool_registry.json         ← cumulative registry
├── output/                    ← generated .py tool files
├── .env                       ← stores your OpenAI key
├── tool_map.py                ← streamlit UI for tool viewing
```

---

## 📥 Inputs

### From Client (via FastAPI):

```json
POST /process-api/
{
  "api_url": "https://petstore3.swagger.io/api/v3/openapi.json"
}
```

* Can be OpenAPI JSON or a link to an HTML doc

### From Command Line:

```bash
python extractor/api_code_generator.py "path_or_url" -o
```

---

## 📤 Outputs

* `output/*.py` — auto-generated Python tool wrappers
* `tool_registry.json` — structured tool metadata:

```json
[
  {
    "tool_name": "get_pet_by_id",
    "method": "GET",
    "url": "https://...",
    "description": "...",
    "required_parameters": ["petId"],
    "example": "get_pet_by_id(petId=123)"
  }
]
```

---

## 📊 Streamlit Interface (`tool_map.py`)

Run it with:

```bash
streamlit run tool_map.py
```

### Features:

* Tool browsing and search by method (GET, POST, etc)
* Visual layout of:

  * Tool name
  * Endpoint and description
  * Python usage examples

---

## 📌 Next Steps (Optional)

* Tag tools by API or domain (finance, healthcare, etc)
* Group tools visually by API title
* Add LangChain-compatible wrappers
* Enable interactive tool test calls in Streamlit
