from django.urls import path
from .views import my_page_home , registrPage , loginPage , logoutUser , my_page_prof  

app_name = 'apphotil'
urlpatterns = [

    
    path('',my_page_home, name='home_page'),
    path('prof',my_page_prof, name='prof'),  
    path('registr/',registrPage, name='registr' ),
    path('login/' , loginPage, name= 'login'),
    path('logout/' , logoutUser, name= 'logout'),  
   
]