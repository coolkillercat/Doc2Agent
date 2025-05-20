import os
import json

def extract_tool_metadata(file_path):
    filename = os.path.basename(file_path)
    tool_name = filename.replace(".py", "")
    parts = tool_name.split("_")
    method = parts[-1] if parts[-1] in {"GET", "POST", "PUT", "DELETE"} else "GET"
    base_name = "_".join(parts[:-1])

    # Basic dummy values (you can improve by parsing the .py)
    return {
        "tool_name": base_name,
        "method": method,
        "url": f"/{base_name.replace('_', '/')}",
        "description": f"Auto-generated tool for `{base_name}`",
        "required_parameters": [],
        "example": f"{base_name}()"
    }

def build_registry_from_folder(folder):
    registry = []
    for filename in os.listdir(folder):
        if filename.endswith(".py"):
            path = os.path.join(folder, filename)
            registry.append(extract_tool_metadata(path))
    return registry

if __name__ == "__main__":
    folder = "extractor/apidocs/example"
    registry = build_registry_from_folder(folder)
    with open("tool_registry.json", "w") as f:
        json.dump(registry, f, indent=2)
    print("✅ tool_registry.json created with", len(registry), "tools.")
