from django.urls import path
from .views import CustomRegisterView

from django.urls import path, include


urlpatterns = [
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('register/', CustomRegisterView.as_view(), name='rest_register'),

]