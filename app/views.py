from django.shortcuts import render
from .models import Order
# Create your views here.
def index(request):
    return render(request,'index.html')
def order(request):
    if request.method =='POST':
        name = request.POST['fname']+' '+request.POST['lname']
        email = request.POST['email']
        mobile = request.POST['mobile']
        message = request.POST['message']
        file = request.FILES['pdf']
        print(email)
        obj = Order(customer_name=name,customer_email=email,customer_mobile=mobile,document= file,special_instructions=message)
        obj.save()

    return render(request,'order.html')