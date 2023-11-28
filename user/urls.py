from django.urls import path
from .views import CustomRegisterView, CustomLoginView

from django.urls import path, include




urlpatterns = [
    path('login/', CustomLoginView.as_view(), name="rest_login"),
    path('register/', CustomRegisterView.as_view(), name='rest_register'),

]