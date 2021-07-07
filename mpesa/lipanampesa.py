from django.http import JsonResponse
from requests.auth import HTTPBasicAuth
from requests.models import Response
from .environment import get_timestamp, generate_password, generate_access_token
import requests
from .credentials import *
from .models import LNMOnline


def lipa_na_mpesa(request):
    formatted_time = get_timestamp()
    decoded_password = generate_password(formatted_time)
    access_token = generate_access_token()

    if request.method == 'POST':
        user_number = request.POST.get('phoneNumber')[1:10]
        user_number = "254" + str(user_number)
        user_number = int(float(user_number))
        order_total = request.POST.get('total')
        order_total = int(float(order_total))
        print(user_number)
        print(order_total)

    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"

    headers = {"Authorization": "Bearer %s" % access_token}

    request = {
        "BusinessShortCode": business_short_code,
        "Password": decoded_password,
        "Timestamp": formatted_time,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": order_total,
        "PartyA": user_number,
        "PartyB": business_short_code,
        "PhoneNumber": user_number,
        "CallBackURL": call_back_url,
        "AccountReference": "test aware",
        "TransactionDesc": "Pay School Fees",
    }

    response = requests.post(api_url, json=request, headers=headers)

    print(response.text)
    return JsonResponse("Success", safe=False)
