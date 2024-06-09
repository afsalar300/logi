from django.shortcuts import render, redirect

from logic.models import receiverdb, contactdb, senderdb


# Create your views here.
def bindex(request):
    return render(request, 'bindex.html')

def status(request):
    data = receiverdb.objects.all()
    return render(request,'status.html',{'data': data})
def statusEdit(request,dataid):
    details = receiverdb.objects.get(id=dataid)
    return render(request, 'statusEdit.html', {'details': details})

def updatestatus(request,dataid):
    if request.method == 'POST':
        vv = request.POST.get('s_status')
        receiverdb.objects.filter(id=dataid).update(re_status=vv)
        return redirect(status)

def message(request):
    dat = contactdb.objects.all()
    return render(request, 'messageshow.html', {'dat': dat})

def sender(request):
    daa = senderdb.objects.all()
    return render(request, 'sender.html', {'daa': daa})

def recever(request):
    foo = receiverdb.objects.all()
    return render(request, 'receiver.html', {'foo': foo})