from django.urls import path, include, re_path
from banka.views import notfound
from .views.auth import signup


urlpatterns = [
    path('auth/signup/', signup.SignUp.as_view(), name="signup"),
  # match route that has not been registered above
    re_path(r'^(?:.*)$', notfound)
]
