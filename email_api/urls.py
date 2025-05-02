from django.urls import path
from .views import SendEmailView

urlpatterns = [
    path('send-selection-email/', SendEmailView.as_view()),
]
