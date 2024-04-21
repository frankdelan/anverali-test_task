from django.urls import path
from .views import register, login, logout

app_name = 'users'

urlpatterns = [
    path('register/', register, name='register_page'),
    path('login/', login, name='login_page'),
    path('logout/', logout, name='logout_page')
]