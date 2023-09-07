from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import CustomTokenObtainPairView, HelloWorldView, PersonListView

urlpatterns = [
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Token refresh view
    path('hello/', HelloWorldView.as_view(), name='hello_world'),
    path('persons/', PersonListView.as_view(), name='person-list'),
]