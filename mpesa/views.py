from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import response
from .models import LNMOnline, C2BPayments
from .serializers import LNMOnlineSerializer, C2BPaymentSerializer
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from datetime import datetime as dt
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse


class LNMCallbackUrlAPIView(CreateAPIView):
    queryset = LNMOnline.objects.all()
    serializer_class = LNMOnlineSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        print(request, "this is the request")
        print(request.data, "this is the request data")
        return JsonResponse("It works", safe=False)
        # merchant_request_id = request.data['Body']['stkCallback']['MerchantRequestID']
        # checkout_request_id = request.data['Body']['stkCallback']['CheckoutRequestID']
        # result_code = request.data['Body']['stkCallback']['ResultCode']
        # result_desc = request.data['Body']['stkCallback']['ResultDesc']
        # amount = request.data['Body']['stkCallback']['CallbackMetadata']['Item'][0]['Value']
        # mpesa_receipt_number = request.data['Body']['stkCallback']['CallbackMetadata']['Item'][1]['Value']
        # phone_number = request.data['Body']['stkCallback']['CallbackMetadata']['Item'][4]['Value']

        
        # model_data = LNMOnline.objects.create(
        #     CheckoutRequestID=checkout_request_id,
        #     MerchantRequestID=merchant_request_id,
        #     Amount=amount,
        #     ResultCode=result_code,
        #     ResultDesc=result_desc,
        #     MpesaReceiptNumber=mpesa_receipt_number,
        #     PhoneNumber=phone_number,
        # )

        # model_data.save()

        # return Response({"ResultDescription": "It works"})
