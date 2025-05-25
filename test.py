import json
import requests
def get_shopping_customer_auth_token():
    ENDPOINT = 'http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770'
    response = requests.post(
        url = f'{ENDPOINT}/rest/default/V1/integration/customer/token',
        headers = {
            'content-type': 'application/json'
        },
        data = json.dumps({
            'username': 'emma.lopez@gmail.com',
            'password': 'Password.123'
        })
    )
    return response.json()

print("customer: ",get_shopping_customer_auth_token())

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
    return response.json()

def get_shopping_admin_admin_auth_token():
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
    return response.json()
print("admin 7780:",get_shopping_admin_admin_auth_token())

print("admin 7770:",get_shopping_admin_auth_token())

# API endpoint
url = 'http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7780/rest/default/V1/orders/3'

# Headers
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer eyJraWQiOiIxIiwiYWxnIjoiSFMyNTYifQ.eyJ1aWQiOjEsInV0eXBpZCI6MiwiaWF0IjoxNzQ3NDQ4MzkzLCJleHAiOjE3NDc0NTE5OTN9.eBiGLVTlTAYxTdLTRdcZ6JY9ZF8vguFZE0dFycwwNq8",
}

payload = {
}

# Make the POST request
response = requests.get(
    url,
    headers=headers,
)
# response = requests.post(
#     url,
#     headers=headers,
#     json=payload
# )
# Print response
print(response.status_code)
print(response.json())
# print(response.text)
# print(get_shopping_admin_auth_token())