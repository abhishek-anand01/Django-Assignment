from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication  # Import BasicAuthentication
from django.http import HttpResponse
from rest_framework import generics
from .models import Person
from .serializers import PersonSerializer
from drf_spectacular.utils import extend_schema
class CustomTokenObtainPairView(TokenObtainPairView):
    pass  # No additional modifications needed

class HelloWorldView(APIView):
    """_summary_

   This view allows you to return Hello World message with basic authentication.

    """
    authentication_classes = [BasicAuthentication]  # Use Basic Authentication
    permission_classes = [IsAuthenticated]  # Require authentication for this view
    serializer_class = None
    @extend_schema(summary="Hello World API", description="This is a basic API view that returns 'Hello World'.")
    def get(self, request):
        message = "Hello World"
        return HttpResponse(message, content_type='text/plain')

class PersonListView(generics.ListAPIView):
    """
    List and create persons.

    This view allows you to list all persons and create new ones.

    """
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
class PersonRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    List and create persons.

    This view allows you to retrieve person by Id.

    """
    queryset = Person.objects.all()
    serializer_class = PersonSerializer