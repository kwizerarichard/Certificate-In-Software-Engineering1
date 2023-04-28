from django.urls import path
from kyc import views

urlpatterns = [
    path('', views.index, name='index'),
    path('indexx', views.indexx, name='indexx')
]