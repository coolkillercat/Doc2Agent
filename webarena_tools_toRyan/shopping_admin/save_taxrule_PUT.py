import requests
import json
from urllib.parse import quote

def get_shopping_admin_auth_token():
    ENDPOINT = 'http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770'
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


def save_taxrule(tax_rule_data=None):
    """
    Save a tax rule using the Magento API.
    
    Args:
        tax_rule_data (dict): The tax rule data to save. Must include a 'rule' field.
            Example:
            {
                "code": "Tax Rule Code",
                "priority": 0,
                "position": 0,
                "customer_tax_class_ids": [3],
                "product_tax_class_ids": [2],
                "tax_rate_ids": [1],
                "calculate_subtotal": False,
                "rule": "Tax Rule Name"
            }
    
    Returns:
        requests.Response: The API response object
    """
    api_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770/rest/default/V1/taxRules"
    headers = {'Content-Type': 'application/json', 'Authorization': get_shopping_admin_auth_token()}
    
    assert tax_rule_data is not None, 'Missing required parameter: tax_rule_data'
    assert 'rule' in tax_rule_data, 'Missing required field: rule in tax_rule_data'
    
    response = requests.post(url=api_url, json=tax_rule_data, headers=headers, timeout=50, verify=False)
    return response

if __name__ == '__main__':
    # Example tax rule data with required 'rule' field
    example_tax_rule = {
        "code": "Test Tax Rule",
        "priority": 0,
        "position": 0,
        "customer_tax_class_ids": [3],
        "product_tax_class_ids": [2],
        "tax_rate_ids": [1],
        "calculate_subtotal": False,
        "rule": "Test Tax Rule Name"
    }
    
    r = save_taxrule(tax_rule_data=example_tax_rule)
    r_json = None
    try:
        r_json = r.json()
    except:
        pass
    
    result_dict = dict()
    result_dict['status_code'] = r.status_code
    result_dict['text'] = r.text
    result_dict['json'] = r_json
    result_dict['content'] = r.content.decode("utf-8")
    print(json.dumps(result_dict, indent=4))