import datetime

from django.contrib import auth
from django.contrib.auth.models import User
from django.core.checks import messages
from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
import random
import string

from django.contrib import messages


# Create your views here.
def hello1(request):
    return HttpResponse("<center><h1>Welcome to TTM Homepage</h1></center>")


def hello123(request):
    return render(request, 'hello123.html')


def newhomepage(request):
    return render(request, 'newhomepage.html')


def travelpackage(request):
    return render(request, 'travelpackage.html')


def print1(request):
    return render(request, 'print_to_console.html')


# it will the html page

def printtoconsole(request):
    if request.method == "POST":
        userinput = request.POST['user_input']
        print(f'user input : {userinput}')
    # return HttpResponse('Form submitted successfully')
    # this function will say what will happen after clicking the button
    a1 = {'userinput': userinput}
    return render(request, 'print_to_console.html', a1)


def random12(request):
    return render(request, "rando.html")


def random123(request):
    if request.method == 'POST':
        input1 = request.POST['input3']
        input2 = int(input1)
        result_str = "".join(random.sample(string.digits, input2))
        print(result_str)
        context = {'result_str': result_str}
    return render(request, "rando.html", context)


def getdate1(request):
    return render(request, 'get_date.html')


def get_date(request):
    if request.method == "POST":
        form = IntegerDateForm(request.POST)
        if form.is_valid():
            integer_value = form.cleaned_data['integer_value']
            date_value = form.cleaned_data['date_value']
            updated_date = date_value + datetime.timedelta(days=integer_value)
            return render(request, 'get_date.html', {'updated_date': updated_date})
    else:
        form = IntegerDateForm()
    return render(request, 'get_date.html', {'form': form})


def tzfunctioncall(request):
    return render(request, 'pytzexample.html')


from django.shortcuts import render, redirect
from .models import Register, contactus  # Assuming your models are in the same app

from .models import Register
from django.shortcuts import render, redirect


def registerloginfunction(request):
    if request.method == 'POST':
        # Extract data from the POST request
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Convert the phone number to an integer
        phonenumber = int(request.POST.get('phonenumber'))

        print(f"Name: {name}, Email: {email}, Password: {password}, Phone: {phonenumber}")

        try:
            # Create a Register instance
            Register.objects.create(
                name=name,
                email=email,
                password=password,
                phonenumber=phonenumber
            )
            print("User registered successfully!")
        except Exception as e:
            print(f"Error creating Register instance: {e}")

    return render(request, 'dbase.html')


import matplotlib.pyplot as plt
import numpy as np


def pie_chart(request):
    if request.method == 'POST':
        form = PieChartForm(request.POST)
        if form.is_valid():
            # Process user input
            y_values = [int(val) for val in form.cleaned_data['y_values'].split(',')]
            labels = [label.strip() for label in form.cleaned_data['labels'].split(',')]

            # Create pie chart
            plt.pie(y_values, labels=labels, startangle=90)
            plt.savefig('static/images/pie_chart.png')  # Save the chart image
            img1 = {'chart_image': '/static/images/pie_chart.png'}
            return render(request, 'chart_form.html', img1)
    else:
        form = PieChartForm()
    return render(request, 'chart_form.html', {'form': form})


def destin(request):
    return render(request, 'destination.html')


def thread(request):
    return render(request, 'insert.html')


def signup(request):
    return render(request, 'signup.html')


def login(request):
    return render(request, 'login.html')


def login1(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['password']
        user = auth.authenticate(username=username, password=pass1)
        if user is not None:
            auth.login(request, user)
            return render(request, 'newhomepage.html')
        else:
            messages.info(request, 'Invalid credentials')
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')


def signup1(request):
    if request.method == "POST":
        username = request.POST['username']
        pass1 = request.POST['password']
        pass2 = request.POST['password1']
        if pass1 == pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'OOPS! user name is alrady exist')
                return render(request, 'signup.html')
            else:
                user = User.objects.create_user(username=username, password=pass1)
                user.save()
                messages.info(request, 'Account created successfully!!')
                return render(request, 'login.html')
        else:

            messages.info(request, 'password do not match')
            return render(request, 'signup.html')


def logout(request):
    auth.logout(request)
    return render(request, 'newhomepage.html')


def contact(request):
    return render(request, 'contactus.html')


def contactmail(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        comment = request.POST['comment']
        tosend = comment + '---------------- This is just the contact page'
        data = contactus(firstname=firstname, lastname=lastname, email=email, comment=comment)
        data.save()
        return HttpResponse('<h1><center>thankyou for feedback </center></h1>')
