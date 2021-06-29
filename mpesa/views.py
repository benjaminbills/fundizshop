from django.shortcuts import render
from django.contrib.auth.models import User
from .models import LNMOnline, C2BPayments
from .serializers import LNMOnlineSerializer, C2BPaymentSerializer
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
import pytz
from datetime import datetime


# Create your views here.
class LNMCallbackUrlAPIView(CreateAPIView):
    queryset = LNMOnline.objects.all()
    serializer_class = LNMOnlineSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        print(request.data, "this is the request data")
        return Response(request.data)
        # merchant_request_id = request.data["Body"]["stkCallback"]["MerchantRequestID"]
        # print(merchant_request_id, "this should be MerchantRequestID")
        # checkout_request_id = request.data["Body"]["stkCallback"]["CheckoutRequestID"]
        # result_code = request.data["Body"]["stkCallback"]["ResultCode"]
        # result_description = request.data["Body"]["stkCallback"]["ResultDesc"]
        # amount = request.data["Body"]["stkCallback"]["CallbackMetadata"]["Item"][0][
        #     "Value"
        # ]
        # print(amount, "this should be an amount")
        # mpesa_receipt_number = request.data["Body"]["stkCallback"]["CallbackMetadata"][
        #     "Item"
        # ][1]["Value"]
        # print(mpesa_receipt_number, "this should be an mpesa_receipt_number")
        #
        # balance = ""
        # transaction_date = request.data["Body"]["stkCallback"]["CallbackMetadata"][
        #     "Item"
        # ][3]["Value"]
        # print(transaction_date, "this should be an transaction_date")
        #
        # phone_number = request.data["Body"]["stkCallback"]["CallbackMetadata"]["Item"][
        #     4
        # ]["Value"]
        # print(phone_number, "this should be an phone_number")
        #
        # str_transaction_date = str(transaction_date)
        # print(str_transaction_date, "this should be an str_transaction_date")
        #
        # transaction_datetime = datetime.strptime(str_transaction_date, "%Y%m%d%H%M%S")
        # print(transaction_datetime, "this should be an transaction_datetime")
        #
        # aware_transaction_datetime = pytz.utc.localize(transaction_datetime)
        # print(aware_transaction_datetime, "this should be an aware_transaction_datetime")
        #
        # our_model = LNMOnline.objects.create(
        #     CheckoutRequestID=checkout_request_id,
        #     MerchantRequestID=merchant_request_id,
        #     Amount=amount,
        #     ResultCode=result_code,
        #     ResultDesc=result_description,
        #     MpesaReceiptNumber=mpesa_receipt_number,
        #     Balance=balance,
        #     TransactionDate=aware_transaction_datetime,
        #     PhoneNumber=phone_number,
        # )
        #
        # our_model.save()
        #
        # return Response({"OurResultDesc": "It worked!"})
