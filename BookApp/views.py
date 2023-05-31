from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from BookApp.models import categorydb,productdb
from django.utils.datastructures import MultiValueDictKeyError
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
import datetime

# Create your views here.
def index(request):
    return render(request,"index.html")

def logintest(request):
    return render(request,"login.html")

def adminlogin(request):
    if request.method=="POST":
        username_r=request.POST.get('username')
        password_r=request.POST.get('password')
        if User.objects.filter(username__contains=username_r).exists():
            user=authenticate(username=username_r,password=password_r)
            if user is not None:
                login(request,user)
                request.session['username'] = username_r
                request.session['password'] = password_r
                return redirect(index)
            else:
                return redirect(logintest)
        else:
            return redirect(logintest)

def adminlogout(request):
    del request.session['username']
    del request.session['password']
    return redirect(logintest)

def categoryfn(request):
    return render(request,"Add_Category.html")

def savedata(request):
    if request.method=="POST":
        na=request.POST.get('name')
        de=request.POST.get('description')
        im=request.FILES['image']
        obj=categorydb(Name=na,Description=de,Image=im)
        obj.save()
        return redirect(categoryfn)

def displaydata(request):
    data=categorydb.objects.all()
    return render(request,"Display_category.html",{"data":data})

def  editcategory(req,dataid):
    data=categorydb.objects.get(id=dataid)
    return render(req,"edit_category.html",{"data":data})

def updatecategory(req,dataid):
    if req.method == "POST":
        na = req.POST.get('name')
        de = req.POST.get('description')
        try:
            img=req.FILES['image']
            fs=FileSystemStorage()
            file=fs.save(img.name,img)
        except MultiValueDictKeyError:
            file=categorydb.objects.get(id=dataid).Image
        categorydb.objects.filter(id=dataid).update(Name=na,Description=de,Image=file)
        return redirect(displaydata)

def deletecategory(req,dataid):
    data=categorydb.objects.filter(id=dataid)
    data.delete()
    return redirect(displaydata)

def productfn(request):
    data=categorydb.objects.all()
    return render(request,"Add_product.html",{"data":data})


def saveproduct(request):
    if request.method=="POST":
        cn=request.POST.get('C_name')
        pn=request.POST.get('P_name')
        de=request.POST.get('description')
        pr = request.POST.get('price')
        qu = request.POST.get('quantity')
        im=request.FILES['image']
        obj=productdb(Category_name=cn,Product_name=pn,P_description=de,Price=pr,Quantity=qu,Image=im)
        obj.save()
        return redirect(productfn)


def displayproduct(request):
    data=productdb.objects.all()
    return render(request,"Display_Product.html",{"data":data})
#
def  editproduct(req,dataid):
    data=productdb.objects.get(id=dataid)
    da = categorydb.objects.all()
    return render(req,"edit_product.html",{"data":data,'da':da})

def updateproduct(request,dataid):
    if request.method == "POST":
        cn = request.POST.get('category')
        pn = request.POST.get('name')
        de = request.POST.get('description')
        pr = request.POST.get('price')
        qu = request.POST.get('quantity')
        try:
            im=request.FILES['image']
            fs=FileSystemStorage()
            file=fs.save(im.name,im)
        except MultiValueDictKeyError:
            file=productdb.objects.get(id=dataid).Image
        productdb.objects.filter(id=dataid).update(Category_name=cn,Product_name=pn,P_description=de,Price=pr,Quantity=qu,Image=file)
        return redirect(displayproduct)

def deleteproduct(request,dataid):
    data=productdb.objects.filter(id=dataid)
    data.delete()
    return redirect(displayproduct)

def logintest(request):
    return render(request,"login_admin.html")

def adminlogin(request):
    if request.method=="POST":
        username_r=request.POST.get('username')
        password_r=request.POST.get('password')
        if User.objects.filter(username__contains=username_r).exists():
            user=authenticate(username=username_r,password=password_r)
            if user is not None:
                login(request,user)
                request.session['username'] = username_r
                request.session['password'] = password_r
                return redirect(index)
            else:
                return redirect(logintest)
        else:
            return redirect(logintest)

def adminlogout(request):
    del request.session['username']
    del request.session['password']
    return redirect(logintest)