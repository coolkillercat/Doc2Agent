import requests, json
from urllib.parse import quote

def get_shopping_customer_auth_token():
    response = requests.post(
        url = f'http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770/rest/default/V1/integration/customer/token',
        headers = {
            'content-type': 'application/json'
        },
        data = json.dumps({
            'username': 'emma.lopez@gmail.com',
            'password': 'Password.123'
        })
    )
    return response.json()

def get_pickup_locations(searchRequest_area__radius_=None, searchRequest_area__searchTerm_=None, searchRequest_filters__country__value_=None, searchRequest_filters__country__conditionType_=None, searchRequest_filters__postcode__value_=None, searchRequest_filters__postcode__conditionType_=None, searchRequest_filters__region__value_=None, searchRequest_filters__region__conditionType_=None, searchRequest_filters__regionId__value_=None, searchRequest_filters__regionId__conditionType_=None, searchRequest_filters__city__value_=None, searchRequest_filters__city__conditionType_=None, searchRequest_filters__street__value_=None, searchRequest_filters__street__conditionType_=None, searchRequest_filters__name__value_=None, searchRequest_filters__name__conditionType_=None, searchRequest_filters__pickupLocationCode__value_=None, searchRequest_filters__pickupLocationCode__conditionType_=None, searchRequest_pageSize_=None, searchRequest_currentPage_=None, searchRequest_scopeType_=None, searchRequest_scopeCode_=None, searchRequest_sort__0__field_=None, searchRequest_sort__0__direction_=None, searchRequest_extensionAttributes__productsInfo__0__sku_=None):
    """
    Get Pickup Locations according to the results of filtration by Search Request.
    
    Parameters:
    - searchRequest_area__radius_ (int): Radius for area search, e.g. 10
    - searchRequest_area__searchTerm_ (str): Search term for area, e.g. 'New York'
    - searchRequest_filters__country__value_ (str): Country filter value, e.g. 'US'
    - searchRequest_filters__country__conditionType_ (str): Country filter condition, e.g. 'eq'
    - searchRequest_filters__postcode__value_ (str): Postcode filter value, e.g. '10001'
    - searchRequest_filters__postcode__conditionType_ (str): Postcode filter condition, e.g. 'eq'
    - searchRequest_filters__region__value_ (str): Region filter value, e.g. 'NY'
    - searchRequest_filters__region__conditionType_ (str): Region filter condition, e.g. 'eq'
    - searchRequest_filters__regionId__value_ (str): Region ID filter value, e.g. '43'
    - searchRequest_filters__regionId__conditionType_ (str): Region ID filter condition, e.g. 'eq'
    - searchRequest_filters__city__value_ (str): City filter value, e.g. 'New York'
    - searchRequest_filters__city__conditionType_ (str): City filter condition, e.g. 'eq'
    - searchRequest_filters__street__value_ (str): Street filter value, e.g. '5th Avenue'
    - searchRequest_filters__street__conditionType_ (str): Street filter condition, e.g. 'eq'
    - searchRequest_filters__name__value_ (str): Name filter value, e.g. 'Store Name'
    - searchRequest_filters__name__conditionType_ (str): Name filter condition, e.g. 'eq'
    - searchRequest_filters__pickupLocationCode__value_ (str): Pickup location code filter value, e.g. 'LOC123'
    - searchRequest_filters__pickupLocationCode__conditionType_ (str): Pickup location code filter condition, e.g. 'eq'
    - searchRequest_pageSize_ (int): Page size, e.g. 20
    - searchRequest_currentPage_ (int): Current page, e.g. 1
    - searchRequest_scopeType_ (str): Scope type, e.g. 'website'
    - searchRequest_scopeCode_ (str): Scope code, e.g. 'base'
    - searchRequest_sort__0__field_ (str): Sort field, e.g. 'name'
    - searchRequest_sort__0__direction_ (str): Sort direction, e.g. 'ASC'
    - searchRequest_extensionAttributes__productsInfo__0__sku_ (str): Product SKU, e.g. 'SKU123'
    
    Returns:
    - Response object from the API call
    """
    api_url = f"http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770/rest/default/V1/inventory/in-store-pickup/pickup-locations"
    
    # Create searchRequest parameter
    searchRequest = {}
    
    if searchRequest_area__radius_ is not None or searchRequest_area__searchTerm_ is not None:
        searchRequest['area'] = {}
        if searchRequest_area__radius_ is not None:
            searchRequest['area']['radius'] = searchRequest_area__radius_
        if searchRequest_area__searchTerm_ is not None:
            searchRequest['area']['searchTerm'] = searchRequest_area__searchTerm_
    
    # Add filters
    filters = {}
    if searchRequest_filters__country__value_ is not None:
        filters['country'] = {'value': searchRequest_filters__country__value_}
        if searchRequest_filters__country__conditionType_ is not None:
            filters['country']['conditionType'] = searchRequest_filters__country__conditionType_
    
    if searchRequest_filters__postcode__value_ is not None:
        filters['postcode'] = {'value': searchRequest_filters__postcode__value_}
        if searchRequest_filters__postcode__conditionType_ is not None:
            filters['postcode']['conditionType'] = searchRequest_filters__postcode__conditionType_
    
    if searchRequest_filters__region__value_ is not None:
        filters['region'] = {'value': searchRequest_filters__region__value_}
        if searchRequest_filters__region__conditionType_ is not None:
            filters['region']['conditionType'] = searchRequest_filters__region__conditionType_
    
    if searchRequest_filters__regionId__value_ is not None:
        filters['regionId'] = {'value': searchRequest_filters__regionId__value_}
        if searchRequest_filters__regionId__conditionType_ is not None:
            filters['regionId']['conditionType'] = searchRequest_filters__regionId__conditionType_
    
    if searchRequest_filters__city__value_ is not None:
        filters['city'] = {'value': searchRequest_filters__city__value_}
        if searchRequest_filters__city__conditionType_ is not None:
            filters['city']['conditionType'] = searchRequest_filters__city__conditionType_
    
    if searchRequest_filters__street__value_ is not None:
        filters['street'] = {'value': searchRequest_filters__street__value_}
        if searchRequest_filters__street__conditionType_ is not None:
            filters['street']['conditionType'] = searchRequest_filters__street__conditionType_
    
    if searchRequest_filters__name__value_ is not None:
        filters['name'] = {'value': searchRequest_filters__name__value_}
        if searchRequest_filters__name__conditionType_ is not None:
            filters['name']['conditionType'] = searchRequest_filters__name__conditionType_
    
    if searchRequest_filters__pickupLocationCode__value_ is not None:
        filters['pickupLocationCode'] = {'value': searchRequest_filters__pickupLocationCode__value_}
        if searchRequest_filters__pickupLocationCode__conditionType_ is not None:
            filters['pickupLocation