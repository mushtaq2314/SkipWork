from django.shortcuts import render
from .models import Order
# Create your views here.
from datetime import datetime,date
import calendar
today = date.today()
now = datetime.now()
month=calendar.month_abbr[now.month]
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
        obj = Order(OrderID="SW"+str(len(Order.objects.values())+1),customer_name=name,customer_email=email,customer_mobile=mobile,document= file,special_instructions=message,order_date=str(today))
        obj.save()
    category = request.GET.get('category',None)
    print(category)
    print(len(Order.objects.values()))
    return render(request,'order.html',{'category':category})