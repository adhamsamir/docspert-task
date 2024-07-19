from django.contrib import admin
from .models import Account
# Register your models here.
@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('account_id', 'account_name', 'account_balance')
    search_fields = ('account_name', 'id')