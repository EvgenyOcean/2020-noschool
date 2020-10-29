from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import UserRegisterSerializer, UserSerializer
from django.contrib.auth.models import User


# getting the users list (just in case)
# again, for testing purposes,
# but later on may become useful
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def users_list(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response({"users": serializer.data})


# registration
class UserCreate(APIView):
    """ 
    Creates the user. 
    """
    authentication_classes = []
    permission_classes = [AllowAny]

    def post(self, request, format='json'):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = {"message": f"{user.username} was successfully created!"}
                return Response(json, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)