import requests
import keys


def register_url():

    access_token = keys.access_token
    api_url = 'https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl'
    headers = {"Authorization": "Bearer %s" % access_token}
    request = {
        "ShortCode": keys.short_code,
        "ResponseType": keys.response_type,
        "ConfirmationURL": keys.confirmation_URL,
        "ValidationURL": keys.validation_URL
    }
    response = requests.post(api_url, json=request, headers=headers)

    print(response.text)

# register_url()

def simulate_c2b_transaction():
    access_token = keys.access_token
    api_url = ' https://sandbox.safaricom.co.ke/mpesa/c2b/v1/simulate'
    headers = {"Authorization": "Bearer %s" % access_token}
    request = {
        "CommandID": "CustomerPayBillOnline",
        "Amount":"10",
        "Msisdn":keys.msisdn,
        "BillRefNumber":"00000",
        "ShortCode":keys.short_code
    }

    response = requests.post(api_url, json=request, headers=headers)

    print(response.text)

simulate_c2b_transaction()