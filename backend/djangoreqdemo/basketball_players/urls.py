import django.urls

import basketball_players.views


urlpatterns = [
    django.urls.path('create/', basketball_players.views.BasketballPlayersCreateAPIView.as_view(), name='create'),
    django.urls.path('all/', basketball_players.views.BasketballPlayersListAPIView.as_view(), name='list'),
    django.urls.path('<int:pk>/', basketball_players.views.BasketballPlayersDetailUpdateDeleteAPIView.as_view(), name='concrete'),
]
