from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import JsonResponse

from django.shortcuts import render, redirect

from .models import UserProfile


# Create your views here.
def demo(request):
    branches = ['palakkad', 'thrissur', 'Kozhikkode', 'kochi', 'malappuram']
    return render(request, 'index.html', {'branches': branches})


def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('demo')
        else:
            messages.info(request,"invalid credential")
            return redirect('login')
    return render(request,"login.html")


def logout(request):
    auth.logout(request)
    return redirect('index.html')

def register(request):

    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"check username")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password)
                user.save();
                return redirect('login')
        else:
            messages.info(request,'password not match')
            return redirect('register')


    return render(request,"register.html")


from django.shortcuts import render, redirect
from django.contrib import messages
from .models import UserProfile  # Import your UserProfile model
from django.contrib.auth.models import User

def reg_form(request):
    if request.method == 'POST':
        # Retrieve data from the form
        username = request.POST['name']
        dob = request.POST['dob']
        age = request.POST['age']
        gender = request.POST.get('gender')
        phone_number = request.POST['phone']
        email = request.POST['mail']
        address = request.POST['address']
        district = request.POST.get('district')
        branch = request.POST.get('branch')
        account_type = request.POST.get('accountType')
        materials_provide = request.POST.getlist('materials')
        try:
            age = int(age)  # Convert age to an integer
            phone_number = int(phone_number)
            if User.objects.filter(username=username).exists():
               messages.info(request, "Username already exists")

            elif User.objects.filter(email=email).exists():
               messages.info(request, "Email already exists")

            else:

             user = User.objects.create_user(username=username, email=email)

            user.save()
            # Create the UserProfile object and link it to the user
            user_profile = UserProfile.objects.create(user=user, dob=dob, age=age, gender=gender,
                                                      phone_number=phone_number, address=address,
                                                      district=district, branch=branch,
                                                      account_type=account_type,
                                                      materials_provide=', '.join(materials_provide))
            messages.success(request, "Registration successful. Please login.")
            return redirect('login')
        except ValueError:
               messages.error(request, "Please enter a valid age and phone number.")
               return redirect('reg_form')
    return render(request, "reg_form.html")





