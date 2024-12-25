from django.urls import path
from .import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('Register/', views.Register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
]
