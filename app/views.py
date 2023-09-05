from django.shortcuts import render,redirect
from .models import Assignment
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate,login,logout
import os
# Create your views here.
from datetime import datetime,date
import calendar
today = date.today()
now = datetime.now()
month=calendar.month_abbr[now.month]
# print(month,type(month))
def index(request):
    return render(request,'index.html')
def payment(request):
    data = request.session.get('data')
    uploaded_file_id = request.session.get('uploaded_file_id')
    if(request.method=='POST'):
        #Saving data to Database
        if data['work']=='Assignment':
                obj = Assignment(OrderID="SW-"+month+str(len(Assignment.objects.values())+1),customer_name=data['fname']+' '+data['lname'],customer_email=data['email'],customer_mobile=data['mobile'],document= request.FILES['pdf'],special_instructions=data['message'],order_date=str(today),order_category=data['category'],frontpage_instructions=data['border_instructions'],customer_school=data['school'])
                obj.save()
                
                subject = 'An '+data['work']+' order has been recieved checkout the database for further details!'
                name = data['fname']+' '+data['lname']
                mobile = data['mobile']
                recipient_list = data['email']
                message =f'\n\nName: {name}\nEmail: {recipient_list}\nMobile: {mobile}'
                print(message)
                email_from = settings.EMAIL_HOST_USER
                send_mail( subject, message, email_from, [email_from] )
                request.session.pop('data',None)
                # print(len(Assignment.objects.values()))
            
    return render(request,'index.html')




def order(request):
    category = request.GET.get('category',None)
    work = request.GET.get('work',None)
    if request.method =='POST':
        request.session['data'] = request.POST
        if(request.POST['work']=='Assignment'):
            if(request.POST['category']=='Express Lane'):
                cost = int(request.POST['sides'])*14 + int(request.POST['diagrams'])*4
            if(request.POST['category']=='Fast Lane'):
                cost = int(request.POST['sides'])*12 + int(request.POST['diagrams'])*4
            if(request.POST['category']=='Regular Lane'):
                cost = int(request.POST['sides'])*10 + int(request.POST['diagrams'])*4
            if(request.POST['binding']=='Spiral'):
                cost+=50    
            if(request.POST['binding']=='Stick'):
                cost+=25
        if(request.POST['work']=='Record'):
            if(request.POST['category']=='Express Lane'):
                cost = int(request.POST['sides'])*14 + int(request.POST['diagrams'])*4
            if(request.POST['category']=='Fast Lane'):
                cost = int(request.POST['sides'])*12 + int(request.POST['diagrams'])*4
            if(request.POST['category']=='Regular Lane'):
                cost = int(request.POST['sides'])*10 + int(request.POST['diagrams'])*4
                
        return render(request,'payment.html',{'cost':cost})
    
    if(work=='Assignment'):
        return render(request,'order_a.html',{'category':category,'work':work})
    elif(work=='Record'):
        return render(request,'order_r.html',{'category':category,'work':work})
    else:
        return render(request,'order_c.html',{'category':category,'work':work})

def intermediate(request):
    work = request.GET.get('work',None)
    if(work=='Chart Work'):
        return render(request,'intermediate_chart.html',{'work':work})
    return render(request,'intermediate.html',{'work':work})        
#delete an order
from django.http import JsonResponse

def delete_order(request, order_id):
    try:
        path=Assignment.objects.filter(OrderID=order_id).values_list()[0][3]
        os.remove(f'./media/{path}')
        # os.remove(f'/home/skipwork/SkipWork/media/{path}')
        Assignment.objects.filter(OrderID=order_id).delete()
        return JsonResponse({"success": True})
    except Assignment.DoesNotExist:
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

# Data base panel
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
    data  = list(Assignment.objects.values_list())
    # print(data)
    return render(request,'db.html',{'data':data})