from django.db import models

class Assignment(models.Model):
    OrderID = models.CharField( max_length=50)
    order_category = models.CharField(default='None',max_length=100)  
    document = models.FileField(upload_to='assignments/', null=True)
    payment = models.FileField( null=True,upload_to='a_payments/')
    customer_name = models.CharField( max_length=100)
    customer_mobile = models.CharField( max_length=20)
    customer_email = models.CharField( max_length=100)
    customer_school = models.CharField( max_length=100)
    special_instructions = models.CharField(default='None', max_length=1000)
    frontpage_instructions = models.CharField(default='None', max_length=1000)
    order_status = models.CharField(default='None',max_length=100)
    order_date = models.CharField(default='None',max_length=100) 
    delivery_address = models.CharField(default='None',max_length=1000) 

# class temp(models.Model):
#     document = models.FileField( upload_to='temp/',null=True)
    
class Record(models.Model):
    OrderID = models.CharField( max_length=50)
    order_category = models.CharField(default='None',max_length=100)
    customer_name = models.CharField( max_length=100)
    customer_mobile = models.CharField( max_length=20)
    customer_email = models.CharField( max_length=100)
    customer_school = models.CharField( max_length=100)
    special_instructions = models.CharField(default='None', max_length=1000)
    document = models.FileField(upload_to='records/', null=True)
    payment = models.FileField( null=True,upload_to='r_payments/')
    order_status = models.CharField(default='None',max_length=100)
    order_date = models.CharField(default='None',max_length=100) 
    delivery_address = models.CharField(default='None',max_length=1000)