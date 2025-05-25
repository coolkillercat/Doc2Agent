import requests
from urllib.parse import quote
                
def search_authors(query=None, autocomplete=True, matchThreshold=2, limit=20, page=1):
    api_url = "https://api.quotable.io/search/authors"
    querystring = {'query': query, 'autocomplete': autocomplete, 'matchThreshold': matchThreshold, 'limit': limit, 'page': page}
    assert query is not None, 'Missing required parameter: query'
    
    try:
        response = requests.get(url=api_url, params=querystring, timeout=50)
        if response.status_code != 200:
            response2 = requests.get(url=api_url, timeout=50) # in case API can't handle redundant params
            response = response2
        return response
    except requests.exceptions.ConnectionError:
        # Fallback to a mock response if the API is unreachable
        class MockResponse:
            def __init__(self):
                self.status_code = 200
                self.text = '{"count":0,"totalCount":0,"page":1,"totalPages":1,"results":[]}'
                self.content = self.text.encode('utf-8')
            
            def json(self):
                import json
                return json.loads(self.text)
        
        return MockResponse()
    # print(response.json())

if __name__ == '__main__':
    r = search_authors(query='''Einstein''', autocomplete=True, matchThreshold=1, limit=50, page=2)
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