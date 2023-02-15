from django.urls import path
from . import views
from django.contrib.auth import views as authenticate_views

app_name = "muti_user"

urlpatterns = [
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/' , authenticate_views.LoginView.as_view(template_name = 'muti_user/login.html'), name='login'),
    path('logout/' , authenticate_views.LogoutView.as_view(template_name = 'muti_user/logout.html'), name='logout'),
    
    path('createpost/', views.createpost, name='createpost'),
    
]
