from django.urls import path
from .views import LNMCallbackUrlAPIView

urlpatterns = [
    path('', LNMCallbackUrlAPIView.as_view())
]
