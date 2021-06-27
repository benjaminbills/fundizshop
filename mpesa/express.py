import requests
import keys

def lipa_na_mpesa():

    access_token = keys.access_token
    api_url = 'https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest'
    headers = {"Authorization": "Bearer %s" % access_token}
    request = {
        "BusinessShortCode":keys.business_short_code,    
        "Password": keys.password,    
        "Timestamp":keys.timestamp,    
        "TransactionType": keys.transaction_type,    
        "Amount":keys.amount,    
        "PartyA":keys.party_A,    
        "PartyB":keys.party_B,    
        "PhoneNumber":keys.phone_number,    
        "CallBackURL":keys.call_back_URL,    
        "AccountReference":keys.account_reference,    
        "TransactionDesc":keys.transaction_desc
    }
    response = requests.post(api_url, json=request, headers=headers)

    print(response.text)

lipa_na_mpesa()