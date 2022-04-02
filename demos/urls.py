from wsgiref.util import application_uri
from django.urls import path
from .views import calculator, lotto, lotto_result

app_name = "demos"

urlpatterns = [
    path("calculator/", calculator, name="calculator"),
    path("lotto/", lotto, name="lotto"),
    path("lotto/result/", lotto_result, name="lotto_result"),
]
