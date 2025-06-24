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


def save_sales_rule(rule_data):
    """
    Save a sales rule using the Magento API.
    
    Args:
        rule_data (dict): A dictionary containing the sales rule data.
            Must include 'rule' key with rule details.
            
    Example:
        rule_data = {
            'rule': {
                'name': 'Summer Sale',
                'description': 'Summer discount',
                'uses_per_customer': 0,
                'is_active': True,
                'stop_rules_processing': False,
                'is_advanced': True,
                'sort_order': 0,
                'discount_amount': 20,
                'discount_step': 0,
                'simple_action': 'by_percent',
                'website_ids': [1],
                'customer_group_ids': [0, 1, 2, 3]
            }
        }
        response = save_sales_rule(rule_data)
    
    Returns:
        requests.Response: The API response object
    """
    api_url = "http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770/rest/default/V1/salesRules"
    headers = {'Content-Type': 'application/json', 'Authorization': get_shopping_admin_auth_token()}
    
    assert rule_data is not None, 'Missing required parameter: rule_data'
    assert 'rule' in rule_data, 'Missing required field: rule'
    
    response = requests.post(url=api_url, json=rule_data, headers=headers, timeout=50, verify=False)
    return response

if __name__ == '__main__':
    rule_data = {
        'rule': {
            'name': 'Summer Sale',
            'description': 'Summer discount',
            'uses_per_customer': 0,
            'is_active': True,
            'stop_rules_processing': False,
            'is_advanced': True,
            'sort_order': 0,
            'discount_amount': 20,
            'discount_step': 0,
            'simple_action': 'by_percent',
            'website_ids': [1],
            'customer_group_ids': [0, 1, 2, 3]
        }
    }
    r = save_sales_rule(rule_data)
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