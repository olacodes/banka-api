from django.urls import path, include, re_path
from banka.views import notfound
from .views.auth import (
    signup,
    signin
)
from .views.accounts import account_view, account_detail_view
from .views.transactions import transaction_view

urlpatterns = [
    path('auth/signup/', signup.SignUp.as_view(), name="signup"),
    path('auth/signin/', signin.SignIn.as_view(), name="signin"),

    path('accounts/', account_view.AccountView.as_view(), name="accounts"),
    path('account/<int:account_number>/', account_detail_view.AccountDetail.as_view(),
         name="account_detail"),
    path('transactions/<int:account_number>/debit/', transaction_view.DebitTransaction.as_view(), name='debit_transaction'),
    path('transactions/<int:account_number>/credit/', transaction_view.CreditTransaction.as_view(), name='credit_transaction'),

    # match route that has not been registered above
    re_path(r'^(?:.*)$', notfound)
]
