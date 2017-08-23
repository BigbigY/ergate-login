# Create your views here.
from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django.contrib import auth
import importlib

#登陆
def login(request):
    user = request.user
    #redirect_uri = request.GET.get('next')
    redirect_uri = "index"
    if request.method == 'POST':
        global username
        username = request.POST.get('username')
        password = request.POST.get('password')
        code = request.POST.get('code')
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user) 
            return HttpResponseRedirect(redirect_uri)
        else:
            passwd_err = "用户名或密码错误！"
            return render_to_response('login.html',locals())
    return render_to_response('login.html')

#登陆成功
def index(request):
    return render_to_response('index.html' ,{'username':username})

#退出
def logout(request):
    #清理cookie里保存username
    response.delete_cookie('username')
    return HttpResponseRedirect('login')
