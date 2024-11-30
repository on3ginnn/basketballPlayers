from rest_framework import serializers

import basketball_players.models


class BasketballPlayersCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = basketball_players.models.BasketballPlayers
        fields = ['name', 'age', "team"]


class BasketballPlayersSerializer(serializers.ModelSerializer):
    class Meta:
        model = basketball_players.models.BasketballPlayers
        fields = ['id', 'name', 'age', "team"]