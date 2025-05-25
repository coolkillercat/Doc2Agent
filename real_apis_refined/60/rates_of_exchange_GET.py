import requests
from urllib.parse import quote
                
def rates_of_exchange(fields='All fields', filter='No filters', sort='First column listed', format='JSON', page_size_=100, page_number_=1):
    api_url = f"https://api.fiscaldata.treasury.gov/services/api/fiscal_service/v1/accounting/od/rates_of_exchange"
    querystring = {'fields': fields, 'filter': filter, 'sort': sort, 'format': format, 'page_size_': page_size_, 'page_number_': page_number_, }
    
    response = requests.get(url=api_url, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = rates_of_exchange(fields='''country_currency_desc,exchange_rate,record_date''', filter='''country_currency_desc:in:(Canada-Dollar,Mexico-Peso),record_date:gte:2020-01-01''', sort='''-record_date''', format='''json''', page_size_=50, page_number_=10)
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

