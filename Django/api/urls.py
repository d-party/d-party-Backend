from django.urls import path

from . import views

urlpatterns = [
    path(
        "v1/chrome-extension/version-check",
        views.ChromeExtensionVersionCheckAPI.as_view(),
    ),
    path(
        "v1/statistics/active-user-per-day",
        views.ActiveUserPerDayAPI.as_view(),
    ),
    path(
        "v1/statistics/active-room-per-day",
        views.ActiveRoomPerDayAPI.as_view(),
    ),
    path(
        "v1/statistics/anime-reaction-count",
        views.AnimeRoomReactionCountAPI.as_view(),
    ),
]
