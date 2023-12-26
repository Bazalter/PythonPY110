from django.urls import path
from .views import login_view, logout_view

app_name = 'login'

urlpatterns = [
    path('', login_view, name="login_view"),
    path('', logout_view, name="logout_view")
]