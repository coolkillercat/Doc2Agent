import json

import requests


def get_shopping_admin_admin_auth_token():
    response = requests.post(
        url='http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7780/rest/default/V1/integration/admin/token',
        headers={'content-type': 'application/json'},
        data=json.dumps({'username': 'admin', 'password': 'admin1234'}),
    )
    return response.json()


def save_sales_rule():
    """
    Creates a new sales rule with the required parameters.

    Returns:
        requests.Response: The API response object
    """
    api_url = 'http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7780/rest/default/V1/salesRules'
    payload = {
        'rule': {
            'name': 'Sample Sales Rule',
            'description': 'Sample sales rule description',
            'is_active': True,
            'stop_rules_processing': False,
            'website_ids': [1],
            'customer_group_ids': [0, 1, 2, 3],
            'coupon_type': 'NO_COUPON',
            'discount_amount': 10,
            'discount_step': 0,
            'simple_action': 'by_percent',
            'apply_to_shipping': False,
            'times_used': 0,
            'is_rss': False,
            'use_auto_generation': False,
            'uses_per_customer': 0,
            'simple_free_shipping': '0',
        }
    }
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + get_shopping_admin_admin_auth_token(),
    }

    response = requests.post(
        url=api_url, headers=headers, json=payload, timeout=50, verify=False
    )
    return response


if __name__ == '__main__':
    r = save_sales_rule()
    r_json = None
    try:
        r_json = r.json()
    except:
        pass
    import json

    result_dict = dict()
    result_dict['status_code'] = r.status_code
    result_dict['text'] = r.text
    result_dict['json'] = r_json
    result_dict['content'] = r.content.decode('utf-8')
    print(json.dumps(result_dict, indent=4))
