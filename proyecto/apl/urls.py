from django.urls import path
from . import views

urlpatterns = [
    path('apl/', views.apl, name='apl'),
]