from django.db import models

class Order(models.Model):
  orderId = models.CharField(max_length=1000)
  created =  models.DateTimeField(auto_now_add=True)
  status = models.CharField(max_length=200, null=True)
  paid = models.FloatField(max_length=200, null=True)

  def save_order(self):
      self.save()
  def __str__(self):
    return self.orderId
