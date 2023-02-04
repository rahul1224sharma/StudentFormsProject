from django.shortcuts import render
from StudentDBApp import forms
# Create your views here.
def studentinputview(request):
    formsobj=forms.StudentForm()
    dict1={'form1':formsobj}
    return render(request,'StudentDBApp/input.html',context=dict1)

import time;
def studentverifyview(request):
    if request.method=='POST':
        formsobj=forms.StudentForm(request.POST)
        if formsobj.is_valid():
            print('form validated success')
            time.sleep(5)
            print('Nmae:',formsobj.cleaned_data['name'])
            print('Marks:',formsobj.cleaned_data['marks'])
            formsobj=forms.StudentForm()
            dict1={'form1':formsobj,'msg':'data successfully...enter another data'}
    return render(request,'StudentDBApp/input2.html',context=dict1)


from django.shortcuts import render
from StudentDBApp.forms import StudentForm
import time

def student(request):
    sentdata=False;
    if request.method=='POST':
        formsobj=StudentForm(request.POST)
        if formsobj.is_valid():
            print('forms request data validation')
            time.sleep(3)
            print('Name:',formsobj.cleaned_data['name'])
            print('marks:',formsobj.cleaned_data['marks'])
            sentdata=True;
            formsobj=StudentForm()
            dict1={'form1':formsobj,'sentdata':sentdata}
            return render(request,'StudentDBApp/thankyou.html',context=dict1)
    formsobj=StudentForm()
    dict1={'form1':formsobj}
    return render(request,'StudentDBApp/input3.html',context=dict1)

from StudentDBApp.forms import StudentloginForm
def login(request):
    formsobj=StudentloginForm()
    dict1={'form1':formsobj}
    return render(request,'StudentDBApp/login.html',context=dict1)

def loginverify(request):
    sentdata=False;
    if request.method=='POST':
        formsobj=StudentloginForm(request.POST)
        if formsobj.is_valid():
            print('login form')
            username=formsobj.cleaned_data['username']
            password=formsobj.cleaned_data['password']
            if username=='Raja' and password==1234:
                sentdata=True;
                username=formsobj.cleaned_data['username'];
                dict1={'sentdata':sentdata,'username':username}
                print('logged in')
                return render(request,'StudentDBApp/loginsuccess.html',context=dict1)
            else:
                return render(request,'StudentDBApp/loginunsuccess.html')
    else:
        return render(request,'StudentDBApp/loginunsuccess.html')
def feedback(request):
    sentdata=False;
    formsobj=forms.feedbackForm()
    if request.method=='POST':
        formsobj=forms.feedbackForm(request.POST);
        if formsobj.is_valid():
            print('name:',formsobj.cleaned_data['name'])
            formsobj=forms.feedbackForm()
            sentdata=True;
    return render(request,'StudentDBApp/feedback.html',{'form':formsobj,'sentdata':sentdata})