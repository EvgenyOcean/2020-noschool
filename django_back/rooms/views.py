from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.exceptions import AuthenticationFailed


# getting the list with all the rooms 
# for testing purposes currently, but 
# may come in handy later on
@api_view(['GET'])
@authentication_classes([])
@permission_classes([AllowAny])
def rooms_list(request):
    rooms = ['first', 'seconds', 'third']
    return Response({"rooms": rooms})