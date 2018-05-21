from django.urls import path

from games import views

urlpatterns = [
    path('games/', views.GameList.as_view(), name=views.GameList.name),
    path('games/<int:pk>/', views.GameDetail.as_view(), name=views.GameDetail.name),
    path('game-categories/', views.GameCategoyViewSet.as_view({'get': 'list'}), name=views.GameCategoryList.name),
    path('game-categories/<int:pk>/', views.GameCategoyViewSet.as_view({'get': 'retrieve'}), name=views.GameCategoryDetail.name),
    path('players/', views.PlayerList.as_view(), name=views.PlayerList.name),
    path('players/<int:pk>/', views.PlayerDetail.as_view(), name=views.PlayerDetail.name),
    path('scores/', views.ScoreList.as_view(), name=views.ScoreList.name),
    path('scores/<int:pk>/', views.ScoreDetail.as_view(), name=views.ScoreDetail.name),
    path('', views.ApiRoot.as_view(), name=views.ApiRoot.name),
]
