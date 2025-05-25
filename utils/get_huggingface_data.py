import pandas as pd

# Login using e.g. `huggingface-cli login` to access this dataset
df = pd.read_parquet("hf://datasets/billyfin/APIdoc2json/data/train-00000-of-00001-d796dffda9188ea4.parquet")
# print(df['json_form'][0])

import json
# Load and parse JSON for each row
json_data = []
total_endpoints = 0
for json_form in df['json_form']:
    try:
        json_data = json.loads(json_form)
        if 'endpoint' in json_data:
            total_endpoints += len(json_data['endpoints'])
    except json.JSONDecodeError:
        continue

print(f"Total number of endpoints across all JSONs: {total_endpoints}")




# import os
# import json

# # Create the real_apis directory if it doesn't exist
# os.makedirs('./real_apis', exist_ok=True)

# # Iterate through each row in the dataframe
# for idx, json_form in enumerate(df['json_form']):
#     # Create a subdirectory for each row
#     row_dir = os.path.join('./real_apis', str(idx))
#     os.makedirs(row_dir, exist_ok=True)
    
#     # Save the JSON form to a file
#     output_path = os.path.join(row_dir, f'{idx}.txt')
#     with open(output_path, 'w', encoding='utf-8') as f:
#         f.write(json_form)
