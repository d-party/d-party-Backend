from django.urls import path

from . import views

urlpatterns = [
    path("", views.IndexView.as_view()),
    path("usage", views.UsageView.as_view()),
    path("admin/chart", views.AdminChartsView.as_view()),
    path("anime-store/lobby/<uuid:room_id>", views.AnimeRoomLobby.as_view()),
]
