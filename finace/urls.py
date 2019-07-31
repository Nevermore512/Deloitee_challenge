from django.urls import path
from . import views


urlpatterns = [
    path('finance/', views.input, name='input'),
    path('finance/result/', views.output, name='output'),
    path('finance/result/report', views.file_download, name='file_download'),
]