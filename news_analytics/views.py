from django.shortcuts import render
import json
from django.http import HttpResponse
import search_call as sc
from  django.contrib.auth.models import User


def signuppage(request):
    return render(request, 'signup.html')
# Create your views here.
def landing_page(request):
    return render(request, 'landingPage.html')

# api call to alchemy to get content
def get_content(request):
    print "here"
    res = ''
    if request.method == 'POST':
        params = request.POST
        val = params.get('search_keyword')
        print val
        res = sc.getData(val)
        
        print "outside"
    # return HttpResponse(json.dumps({'data': res}), content_type="application/json")
    return render(request, 'landingPage.html', {'data': res})
