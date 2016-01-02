from django.contrib.auth.models import User
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate

def errorpage(request):
    return render(request, 'errorpage.html')

def loginpage(request):
    return render(request, 'login.html')
def usersignup(request):
    if request.method == 'POST':
        
        request_context = RequestContext(request)
        username = request.POST['username']
        password = request.POST['password']
        repassword = request.POST['repassword']
        email=request.POST['email']
      
        user=User.objects.create_user(username, email, password)

        return loginpage(request)
        


def validateuser(request):
    if request.method == 'POST':
       request_context = RequestContext(request)
       logusername = request.POST.get('username',False)
       logpassword = request.POST.get('password',False)
       user = authenticate(username=logusername,password=logpassword)
    if user is not None:
    # the password verified for the user
       if user.is_active:
           errordet=errorpage(request)
           return errordet
       else:
           errordet=errorpage(request)
           return errordet
    else:
    # the authentication system was unable to verify the username and password
        errordet=errorpage(request)
        return errordet
