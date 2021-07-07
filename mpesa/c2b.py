import requests
from requests.auth import HTTPBasicAuth

from access_token import generate_access_token
import credentials


def register_url():

    my_access_token = generate_access_token()

    api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl"

    headers = {"Authorization": "Bearer %s" % my_access_token}

    request = {
        "ShortCode": credentials.shortcode,
        "ResponseType": "Completed",
        "ConfirmationURL": "https://fundizshop.herokuapp.com/",
        "ValidationURL":   "https://fundizshop.herokuapp.com/",
    }

    try:
        response = requests.post(api_url, json=request, headers=headers)
    except:
        response = requests.post(api_url, json=request, headers=headers, verify=False)

    print(response.text)


# register_url()


def simulate_c2b_transaction():
    my_access_token = generate_access_token()

    api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/simulate"

    headers = {"Authorization": "Bearer %s" % my_access_token}

    request = {
        "ShortCode": credentials.shortcode,
        "CommandID": "CustomerPayBillOnline",
        "Amount": "4",
        "Msisdn": credentials.test_msisdn,
        "BillRefNumber": "myaccnumber",
    }
    try:
        response = requests.post(api_url, json=request, headers=headers)

    except:
        response = requests.post(api_url, json=request, headers=headers, verify=False)

    print(response.text)


simulate_c2b_transaction()
