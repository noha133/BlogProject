from django.urls import path
from .views import CustomRegisterView

from django.urls import path, include
from dj_rest_auth.views import (
    LoginView
)

urlpatterns = [
    path('login/', LoginView.as_view(), name="rest_login"),
    path('register/', CustomRegisterView.as_view(), name='rest_register'),

]