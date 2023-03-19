from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.pagination import PageNumberPagination
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import Image
from.serializers import ImageViewSerializer, ImageCreateSerializer, ImageDeleteSerializer

# Pagination Class. This can also be done globally by specifying in the views.py
class StandardPagination(PageNumberPagination):
    page_size = 16 # 4 x 4 page

# API View for displaying list of all the images uploaded by a user.
class ImageListView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ImageViewSerializer
    pagination_class = StandardPagination

    def get_queryset(self):
        user = self.request.user
        return Image.objects.filter(user=user).order_by('-created_on')
    
# API View for displaying details for a single image.
# Lookup field is the image id (p.k).
class ImageDetailView(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ImageViewSerializer

    def get_queryset(self):
        user = self.request.user
        return Image.objects.filter(user=user)

# API View for creating a new image
class ImageCreateView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ImageCreateSerializer
    queryset = Image.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# API View for deleting an image
class ImageDeleteView(generics.DestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ImageDeleteSerializer
    
    def get_queryset(self):
        user = self.request.user
        return Image.objects.filter(user=user)

# API View for user login
class LoginView(APIView):
    def post(self, request, format=None):
        username = request.data.get('username', None)
        password = request.data.get('password', None)
        if username and password:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                token, created = Token.objects.get_or_create(user=user)
                return Response({'token': token.key, 'username' : username})
            else:
                return Response({'error': 'Invalid Credentials'}, 
                                status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'Please provide username and password'}, 
                            status=status.HTTP_400_BAD_REQUEST)

# API View for user registration       
class RegisterView(APIView):
    def post(self, request, format=None):
        username = request.data.get('username', None)
        password = request.data.get('password', None)
        confirm_password = request.data.get('confirm_password', None)

        if username is None or password is None or confirm_password is None:
            return Response({'error': 'Please provide all the details'}, 
                            status=status.HTTP_400_BAD_REQUEST)
    
        if password!=confirm_password:
            return Response({'error': 'Passwords do not match'}, 
                            status=status.HTTP_400_BAD_REQUEST)
        
        if User.objects.filter(username=username).exists():
            return Response({'error': 'Username already exists'}, 
                            status=status.HTTP_400_BAD_REQUEST)
        
        user = User.objects.create_user(username=username, password=password)
        token, created = Token.objects.get_or_create(user=user)
        return Response({'message':'User created succesfully', 'token': token.key, 'username':username}, 
                        status=status.HTTP_201_CREATED)

# API View for user logout
class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        request.user.auth_token.delete()
        return Response({'message' : 'Token deleted successfully'}, status=status.HTTP_200_OK)