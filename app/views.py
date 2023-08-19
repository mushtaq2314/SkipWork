from django.shortcuts import render,redirect
from .models import Order
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate,login,logout
import os
# Create your views here.
from datetime import datetime,date
import calendar
today = date.today()
now = datetime.now()
month=calendar.month_abbr[now.month]
print(month,type(month))
def index(request):
    return render(request,'index.html')
def loginuser(request):
    if(request.method=='POST'):
        user = authenticate(username=request.POST['username'],password=request.POST['password'])
        
        if user is not None: 
            login(request,user)
            return redirect('db')
        else:
            return render(request,'login.html',{'message':'Invalid Credentials! Please try again'})
    return render(request,'login.html',{'message':None})
            
def logoutuser(request):
    logout(request)
    return render(request,'index.html')

def db(request):
    if(request.user.is_anonymous):
        return render(request,'login.html',{'message':'Please login first to access the database'})
    data  = list(Order.objects.values_list())
    print(data)
    return render(request,'db.html',{'data':data})
def order(request):
    category = request.GET.get('category',None)
    if request.method =='POST':
        name = request.POST['fname']+' '+request.POST['lname']
        email = request.POST['email']
        mobile = request.POST['mobile']
        message = request.POST['message']
        category = request.POST['category']
        file = request.FILES['pdf']
        print(email,category)
        obj = Order(OrderID="SW-"+month+str(len(Order.objects.values())+1),customer_name=name,customer_email=email,customer_mobile=mobile,document= file,special_instructions=message,order_date=str(today),order_category=category)
        obj.save()
    print(len(Order.objects.values()))
    return render(request,'order.html',{'category':category})

from django.http import JsonResponse

def delete_order(request, order_id):
    try:
        path=Order.objects.filter(OrderID=order_id).values_list()[0][6]
        os.remove(f'./media/{path}')
        Order.objects.filter(OrderID=order_id).delete()
        return JsonResponse({"success": True})
    except Order.DoesNotExist:
        return JsonResponse({"success": False})
