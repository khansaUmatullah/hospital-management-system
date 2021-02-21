from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name='index'),
    path('doctors',views.team,name='doctors'),
    path('patients',views.patientsdata,name='patients'),
    path('pharmacies',views.pharmacy_storage,name='pharmacies'),
    path('H_record',views.Records,name='H_record'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout')


]










