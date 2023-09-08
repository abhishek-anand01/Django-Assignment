from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication  # Import BasicAuthentication
from django.http import HttpResponse
from rest_framework import generics
from .models import Person
from .serializers import PersonSerializer
class CustomTokenObtainPairView(TokenObtainPairView):
    pass  # No additional modifications needed

class HelloWorldView(APIView):
    authentication_classes = [BasicAuthentication]  # Use Basic Authentication
    permission_classes = [IsAuthenticated]  # Require authentication for this view

    def get(self, request):
        message = "Hello World"
        return HttpResponse(message, content_type='text/plain')

class PersonListView(generics.ListAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
class PersonRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer