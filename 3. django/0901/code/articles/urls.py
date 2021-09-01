from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('index/', views.index),
    path('', views.index), # ''는 기본주소를 의미
]