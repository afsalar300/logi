from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render,redirect
from django.utils.datastructures import MultiValueDictKeyError

from logic.models import logindb, receiverdb, senderdb, prodb, contactdb


# Create your views here.
def index(request):
    return render(request,'index.html')
def profilecreate(request):
    return render(request, 'profilecreate.html')

def profiledb(request):
    if request.method == 'POST':
        aa = request.POST.get('f_name')
        ab = request.POST.get('l_name')
        ac = request.POST.get('mob_number')
        ad = request.POST.get('address1')
        ae = request.POST.get('address2')
        af = request.POST.get('postcode')
        ag = request.POST.get('sta')
        ah = request.POST.get('are')
        ai = request.POST.get('count')
        # aj = request.POST.get('email_id')
        # ak = request.POST.get('pass')
        obj = prodb(first_name=aa, last_name=ab, mobile=ac, address_1=ad, address_2=ae, post_code=af, state=ag, area=ah,
                    country=ai)
        obj.save()
        request.session['f_name'] = aa
        request.session['l_name'] = ab
        request.session['mob_number'] = ac
        request.session['address1'] = ad
        request.session['address2'] = ae
        request.session['postcode'] = af
        request.session['sta'] = ag
        request.session['are'] = ah
        request.session['count'] = ai
        # request.session['email_id'] = aj
        # request.session['pass'] = ak
        return redirect(home)

def login(request):
    return render(request,'login.html')

def savelog(request):
    if request.method == 'POST':
        a = request.POST.get('name')
        b = request.POST.get('mail')
        c = request.POST.get('pass')
        obj = logindb(s_name=a, s_mail=b, s_pass=c)
        obj.save()
        return redirect(login)

def loginsave(request):
    if request.method == "POST":
        d = request.POST.get('email')
        e = request.POST.get('pas')
        if logindb.objects.filter(s_mail=d,s_pass=e).exists():
            request.session['email'] = d
            request.session['pas'] = e
            return redirect(detail)
        else:
            return redirect(login)
    else:
        return redirect(login)
def detail(request):
    return render(request,'detail.html')
def logout(request):
    del request.session['email']
    del request.session['pas']
    return redirect(login)

def home(request):
    return render(request,'home.html')
def senderdata(request):
    if request.method == 'POST':
        g = request.POST.get('name')
        i = request.POST.get('mobile')
        k = request.POST.get('Address')
        obj = senderdb(se_f_name=g,se_mobile=i,se_address=k)
        obj.save()
        return redirect(home2)

def home2(request):
    return render(request, 'home2.html')
def receiverdata(request):
    if request.method == 'POST':
        oo = request.POST.get('emailee')
        m = request.POST.get('rname')
        o = request.POST.get('rmobile')
        q = request.POST.get('rAddress')
        r = request.POST.get('date')
        w = request.POST.get('status')
        obj = receiverdb(re_f_name=m, re_mobile=o, re_address=q, re_date=r, re_status=w, email=oo)
        obj.save()
        messages.success(request, " Your order is saved and We will catch up you with in two hours")
        return redirect(orders)

def first(request):
    return render(request, 'first.html')


def about(request):
    return render(request,'about.html')

def service(request):
    return render(request,'service.html')

def orders(request):
    data = receiverdb.objects.filter(email=request.session['email'])
    return render(request,'orders.html',{'data': data})

# def edit(request,dataid):
#     details = senderdb.objects.get(id=dataid)
#     return render(request,'edit.html',{'details': details})
# def editupdate(request,dataid):
#     if request.method == 'POST':
#         w = request.POST.get('nname')
#         x = request.POST.get('mmobile')
#         y = request.POST.get('AAddress')
#         senderdb.objects.filter(id=dataid).update(se_f_name=w,se_mobile=x,se_address=y)
#         return redirect(edit2)
def delete(request,de):
    da = senderdb.objects.filter(id=de)
    dr = receiverdb.objects.filter(id=de)
    da.delete()
    dr.delete()
    return redirect(orders)
def edit2(request,dataid):
    details = receiverdb.objects.get(id=dataid)
    return render(request,'edit2.html',{'details': details})
def editupdate2(request, dataid):
    if request.method == 'POST':
        s = request.POST.get('namee')
        t = request.POST.get('mobilee')
        u = request.POST.get('Addresss')
        v = request.POST.get('datee')
        vv = request.POST.get('statuss')
        receiverdb.objects.filter(id=dataid).update(re_f_name=s,re_mobile=t,re_address=u, re_date=v, re_status=vv)
        return redirect(orders)

def contact(request):
    return render(request, 'contact.html')

def contactdata(request):
    if request.method == 'POST':
        aa = request.POST.get('nam')
        bb = request.POST.get('emai')
        cc = request.POST.get('subj')
        dd = request.POST.get('messag')
        obj = contactdb(name=aa, email=bb, subject=cc, message=dd)
        obj.save()
        return redirect(contact)




