from django.urls import path
from .views import show_profile, edit_profile

app_name = 'accounts'

urlpatterns = [
    path('profile/', show_profile, name='account_page'),
    path('profile/edit', edit_profile, name='edit_page')
]