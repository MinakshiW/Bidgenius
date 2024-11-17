from rest_framework import viewsets
from .serializers import AuctionDetailsSerializer
from .models import AuctionDetails
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


class AuctionDetailsAPI(viewsets.ModelViewSet):
    serializer_class = AuctionDetailsSerializer
    queryset = AuctionDetails.objects.all()
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]