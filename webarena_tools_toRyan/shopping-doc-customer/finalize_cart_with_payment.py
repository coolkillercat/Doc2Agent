import requests
import json

def get_shopping_customer_auth_token():
    """
    Get customer authentication token from the API.
    
    Returns:
        str: Authentication token for the customer
        
    Example:
        token = get_shopping_customer_auth_token()
    """
    response = requests.post(
        url = 'http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770/rest/default/V1/integration/customer/token',
        headers = {
            'content-type': 'application/json'
        },
        data = json.dumps({
            'username': 'emma.lopez@gmail.com',
            'password': 'Password.123'
        })
    )
    return "Bearer " + response.text.strip('"')


def finalize_cart_with_payment(payment_method_code: str = "checkmo", customer_email: str = "jdoe@example.com", 
                              region: str = "New York", region_id: int = 43, region_code: str = "NY",
                              country_id: str = "US", street: list = ["123 Oak Ave"],
                              postcode: str = "10577", city: str = "Purchase",
                              telephone: str = "512-555-1111", firstname: str = "Jane",
                              lastname: str = "Doe") -> requests.Response:
    """
    Finalizes the current shopping cart by providing payment method and billing information, 
    converting it to an order and returning the order ID.
    
    Args:
        payment_method_code (str): The payment method code (default: "checkmo")
        customer_email (str): Email of the customer (default: "jdoe@example.com")
        region (str): Billing address region (default: "New York")
        region_id (int): Billing address region ID (default: 43)
        region_code (str): Billing address region code (default: "NY")
        country_id (str): Billing address country ID (default: "US")
        street (list): List of street address lines (default: ["123 Oak Ave"])
        postcode (str): Billing address postal code (default: "10577")
        city (str): Billing address city (default: "Purchase")
        telephone (str): Customer's telephone number (default: "512-555-1111")
        firstname (str): Customer's first name (default: "Jane")
        lastname (str): Customer's last name (default: "Doe")
        
    Returns:
        requests.Response: The API response containing the order ID
        
    Example:
        # Using default values
        response = finalize_cart_with_payment()
        
        # Using custom values
        response = finalize_cart_with_payment(
            payment_method_code="checkmo",
            customer_email="john.lee@yahoo.com",
            region="Illinois",
            region_id=23,
            region_code="IL",
            country_id="US",
            street=["456 Michigan Ave"],
            postcode="60611",
            city="Chicago",
            telephone="3125551234",
            firstname="John",
            lastname="Lee"
        )
    """
    headers = {'Content-Type': 'application/json', 'Authorization': get_shopping_customer_auth_token()}
    
    payload = {
        "paymentMethod": {
            "method": payment_method_code
        },
        "billing_address": {
            "email": customer_email,
            "region": region,
            "region_id": region_id,
            "region_code": region_code,
            "country_id": country_id,
            "street": street,
            "postcode": postcode,
            "city": city,
            "telephone": telephone,
            "firstname": firstname,
            "lastname": lastname
        }
    }
    
    response = requests.post(
        url='http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770/rest/default/V1/carts/mine/payment-information',
        headers=headers,
        data=json.dumps(payload)
    )
    
    return response

if __name__ == '__main__':
    r = finalize_cart_with_payment()
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