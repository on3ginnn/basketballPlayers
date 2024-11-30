from rest_framework.views import APIView
import rest_framework.generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

import basketball_players.models
import basketball_players.serializer


class BasketballPlayersCreateAPIView(rest_framework.generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = basketball_players.models.BasketballPlayers.objects.all()
    serializer_class = basketball_players.serializer.BasketballPlayersCreateSerializer
"""
{
    "name": "Майкл Джордан",
    "age": "61",
    "team": "Чикаго Буллз"
}
"""

class BasketballPlayersListAPIView(rest_framework.generics.ListAPIView):
    queryset = basketball_players.models.BasketballPlayers.objects.all()
    serializer_class = basketball_players.serializer.BasketballPlayersSerializer


class BasketballPlayersDetailUpdateDeleteAPIView(rest_framework.generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = basketball_players.models.BasketballPlayers.objects.all()
    serializer_class = basketball_players.serializer.BasketballPlayersSerializer
{
    "title": "Кока Кола"
}