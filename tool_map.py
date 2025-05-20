import streamlit as st
import json
import os

st.set_page_config(page_title="Tool Registry Viewer", layout="wide")
st.title("🛠️ Tool Registry")

# Check and load registry
if not os.path.exists("tool_registry.json"):
    st.warning("No tools found. Run the extractor to populate tool_registry.json.")
    st.stop()

with open("tool_registry.json") as f:
    tools = json.load(f)

# Sidebar Filters
st.sidebar.header("🔍 Filter Tools")
methods = list(set(t["method"] for t in tools))
selected_methods = st.sidebar.multiselect("HTTP Methods", methods, default=methods)

# Filtered tools
filtered = [t for t in tools if t["method"] in selected_methods]

# Display each tool
for tool in filtered:
    st.markdown(f"### 🔧 `{tool['tool_name']}`")
    st.write(f"**Method:** `{tool['method']}`")
    st.write(f"**URL:** `{tool['url']}`")
    st.write(f"**Description:** {tool.get('description', 'No description')}\n")
    st.code(tool["example"], language="python")
    st.divider()
