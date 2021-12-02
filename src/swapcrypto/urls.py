from django.urls import path
from . import views

# urlconf
urlpatterns = [
    path('signin/', views.sign_in)
]
