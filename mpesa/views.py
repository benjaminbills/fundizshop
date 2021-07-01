from django.shortcuts import render
from django.contrib.auth.models import User
from .models import LNMOnline, C2BPayments
from .serializers import LNMOnlineSerializer, C2BPaymentSerializer
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
import pytz
from datetime import datetime as dt


# Create your views here.
class LNMCallbackUrlAPIView(CreateAPIView):
    queryset = LNMOnline.objects.all()
    serializer_class = LNMOnlineSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        print(request.data, "this is the request data")

        merchant_request_id = request.data['Body']['stkCallback']['MerchantRequestID']
        checkout_request_id = request.data['Body']['stkCallback']['CheckoutRequestID']
        result_code = request.data['Body']['stkCallback']['ResultCode']
        result_desc = request.data['Body']['stkCallback']['ResultDesc']
        amount = request.data['Body']['stkCallback']['CallbackMetadata']['Item'][0]['Value']
        mpesa_receipt_number = request.data['Body']['stkCallback']['CallbackMetadata']['Item'][1]['Value']
        balance = ''
        transaction_date = request.data['Body']['stkCallback']['CallbackMetadata']['Item'][3]['Value']
        phone_number = request.data['Body']['stkCallback']['CallbackMetadata']['Item'][4]['Value']

        """
        Converting the transaction date into string format 
        """
        str_transaction_datetime = str(transaction_date)
        transaction_datetime = dt.strftime(str_transaction_datetime, '%Y%m%d%H%M%S')
        aware_transaction_datetime = pytz.utc.localize(transaction_datetime)

        model_data = LNMOnline.objects.create(
            CheckoutRequestID=checkout_request_id,
            MerchantRequestID=merchant_request_id,
            Amount=amount,
            ResultCode=result_code,
            ResultDesc=result_desc,
            MpesaReceiptNumber=mpesa_receipt_number,
            Balance=balance,
            TransactionDate=aware_transaction_datetime,
            PhoneNumber=phone_number,
        )
        model_data.save()

        return Response({"ResultDescription": "It worked"})
