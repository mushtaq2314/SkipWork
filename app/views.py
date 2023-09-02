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
def payment(request):
    return render(request,'index.html')
def intermediate(request):
    work = request.GET.get('work',None)
    if(work=='Chart Work'):
        return render(request,'intermediate_chart.html',{'work':work})
    return render(request,'intermediate.html',{'work':work})
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
    # print(data)
    return render(request,'db.html',{'data':data})
def order(request):
    category = request.GET.get('category',None)
    work = request.GET.get('work',None)
    if request.method =='POST':
        print(request.POST)
        context = request.POST
        if(request.POST['work']=='Assignment'):
            if(request.POST['category']=='Express Lane'):
                cost = int(request.POST['sides'])*14 + int(request.POST['diagrams'])*4
            if(request.POST['category']=='Fast Lane'):
                cost = int(request.POST['sides'])*12 + int(request.POST['diagrams'])*4
            if(request.POST['category']=='Regular Lane'):
                cost = int(request.POST['sides'])*10 + int(request.POST['diagrams'])*4
                
        return render(request,'payment.html',{'context':context,'cost':cost})
    #     name = request.POST['fname']+' '+request.POST['lname']
    #     email = request.POST['email']
    #     mobile = request.POST['mobile']
    #     message = request.POST['message']
    #     category = request.POST['category']
    #     file = request.FILES['pdf']
    #     # print(email,category)
    #     obj = Order(OrderID="SW-"+month+str(len(Order.objects.values())+1),customer_name=name,customer_email=email,customer_mobile=mobile,document= file,special_instructions=message,order_date=str(today),order_category=category)
    #     obj.save()
    # print(len(Order.objects.values()))
    if(work=='Assignment'):
        return render(request,'order_a.html',{'category':category,'work':work})
    elif(work=='Record'):
        return render(request,'order_r.html',{'category':category,'work':work})
    else:
        return render(request,'order_c.html',{'category':category,'work':work})
        

from django.http import JsonResponse

def delete_order(request, order_id):
    try:
        path=Order.objects.filter(OrderID=order_id).values_list()[0][6]
        # os.remove(f'./media/{path}')
        os.remove(f'/home/skipwork/SkipWork/media/{path}')
        Order.objects.filter(OrderID=order_id).delete()
        return JsonResponse({"success": True})
    except Order.DoesNotExist:
        return JsonResponse({"success": False})


#Contact Form
from django.core.mail import send_mail
from django.conf import settings

def contact(request):
    if(request.method == 'POST'):
        subject = 'There is someone who wants to contact you!'
        name = request.POST['name']
        mobile = request.POST['mobile']
        recipient_list = request.POST.get('mail')
        message = request.POST['message']+f'\n\nName: {name}\nEmail: {recipient_list}\nMobile: {mobile}'
        print(message)
        email_from = settings.EMAIL_HOST_USER
        send_mail( subject, message, email_from, [email_from] )
        #Sending mail to the customer
        subject = 'Reply from SkipWork'
        message = f'Hey {name}, we have recieved your query. Our team will contact you soon through email or call.'
        send_mail( subject, message, email_from, [recipient_list] )

    return render(request,'index.html')    