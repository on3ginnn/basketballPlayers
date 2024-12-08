from django.contrib.auth import authenticate
from users.serializer import UserSerializer
from rest_framework.views import APIView
import rest_framework.generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.shortcuts import get_object_or_404
from django.contrib.auth.hashers import make_password
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt import views as jwt_views
from django.contrib.auth import get_user_model

import team.models
import team.serializer


class TeamCreateAPIView(rest_framework.generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = team.models.Team.objects.all()
    serializer_class = team.serializer.TeamCreateSerializer


class TeamListAPIView(rest_framework.generics.ListAPIView):
    queryset = team.models.Team.objects.all()
    serializer_class = team.serializer.TeamSerializer


class TeamDetailUpdateDeleteAPIView(rest_framework.generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = team.models.Team.objects.all()
    serializer_class = team.serializer.TeamSerializer
    
