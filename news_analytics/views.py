from django.shortcuts import render

import museapi as mus

# Create your views here.
def landing_page(request):
    return render(request, 'landingPage.html')
def signuppage(request):
    return render(request, 'signup.html')

# api call to alchemy to get content
def get_content(request):
    print ("here")
    res = ''
    if request.method == 'POST':
        params = request.POST
        val = params.get('search_keyword')
        print (val)
        res = mus.getDetails(val)
        print (res)
        print ("outside")
    # return HttpResponse(json.dumps({'data': res}), content_type="application/json")
    return render(request, 'landingPage.html', {'data': res})
