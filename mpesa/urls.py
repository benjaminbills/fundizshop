from django.urls import path
from .views import LNMCallbackUrlAPIView
from .models import LNMOnline

urlpatterns = [
    path('', LNMCallbackUrlAPIView.as_view(), name='lnm-callbackurl')
]
