from django.db import models

class Order(models.Model):
    OrderID = models.CharField( max_length=50)
    customer_name = models.CharField( max_length=100)
    customer_mobile = models.CharField( max_length=20)
    customer_email = models.CharField( max_length=100)
    special_instructions = models.CharField(default='None', max_length=100)
    document = models.FileField( null=True)
    order_status = models.CharField(default='None',max_length=100)
    