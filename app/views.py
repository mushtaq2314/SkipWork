from django.shortcuts import render,redirect
from .models import Order
# Create your views here.
from datetime import datetime,date
import calendar
today = date.today()
now = datetime.now()
month=calendar.month_abbr[now.month]
print(month,type(month))
def index(request):
    return render(request,'index.html')
def login(request):
    if(request.method=='POST'):
        if(request.POST['username']=='SkipWorkAdmin'):
            if(request.POST['password']=='skip!@#$'):
                return redirect('db')
    return render(request,'login.html')
def db(request):
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