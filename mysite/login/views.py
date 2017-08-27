# Create your views here.
from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django.contrib import auth
from django.contrib.auth.decorators import login_required
import importlib

#登陆
def login(request):
    user = request.user
    redirect_uri = "index"
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user) 
            return HttpResponseRedirect(redirect_uri)
        else:
            passwd_err = "用户名或密码错误！"
            return render_to_response('login.html',locals())
    return render_to_response('login.html')

#登陆成功
@login_required
def index(request):
    username = request.user
    return render_to_response('index.html' ,{'username':username})

#退出
def logout(request):
    return HttpResponseRedirect('/login/')
