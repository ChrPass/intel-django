# from django.conf.urls import url
from django.urls import path, include
from .views import (
    TermsListApiView,
)

urlpatterns = [
    path('api', TermsListApiView.as_view()),
]