from django.shortcuts import render,render_to_response
from django.http import FileResponse
import os
# Create your views here.

from django.shortcuts import HttpResponse
# Create your views here.
def home(request):
    # return HttpResponse("hello")
    context={}
    return render_to_response('home.html',context)

from gcgl import models

def pj(request):
    if request.method=="POST":
        uname=request.POST.get("usr11", None)
        upwd=request.POST.get("pwd11",None)
        models.Pj.objects.create(pj=uname,pname=upwd)
        # userlist=models.User.objects.all()
        # print(userlist)
        print(uname,upwd)
    # return render(request,"user.html",{"data":userlist})
    return render(request,"user.html")


def file_down(request,fname):
    if request.method=="POST":
        wantf = request.POST.get(fname,None)
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        file=open(os.path.join(BASE_DIR, 'download/'+wantf+'.xlsx'),'rb')
        response =FileResponse(file)
        response['Content-Type']='application/octet-stream'
        response['Content-Disposition']='attachment;filename="{}"'.format(wantf+"xlsx")
    return response

def tools(request):
    context={}
    return render_to_response('tools.html', context)
    # return  render(request,'tools.html')

def gdview(request):
    context={}
    return render_to_response('gdview.html', context)
    # return  render(request,'tools.html')

