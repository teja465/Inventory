from django.shortcuts import render
from stocks.models import *
from stocks.forms import *
from django.http import HttpResponseRedirect
# Create your views here.
def check(r):
    return render(r,'check.html')

def index_view(r):
    return render(r,'index.html')
def display_mobiles(r):
    #
    mobiles=mobile.objects.all()
    return render(r,'mobiles.html',{'mobiles':mobiles})
def  delete_mob(request,id):
    print('in delete_mob view')
    mob=mobile.objects.get(id=id)
    mob.delete()
    return HttpResponseRedirect('/')
def update_mob(request,id):
    form=mobile.objects.get(id=id)
    if request.method=='POST':
        #
        form=mobile_form(request.POST,instance=form)
        form.save()
        return HttpResponseRedirect('/')


    return render(request,'update_mob.html',{'form':form})
