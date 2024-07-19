from django.test import TestCase
from django.urls import reverse
from .models import Account

# Create your tests here.
class AccountTests(TestCase):

    def setUp(self):
        Account.objects.create(account_id="12345", account_name="Ahmed Samir", account_balance=1000)
        Account.objects.create(account_id="67890", account_name="Adham Samir", account_balance=500)

    def test_list_accounts(self):
        response = self.client.get(reverse('accounts:list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Ahmed Samir")
        self.assertContains(response, "Adham Samir")


    def test_transfer_funds(self):
        from_account = Account.objects.get(account_id="12345")
        to_account = Account.objects.get(account_id="67890")
        response = self.client.post(reverse('accounts:transfer'), {
            'from_account': from_account.id,
            'to_account': to_account.id,
            'amount': 200
        })
        self.assertEqual(response.status_code, 200)
        from_account.refresh_from_db()
        to_account.refresh_from_db()
        self.assertEqual(from_account.account_balance, 800)
        self.assertEqual(to_account.account_balance, 700)
