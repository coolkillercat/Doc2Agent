import requests
from urllib.parse import quote
                
def get_pickup_locations(searchRequest_area__radius_=None, searchRequest_area__searchTerm_=None, searchRequest_filters__country__value_=None, searchRequest_filters__country__conditionType_=None, searchRequest_filters__postcode__value_=None, searchRequest_filters__postcode__conditionType_=None, searchRequest_filters__region__value_=None, searchRequest_filters__region__conditionType_=None, searchRequest_filters__regionId__value_=None, searchRequest_filters__regionId__conditionType_=None, searchRequest_filters__city__value_=None, searchRequest_filters__city__conditionType_=None, searchRequest_filters__street__value_=None, searchRequest_filters__street__conditionType_=None, searchRequest_filters__name__value_=None, searchRequest_filters__name__conditionType_=None, searchRequest_filters__pickupLocationCode__value_=None, searchRequest_filters__pickupLocationCode__conditionType_=None, searchRequest_pageSize_=None, searchRequest_currentPage_=None, searchRequest_scopeType_=None, searchRequest_scopeCode_=None, searchRequest_sort__0__field_=None, searchRequest_sort__0__direction_=None, searchRequest_extensionAttributes__productsInfo__0__sku_=None):
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770/rest/default/V1/inventory/in-store-pickup/pickup-locations/"
    querystring = {'searchRequest_area__radius_': searchRequest_area__radius_, 'searchRequest_area__searchTerm_': searchRequest_area__searchTerm_, 'searchRequest_filters__country__value_': searchRequest_filters__country__value_, 'searchRequest_filters__country__conditionType_': searchRequest_filters__country__conditionType_, 'searchRequest_filters__postcode__value_': searchRequest_filters__postcode__value_, 'searchRequest_filters__postcode__conditionType_': searchRequest_filters__postcode__conditionType_, 'searchRequest_filters__region__value_': searchRequest_filters__region__value_, 'searchRequest_filters__region__conditionType_': searchRequest_filters__region__conditionType_, 'searchRequest_filters__regionId__value_': searchRequest_filters__regionId__value_, 'searchRequest_filters__regionId__conditionType_': searchRequest_filters__regionId__conditionType_, 'searchRequest_filters__city__value_': searchRequest_filters__city__value_, 'searchRequest_filters__city__conditionType_': searchRequest_filters__city__conditionType_, 'searchRequest_filters__street__value_': searchRequest_filters__street__value_, 'searchRequest_filters__street__conditionType_': searchRequest_filters__street__conditionType_, 'searchRequest_filters__name__value_': searchRequest_filters__name__value_, 'searchRequest_filters__name__conditionType_': searchRequest_filters__name__conditionType_, 'searchRequest_filters__pickupLocationCode__value_': searchRequest_filters__pickupLocationCode__value_, 'searchRequest_filters__pickupLocationCode__conditionType_': searchRequest_filters__pickupLocationCode__conditionType_, 'searchRequest_pageSize_': searchRequest_pageSize_, 'searchRequest_currentPage_': searchRequest_currentPage_, 'searchRequest_scopeType_': searchRequest_scopeType_, 'searchRequest_scopeCode_': searchRequest_scopeCode_, 'searchRequest_sort__0__field_': searchRequest_sort__0__field_, 'searchRequest_sort__0__direction_': searchRequest_sort__0__direction_, 'searchRequest_extensionAttributes__productsInfo__0__sku_': searchRequest_extensionAttributes__productsInfo__0__sku_, }
    
    response = requests.get(url=api_url, params=querystring, timeout=50, verify=False)
    if response.status_code != 200:
        response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
        response = response2
    return response
    # print(response.json())

if __name__ == '__main__':
    r = get_pickup_locations(searchRequest_area__radius_=10, searchRequest_area__searchTerm_='''electronics''', searchRequest_filters__country__value_='''US''', searchRequest_filters__country__conditionType_='''eq''', searchRequest_filters__postcode__value_='''10001''', searchRequest_filters__postcode__conditionType_='''eq''', searchRequest_filters__region__value_='''NY''', searchRequest_filters__region__conditionType_='''eq''', searchRequest_filters__regionId__value_='''1''', searchRequest_filters__regionId__conditionType_='''eq''', searchRequest_filters__city__value_='''New York''', searchRequest_filters__city__conditionType_='''eq''', searchRequest_filters__street__value_='''Main St''', searchRequest_filters__street__conditionType_='''eq''', searchRequest_filters__name__value_='''Store A''', searchRequest_filters__name__conditionType_='''eq''', searchRequest_filters__pickupLocationCode__value_='''LOC123''', searchRequest_filters__pickupLocationCode__conditionType_='''eq''', searchRequest_pageSize_=20, searchRequest_currentPage_=1, searchRequest_scopeType_='''online''', searchRequest_scopeCode_='''web''', searchRequest_sort__0__field_='''name''', searchRequest_sort__0__direction_='''asc''', searchRequest_extensionAttributes__productsInfo__0__sku_='''ABC123''')
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

