from django.shortcuts import render,redirect
from BookApp.models import categorydb,productdb
from displayapp.models import regdb,cartdb
# Create your views here.

def homepage(request):
    data=categorydb.objects.all()
    return render(request,"homepage.html",{"data":data})

def productpage(request,catg):
    data_2=productdb.objects.filter(Category_name=catg)
    return render(request,"productpage.html",{'data_2':data_2})

def detailspage(req,dataid):
    data=productdb.objects.get(id=dataid)
    return render(req,"Details.html",{'data':data})

def displaycartdata(request):
    cartdata=cartdb.objects.filter(username=request.session['username1'])
    return render(request,"displaycart.html",{"cartdata": cartdata})

def savecart(request):
    if request.method=="POST":
        username=request.POST.get('username1')
        p=request.POST.get('Pname')
        r=request.POST.get('price')
        q=request.POST.get('quantity')
        t=request.POST.get('T_price')
        obj=cartdb(username=username,Pname=p,price=r,quantity=q,T_price=t)
        obj.save()
        return redirect(homepage)

def signin(request):
    return render(request,"signup.html")

def user_reg(request):
    if request.method=="POST":
        na=request.POST.get('name')
        em=request.POST.get('email')
        pa=request.POST.get('password1')
        pa2=request.POST.get('password2')
        obj=regdb(Name=na,Email=em,Password=pa,C_password=pa2)
        obj.save()
        return redirect(signin)

def userlogin(request):
    if request.method=="POST":
        username_r=request.POST.get('username')
        password_r=request.POST.get('password')
        if regdb.objects.filter(Name=username_r,Password=password_r).exists():

            request.session['username1'] = username_r
            request.session['password1'] = password_r

            return redirect(homepage)
        else:
            return redirect(signin)
    return redirect(signin)

def logout(request):
    del request.session['username1']
    del request.session['password1']
    return redirect(homepage)
