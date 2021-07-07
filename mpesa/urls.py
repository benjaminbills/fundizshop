from django.urls import path
from .views import LNMCallbackUrlAPIView
from .models import LNMOnline
from .lipanampesa import lipa_na_mpesa


urlpatterns = [
    path('', LNMCallbackUrlAPIView.as_view(), name='lnm-callbackurl'),
    path('lipa/', lipa_na_mpesa, name="lipanampesa")
]
