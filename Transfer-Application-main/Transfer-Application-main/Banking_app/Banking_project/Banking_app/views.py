from django.shortcuts import render,redirect,HttpResponse
from .models import *
from .forms import *

# Create your views here.
def home(request):
    ac = Accounts.objects.all()
    return render(request, 'home.html', {'ac':ac})

def add_account(request):
    if request.method == 'POST':
        form = Account_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_ac')
    else:
        form = Account_form()
    return render(request, 'add_acc.html', {'add_form':form})


def edit_account(request,id):
    edit = Accounts.objects.get(id=id)
    if request.method == 'POST':
        form = Account_form(request.POST, instance=edit)
        if form.is_valid():
            form.save()
            return redirect('view_ac')
    else:
        form = Account_form(instance=edit)
    return render(request, 'edit.html', {'form':form})

def delete_account(request,id):
    edit = Accounts.objects.get(id=id)
    edit.delete()
    return redirect('view_ac')

def View_account(request):
    ac = Accounts.objects.all()
    return render(request, 'view_acc.html', {'ac':ac})
    


def transfer(request):
    if request.method == 'POST':
        form = Transfer_form(request.POST)
        print ("the answer is :",form)
        if form.is_valid():
                trans = form.save()
            # if form!=trans.sender.name:
            #     print()
        
            
        
            # else:
            #     return HttpResponse("account mismatch")

                if  trans.amount<=trans.sender.ac_balance:
                    trans.sender.ac_balance -= trans.amount
                    trans.receiver.ac_balance += trans.amount
                    trans.sender.save()
                    trans.receiver.save()
                    return redirect('home')
                else:
                    return HttpResponse('Insufficent Balance')
    else:
        form = Transfer_form()
    return render(request, 'transfer.html', {'form':form})
        
def view_transfer(request):
    transfers = Transfer.objects.all()
    return render(request, 'transfer_status.html', {'tf': transfers})