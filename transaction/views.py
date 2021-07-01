from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import Order


def paymentComplete(request):
  body = json.loads(request.body)
  print('BODY:', body)
  # chkOrder = Order.objects.filter(orderId=body['orderId'])
  # print(chkOrder)
  order = Order(orderId=body['orderId'], status=body['status'], paid=body['paid'])
  order.save_order()
  return JsonResponse('Payment completed!', safe=False)