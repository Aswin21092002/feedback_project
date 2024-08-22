from django.urls import path
from . import views

urlpatterns = [
    path('', views.feedback_view, name='feedback'),  # Set the default view for the feedback app
]
