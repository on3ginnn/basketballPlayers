from rest_framework import serializers

import team.models


class TeamCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = team.models.Team
        fields = ['title', "country"]


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = team.models.Team
        fields = ['id', 'title', "country"]