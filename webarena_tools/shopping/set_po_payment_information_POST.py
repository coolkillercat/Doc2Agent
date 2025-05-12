import requests
from urllib.parse import quote
                
def set_po_payment_information(paymentInformation=None):
    api_url = f"/V1/carts/mine/po-payment-information"
    payload = {'paymentInformation': paymentInformation, }
    
    response = requests.post(url=api_url, json=payload, timeout=50, verify=False)
    return response
    # print(response.json())

if __name__ == '__main__':
    r = set_po_payment_information(paymentInformation={'method': 'purchase_order', 'po_number': 'PO123456'})
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
    result_dict['content'] = r.content.decode("utf-8")
    print(json.dumps(result_dict, indent=4))

