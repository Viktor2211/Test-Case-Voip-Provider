from api.cdr.cdrs import CdrAPI, CdrDetailAPI
from django.urls import include, path

urlpatterns = [
    path('', CdrAPI.as_view()),
    path('<int:pk>/', CdrDetailAPI.as_view())
]
