from django.shortcuts import render,redirect
import csv
from django.contrib import messages
from accounts.forms import ImportForm
from accounts.forms import TransferForm
from accounts.models import Account
from django.shortcuts import get_object_or_404
from django.db import transaction
# Create your views here.

def import_accounts(request):
    if request.method == 'POST':
        form = ImportForm(request.POST, request.FILES)
        
        if form.is_valid():
            csv_file = request.FILES['csv_file']
            reader = csv.DictReader(csv_file.read().decode('utf-8').splitlines())
            
            for row in reader:
                Account.objects.get_or_create(
                   account_id=row['ID'] ,
                   account_name=row['Name'],
                   account_balance = row['Balance']
                )
        messages.success(request,'Accounts imported successfully') 
        
    else:
        form = ImportForm()
        
    return render(request, 'accounts/import_accounts.html', {'form': form})



def list_accounts(request):
    accounts = Account.objects.all()
    return render(request, 'accounts/list_accounts.html', {'accounts': accounts})


def account_detail(request, account_id):
    account = get_object_or_404(Account, account_id=account_id)
    return render(request, 'accounts/account_detail.html', {'account': account})

def transfer_funds(request):
    if request.method == 'POST':
        form = TransferForm(request.POST)
        if form.is_valid():
            from_account = form.cleaned_data['from_account']
            to_account = form.cleaned_data['to_account']
            amount = form.cleaned_data['amount']

            if from_account.account_balance >= amount:
                with transaction.atomic():
                    from_account.account_balance -= amount
                    to_account.account_balance += amount
                    from_account.save()
                    to_account.save()
                messages.success(request, 'Funds transferred successfully!')
            else:
                messages.error(request, 'Insufficient funds in the source account.')
            
    else:
        form = TransferForm()
    return render(request, 'accounts/transfer_funds.html', {'form': form})

def landing_page(request):
    return render(request,'accounts/landing_page.html')

def account_search(request):
    account = None
    if 'account_id' in request.GET:
        account_id = request.GET['account_id']
        account = get_object_or_404(Account, account_id=account_id)
    return render(request, 'accounts/account_search.html', {'account': account})


