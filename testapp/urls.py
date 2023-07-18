from django.urls import path
from testapp import views

urlpatterns = [
    path('addTask/', views.addTask ,name='addTask'),
    

]