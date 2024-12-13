from django.urls import path,include
from .views import *

urlpatterns = [
    path('',home), 
    path('contact/', contact), 
    path('about/', aboutpage),
    path('welcome/', welcome) 
]
