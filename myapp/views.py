import os
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .form import Users
from django.contrib import messages

def index(request):
    # Create a YouTubeDL object with the desired options
    email = request.session.get('email')
    return render(request,'index.html',{'email':email})
def navbar(request):
    email = request.session.get('email')
    print('navbar',email)
    if email:
        return render(request,'index.html',{'email':email})
    return render(request,'login.html')
def contact(request):
    return render(request,'contact.html',{'email':request.session.get('email')})
def signout(request):
    try:
        del request.session['email']
    except:
        pass
    return render(request,'index.html',{'email':request.session.get('email')})
def login(request):
    if request.POST:
        email = request.POST['email']
        password =request.POST['password']

        if Users.get_email(email)==False:
            messages.error(request,'Email not exist, check you email or create account')
            return render(request,'login.html',{'email':email,'password':password})
        else:
            flag = Users.get_pass(email,password)
            print(flag,password,email)
            if flag:
                messages.success(request,'login successfully !')
                request.session['email']=email
                return redirect(index)
            else:
                messages.error(request,'password didn\'t match')
                return render(request,'login.html',{'mail':email,'password':password})
        
    return render(request,'login.html')
def signup(request):
    if request.POST:
        fname = request.POST['fname']
        lname = request.POST['lname']
        phone = request.POST['number']
        email = request.POST['email']
        password = request.POST['password']
        
        if(Users.get_email(email=email)):
            messages.error(request,'email is already exist')
            return render(request,'signup.html',{'fname':fname,'lname':lname,'phone':phone,'email':email,'password':password})
        if len(password)<4:
            messages.error(request,'password must be atleast length four')
            return render(request,'signup.html',{'fname':fname,'lname':lname,'phone':phone,'email':email,'password':password})
        if phone.strip().isdigit()==False:
            messages.error(request,'phone number must be in digits not characters')
            return render(request,'signup.html',{'fname':fname,'lname':lname,'phone':phone,'email':email,'password':password})
        data = Users(fname=fname,lname=lname,phone=phone,email=email,password=password)
        data.save()
        request.session['email']=email
        data = Users.get_data(email)
        if data:
            request.session['fname']=data.fname
            request.session['lname']=data.lname
            request.session['phone']=data.phone
        
        messages.success(request,'Registered!')
        return render(request,'index.html')
    return render(request,'signup.html')
def about(request):
    return render(request,'about.html',{'email':request.session.get('email')})
def account(request):
    data = request.session.get('email')
    if data:
        data = Users.get_data(data)
        if(data):
            fname = data.fname        
            lname = data.lname
            phone = data.phone
            email = data.email        
    return render(request,'account.html',{'fname':fname,'lname':lname,'phone':phone,'email':email,})

#content
def quantumcom(request):
    return render(request,'quantumcom.html',{'email':request.session.get('email')})
def cloudcom(request):
    return render(request,'cloudcom.html',{'email':request.session.get('email')})
def chatgpt(request):
    return render(request,'chatgpt.html',{'email':request.session.get('email')})
def starlink(request):
    return render(request,'starlink.html',{'email':request.session.get('email')})
def ai(request):
    return render(request,'ai.html',{'email':request.session.get('email')})
def bard(request):
    return render(request,'bard.html',{'email':request.session.get('email')})
def augmented_r(request):
    return render(request,'augmented_r.html',{'email':request.session.get('email')})