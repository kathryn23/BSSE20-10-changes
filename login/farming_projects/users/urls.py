# users/urls.py

from django.conf.urls import url, include
from users.views import homepage, register

urlpatterns = [
    url(r"^homepage/", homepage, name="homepage"),
    url(r"^register/", register, name="register"),
    url(r"^accounts/", include("django.contrib.auth.urls")),
]