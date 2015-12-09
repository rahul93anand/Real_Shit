from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render, HttpResponse,redirect
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from .models import UserProfle, Menu, Restaurant, Restaurant_Review, review , orderplaced
from datetime import date, timedelta
import time
# Create your views here.

def ScreenShot(request):
    return render(request,'screenshot.html')


def rahulanand(request):
    return render(request,'livetracking/rahulanand.html')
def aishwarya(request):
    return render(request,'livetracking/aishwarya.html')
def vishrut(request):
    return render(request,'livetracking/vishrut.html')
def ashutosh(request):
    return render(request,'livetracking/ashutosh.html')


def LiveTracking(request):
    if request.method == "POST":
        incoming_dict = request.POST
        order_no = incoming_dict.get('order_number')
        img = ""
        try:
            order_status = orderplaced.objects.get(order_id = order_no).status
            username = orderplaced.objects.get(order_id = order_no).username
            placed_on = orderplaced.objects.get(order_id = order_no).placed_on
            order_id = orderplaced.objects.get(order_id = order_no).order_id


            return render(request,'livetracking/index.html',{'order_status' : order_status,'order_id' : order_id, 'username' : username , 'placed_on' : placed_on})
        except:
            print "error"


    else:
        return render(request, "livetracking.html")
    return HttpResponse("Live tracking over here bitch")




def WelcomePage(request):
    try:
        print User.objects.all()
    except:
        pass
    return render(request,"index.html")


def SignIn(request):
    print "________________________________"

    if request.method==  "POST":
        detail = request.POST
        email = detail.get('email')
        password = detail.get('password')
        print email
        print password
        try :
            username = User.objects.get(email = email).username
            print username
            pass1 = User.objects.get(email = email).password
            print pass1
        except:
            return HttpResponse("Invalid Credentials")

        user = authenticate(username = username,password = password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponse("active")
            else:
                return HttpResponse("It seems like you haven't verified your account, check your inbox for verification code ;) ")
        else:
            return HttpResponse("Invalid Password or Id")

    return render(request,'Signin.html')




def Register(request):

    if request.method=='POST':
        detail = request.POST
        username = detail.get('username')
        password = detail.get('password')
        email = detail.get('email')
        email_domain_check = email.split('@')
        user_exist = ""

        if email_domain_check[1] == 'st.niituniversity.in' or email_domain_check[1] == 'niituniversity.in':
            try:
                User.objects.get(email = email)
                user_exist = True
            except :
                user_exist = False

            if user_exist:
                return HttpResponse("Sorry you are already registered with the email id " + email)
            today  = str(date.today())
            current_time =  str(time.strftime("%H:%M:%S"))
            otp = today.replace('-', '')  + current_time.replace(':','')
            user = User.objects.create_user(username = username, email = email)
            user.password  = make_password(password=password,salt=None,hasher='unsalted_md5')
            user.is_active = False
            user.save()
            otp_object= UserProfle.objects.create(user = user,otp = otp )
            send_mail("One time registering" , "Dear " +  username + "OTP is :  " + otp  , "foodsquare10@gmail.com", [email])
            return HttpResponse("SUCCESS kindly proceed with log in")


        else:
            return HttpResponse("Sorry the facilities of FoodSquare are only limited to Students and faculty members of NIIT University")


    return render(request,'register.html')



def verification(request):
    if request.method == "POST":
        incoming_dict = request.POST
        username = incoming_dict.get('username')
        verification_number =incoming_dict.get('verification')
        try:
            user = User.objects.get(username = username)
            print "User working"
            otp_created = UserProfle.objects.get(user = user).otp
            print "ops created"
            if otp_created == verification_number:
                user.is_active = True
                user.save()
                return HttpResponse("You got it right! ;)")
            else:
                return HttpResponse("Ooops there was some problem! :(")
        except:
            return HttpResponse("Invalid Credentials")
    else:
        return render(request,'verification.html')




def Load_Menu(request, **kwargs):
    if request.user.is_authenticated():
        rest_name = kwargs.get('menu_name')
        try:
            rest = Restaurant.objects.get(rest_name = rest_name)

            items = Menu.objects.filter(rest_name = rest, avail = True)
            list = []
        except:
            pass
        for x in items:
            only_dish = str(x)
            list.append(only_dish)
        print list

        return render(request,'load_menu.html',{'list' : list})

    else:
        return redirect('/signin')


def Restaurant_Menu(request):
    return render(request,'menu/index.html')

def Review(request, **kwargs):

    comments = []
    comments_objects = review.objects.all()
    for x in comments_objects:
        comments.append(x)




    return render(request,'review/index.html', {'comments' : comments})


def Portfolio(request):
    return render(request, 'portfolio/index.html')

def ContactUs(request):
    if request.method == "POST":

        detail = request.POST
        name = detail.get("name")
        email = detail.get("email")
        message = detail.get("message") + "    EMAIL ID :  " + email
        save_message = detail.get('message') + "    - " + name
        review.objects.create(comment = save_message)
        send_mail("Hey We got a message from " + name, message, 'foodsquare10@gmail.com', ['foodsquare10@gmail.com'])
        send_mail("Thanks For sharing" , "Dear " +  name + " thanks for sharing valuable feedback with us, our team will get back to you shortly xD", "foodsquare10@gmail.com", [email])
        return render(request,"index.html",{'status' : "Message sent"})


def PlaceOrder(request):

    if request.method == "POST":
        incoming_dict = request.POST
        order = ""
        for x in incoming_dict.get('dishes'):
            order = order + x
        print incoming_dict.get('dishes')
        message = "Order Has been placed" + "Order is                 " + order
        print message
        username = request.user
        date_token = str(date.today())
        current_time =  str(time.strftime("%H:%M:%S"))
        order_id = ""
        for x in date_token:
            if x is "-":
                pass
            else:
                order_id = order_id + x

        for x in current_time:
            if x is ":":
                pass
            else:
                order_id = order_id + x


        print "%%%"*10
        name = str(request.user)
        print name
        print orderplaced.objects.all()
        new_order = orderplaced.objects.create(username=name,order = order, order_id = order_id)
        print orderplaced.objects.all()


        send_mail("Incoming Order " , message, 'foodsquare10@gmail.com', ['foodsquare10@gmail.com'])
        #send_mail("Thanks For Ordering" , "Dear " +  request.user + " Your food will reach you shortly!", "foodsquare10@gmail.com", [])


    return HttpResponse(order_id)

