import json
import requests
def get_shopping_admin_auth_token():
    """
    get_shopping_admin_auth_token function.
    
    Returns:
        Returns a list of out-of-stock products with search criteria details and total count of matching items.
    """
    ENDPOINT = 'http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7780'
    response = requests.post(
        url = f'{ENDPOINT}/rest/default/V1/integration/admin/token',
        headers = {
            'content-type': 'application/json'
        },
        data = json.dumps({
            'username': 'admin',
            'password': 'admin1234'
        })
    )
    return "Bearer " + response.json()
headers = {
    'Authorization': get_shopping_admin_auth_token(),
    "Content-Type": "application/json"
}
example_response = requests.get('http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7780/rest/default/V1/orders?searchCriteria%5Bfilter_groups%5D%5B0%5D%5Bfilters%5D%5B0%5D%5Bfield%5D=created_at&searchCriteria%5Bfilter_groups%5D%5B0%5D%5Bfilters%5D%5B0%5D%5Bvalue%5D=2022-01-01+00%3A00%3A00&searchCriteria%5Bfilter_groups%5D%5B0%5D%5Bfilters%5D%5B0%5D%5Bcondition_type%5D=gteq&searchCriteria%5Bfilter_groups%5D%5B1%5D%5Bfilters%5D%5B0%5D%5Bfield%5D=created_at&searchCriteria%5Bfilter_groups%5D%5B1%5D%5Bfilters%5D%5B0%5D%5Bvalue%5D=2022-03-31+23%3A59%3A59&searchCriteria%5Bfilter_groups%5D%5B1%5D%5Bfilters%5D%5B0%5D%5Bcondition_type%5D=lteq&searchCriteria%5BpageSize%5D=100&searchCriteria%5BsortOrders%5D%5B0%5D%5Bfield%5D=created_at&searchCriteria%5BsortOrders%5D%5B0%5D%5Bdirection%5D=ASC', headers=headers).json()
print(example_response)






def extract_json_key_hierarchy(json_obj, max_depth=10, keep_array_items=1):
    """
    Extract key hierarchy from JSON object, keeping only keys and limiting array items.
    
    Args:
        json_obj: JSON object to extract hierarchy from
        max_depth: Maximum depth to traverse
        keep_array_items: Number of array items to keep (default: 1)
    
    Returns:
        dict: Simplified JSON structure with key hierarchy
    """
    def _extract_recursive(obj, current_depth=0):
        if current_depth >= max_depth:
            return "..."
        
        if isinstance(obj, dict):
            result = {}
            for key, value in obj.items():
                result[key] = _extract_recursive(value, current_depth + 1)
            return result
        elif isinstance(obj, list):
            if len(obj) == 0:
                return []
            # Keep only the first item(s) from arrays
            items_to_keep = min(keep_array_items, len(obj))
            result = []
            for i in range(items_to_keep):
                result.append(_extract_recursive(obj[i], current_depth + 1))
            if len(obj) > keep_array_items:
                result.append("...")
            return result
        else:
            # For primitive types, just indicate the type
            return f"<{type(obj).__name__}>"
    
    return _extract_recursive(json_obj)

print(json.dumps(extract_json_key_hierarchy(example_response, max_depth=5), indent=4))