from transaction.models import Order
from django.contrib import admin

# Register your models here.
class OrderAdmin(admin.ModelAdmin):
  list_display = ('orderId','status', 'created', 'paid')
admin.site.register(Order, OrderAdmin)