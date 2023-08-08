from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
#from django.shortcuts import render,redirect
#from devicetrack.models import CompanyEmployees
#from devicetrack.models import deviceGive
#from devicetrack.models import deviceReturn
#from django.contrib.admin.widgets import  AdminDateWidget, AdminTimeWidget, AdminSplitDateTime

from .models import UploadFile
from .forms import MyfileUploadForm


# Create your views here.

def homePage(request):
    #data={
    #    'title': 'Home Page New',
    #    'body_data': 'Homepage has started now'
    #}
    return render(request, "index.html")

@login_required(login_url='login')
def aboutUs(request):
    return render(request, "about.html")

@login_required(login_url='login')
def FileUpload(request):
    if request.method=='POST':
        name=request.user.username
        userid=request.user.id
        title1=request.POST.get('title')
        file2=request.FILES['file1']
        doctype1=request.POST.get('doctype')
        description1=request.POST.get('description')
        permissions1=request.POST.get('permission')

        #print 

        document = UploadFile.objects.create(name=name,user_id=userid,title=title1, file=file2, doctype=doctype1, description=description1,permissions=permissions1)
        document.save()


    return render(request, "fileupload.html")


@login_required(login_url='login')
def FileDownload(request):
    if request.user.username == 'user':
     values = UploadFile.objects.all()

    #st = request.GET.get('permissions')
    print(request.user)
    
    if request.user.username != 'user':
     values = UploadFile.objects.filter(permissions='Public').values() | UploadFile.objects.filter(permissions='Private', user_id=request.user.id).values()

        #ids = request.GET.get('user_id')

    if request.method=="GET":
        st=request.GET.get('search')
        if st!=None:
            values = UploadFile.objects.filter(title=st, permissions='Public') | UploadFile.objects.filter(title=st, permissions='Private', user_id=request.user.id)

    context = {
        'data': values,
        #'uid': request.user.id
    }

    return render(request, "downloadFiles.html", context)

@login_required(login_url='login')
def FileSearch(request):
    values = ''
    if request.method=="GET":
        st=request.GET.get('search')
        if st!=None:
            values = UploadFile.objects.filter(title=st, user_id=request.user.id) | UploadFile.objects.filter(description=st, user_id=request.user.id) | UploadFile.objects.filter(doctype=st, user_id=request.user.id) 
    context = {
        'data': values,
        #'uid': request.user.id
    }

    return render(request, "search.html", context)

def AccountRegister(request):
    n =  ''

    if request.method=='POST':
        name=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        
        if pass1!=pass2:
            return HttpResponse("Password and Confirm Password do not match")
        else:
            account_user=User.objects.create_user(name, email, pass1)
            account_user.save()
        #n='Data Inserted'
        return redirect('login')
    return render(request, "registration.html")


def Login(request):

    if request.method=='POST':
        name=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=name,password=pass1)
        
        if user is not None:
            login(request,user)
            return redirect('about') 
        else:
            return HttpResponse("Username or Password is incorrect")
        #en=deviceReturn(employeeName=name,deviceName=device,returnDate=returnDate,deviceCondition2=deviceSituation2)
        #en.save()
        #n='Data Inserted'

    return render(request, "login.html")

def Logout(request):
    logout(request)
    return redirect('login')