from operator import itemgetter
from django.shortcuts import render,redirect
from . models import Item
from django.contrib import messages
from django.views.generic import ListView


def index(request):
    item = Item.objects.all()
    return render(request,'home.html',{'item':item})


def create(request): 
    crud = Item.objects.all()
    if request.method == "POST":
        SlNo = request.POST.get('SlNo','')
        item = request.POST.get('item','')
        description = request.POST.get('description','')
        crud1 = Item( SlNo=SlNo, item=item, description=description )
        crud1.save()
        messages.success(request,"Data added Succesfully")
    # return render(request,'home.html',{'curd':crud})
    return redirect('/')


def delete(request,id):
    crud1 = Item.objects.get(id=id)
    crud1.delete()
    return redirect('/')



def updateRecord(request,id):
    crud: Item.objects.get(id=id)
    if request.method == 'POST':
        crud.SlNo = request.POST["SlNo",'']
        crud.item = request.POST.get('item','')
        crud.description = request.POST.get('description','')
        crud1 = Item( SlNo=SlNo, item=item, description=description )
        crud1.save()
        return redirect('/')
    # return render(request,'home.html',{'crud':crud})

def update(request,id):
    item = Item.objects.get(id=id)
    return render(request,'update.html',{'item':item})
        
       