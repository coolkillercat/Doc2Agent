import requests
from urllib.parse import quote
                
def create_product(title=None, price=None, description=None, image=None, category=None):
    api_url = f"https://fakestoreapi.com/products"
    payload = {'title': title, 'price': price, 'description': description, 'image': image, 'category': category, }
    assert title is not None, 'Missing required parameter: title'
    assert price is not None, 'Missing required parameter: price'
    assert description is not None, 'Missing required parameter: description'
    assert image is not None, 'Missing required parameter: image'
    assert category is not None, 'Missing required parameter: category'
    
    response = requests.post(url=api_url, json=payload, timeout=50, verify=False)
    return response
    # print(response.json())

if __name__ == '__main__':
    r = create_product(title='''New Product''', price=29.99, description='''This is a new product.''', image='''https://example.com/image.jpg''', category='''electronics''')
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

