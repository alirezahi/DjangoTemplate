from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.urls import reverse

# Create your views here.

@csrf_exempt
def hello_world(request, django):
    # import pdb;pdb.set_trace()
    return 'adsiufadiuf'
    if request.method == 'GET':
        param = request.GET
        username = param.get('username','')
        if username != '':
            return JsonResponse({'status':'is valid'})
        return JsonResponse("You're not cool")
    if request.method == 'POST':
        param = request.POST
        username = param.get('username','')
        password = param.get('password','')
        sth = username + ' ' + password
        return JsonResponse(sth)
    
    
def render_html(request):
    my_url = reverse('render_test')
    return render(request=request, template_name='index.html',context={'You_Know':{'a':'آ','b':'ب','c':3}, 'link':my_url, 'new_iteration':[{'name':'john','family_name':'wick'},{'name':'woody','family_name':'allen'}]})


def render_html_trying(request):
    return render(request=request, template_name='base.html', context={'show':2, 'Emperor':'&lt;'})

def render_html_trying_main(request):
    return render(request=request, template_name='main_page.html')