import django.urls
import team.views


urlpatterns = [
    django.urls.path('create/', team.views.TeamCreateAPIView.as_view(), name='create'),
    django.urls.path('all/', team.views.TeamListAPIView.as_view(), name='list'),
    django.urls.path('<int:pk>/', team.views.TeamDetailUpdateDeleteAPIView.as_view(), name='concrete'),
]
