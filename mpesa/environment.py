from requests.auth import HTTPBasicAuth
from datetime import datetime
import requests
import base64
from .credentials import *


def generate_access_token():
    consumerKey = consumer_key
    consumerSecret = consumer_secret
    api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"

    try:
        r = requests.get(api_URL, auth=HTTPBasicAuth(consumerKey, consumerSecret))
    except:
        r = requests.get(api_URL, auth=HTTPBasicAuth(consumerKey, consumerSecret), verify=False)

    # print(r.text)

    json_response = (r.json())

    my_access_token = json_response["access_token"]

    return my_access_token

def get_timestamp():
    unformatted_time = datetime.now()
    formatted_time = unformatted_time.strftime("%Y%m%d%H%M%S")

    return formatted_time


def generate_password(formatted_time):

    data_to_encode = (
        business_short_code + pass_key + formatted_time
    )

    encoded_string = base64.b64encode(data_to_encode.encode())
    decoded_password = encoded_string.decode("utf-8")

    return decoded_password
