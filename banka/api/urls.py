from django.urls import path, include, re_path
from banka.views import notfound
from .views.auth import (
  signup, 
  signin
)


urlpatterns = [
    path('auth/signup/', signup.SignUp.as_view(), name="signup"),
    path('auth/signin/', signin.SignIn.as_view(), name="signin"),
  # match route that has not been registered above
    re_path(r'^(?:.*)$', notfound)
]
