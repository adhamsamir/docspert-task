from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('import/', views.import_accounts, name='import'),
    path('', views.list_accounts, name='list'),
    path('transfer/', views.transfer_funds, name='transfer'),
    path('detail/', views.account_detail, name='detail'),
    path('search/', views.account_search, name='search'),
]
