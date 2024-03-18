from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from myapp.models import *
from django.contrib import messages

# Create your views here.


def one(request):
    return render(request,'index.html')


def two(request):
    return render(request,'website.css')



def three(request):
    return render(request,'BLOG.html')

def four(request):
    return render(request,'from.html')

def five(request):
    return render(request,'account.html')

def seven(request):
    data=iteams.objects.all()
    return render(request,'shop.html',{'value':data})

def eight(request):
    
    obj=cartadd.objects.all()
    return render(request,'cart.html',{'shop':obj})
    # return render(request,'cart.html')

def web(request):
    

    a=request.GET['First Name']
    b=request.GET['Last Name']
    c=request.GET['email']
    d=request.GET['cmt']


    obj=contact(fn=a,ln=b,ed=c,cm=d)
    obj.save()

    return render(request,'from.html')


def six(request):
    return render(request,'register.html')


def send(request):
    
    uname=request.POST['name']
    upassword=request.POST['pwd']
    umail=request.POST['mail']
    uaddress=request.POST['add']
    uphone=request.POST['pho']


    obj=register(sname=uname,rpwd= upassword,remail=umail,radd=uaddress, rphone=uphone)
    obj.save()

    return render(request,"account.html")


def pro(request):

    csn=request.GET['nam']
    pws=request.GET['ppw']
     
    csn=str(csn) 

    if csn is '':
        messages.warning(request,'abe bharnaaa......')
        return render(request,'account.html')
    obj=register.objects.all()


    for i in obj:

        if (csn==i.sname or csn==i.remail)and pws==i.rpwd:
            messages.success(request, "AAP KA SAWAGAT HEY........ ")
            return render(request,'account.html')

    messages.error(request,"ham me maf kare aap ki jankari nahi hey.....")
    return render(request,'account.html')
    

def addcart(request):
    iid=request.POST['nm']
    iname=request.POST['nm1']
    iprice=request.POST['nm2']
    iimage=request.POST['nm3']

    cobj=cartadd(iname=iname,iprice=iprice,image=iimage)
    cobj.save()

    obj=cartadd.objects.all()
    return render(request,'cart.html',{'shop':obj})


def delete(request):
    value=request.GET['value']
    obj=cartadd.objects.all().filter(id=value)
    obj.delete()
    
    output=cartadd.objects.all()
    return render(request,'cart.html',{'shop':output})


def ten(request):
    return render(request,'forgot.html')



def update(request):
    value=request.GET['pid']
    pqty=request.GET['qty']
    pqty=int(pqty)
    pqty=pqty+1
    data=cartadd.objects.get(id=value)
    data.pquantity=pqty
    data.ptotalprice=int(data.ptotalprice)+50
    data.save()


    obj = cartadd.objects.all()
    return HttpResponseRedirect('/cart',{'shop':obj})

def uptodata(request):
    value=request.GET['pid']
    pqty=request.GET['qty']
    data=cartadd.objects.get(id=value)
    data.pquantity=int(data.pquantity)-1
    data.ptotalprice=int(data.ptotalprice)-50
    data.save()

    obj=cartadd.objects.all()
    return HttpResponseRedirect('/cart',{'shop':obj})


def forgotpw(request):
    return render(request,'forgot.html')


def forgot(request):
    forgotn=request.POST['en']
    forgotp=request.POST['ep']
    forgotcp=request.POST['cp']


    if forgotp==forgotcp:
        obj = register.objects.get(sname=forgotn)
        obj.rpwd=forgotp
        obj.save()

    return render(request,'account.html')



