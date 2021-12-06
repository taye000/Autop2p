from django.urls import path
from . import views

# urlconf
urlpatterns = [
    path('signup/', views.sign_up)
]
