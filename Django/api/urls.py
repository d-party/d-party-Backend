from django.urls import path

from . import views

urlpatterns = [
    path(
        "v1/chrome-extension/version-check",
        views.ChromeExtensionVersionCheckAPI.as_view(),
    ),
    path(
        "v1/statistics/anime-store/active-user-per-day",
        views.AnimeActiveUserPerDayAPI.as_view(),
    ),
    path(
        "v1/statistics/anime-store/active-room-per-day",
        views.AnimeActiveRoomPerDayAPI.as_view(),
    ),
    path(
        "v1/statistics/anime-store/anime-reaction-count",
        views.AnimeRoomReactionCountAPI.as_view(),
    ),
    path(
        "v1/statistics/anime-store/anime-reaction-all-count",
        views.AnimeRoomReactionAllCountAPI.as_view(),
    ),
    path(
        "v1/statistics/anime-store/anime-room-all-count",
        views.AnimeRoomAllCountAPI.as_view(),
    ),
    path(
        "v1/statistics/anime-store/anime-user-all-count",
        views.AnimeUserAllCountAPI.as_view(),
    ),
    path(
        "v1/statistics/anime-store/anime-room-alive-count",
        views.AnimeRoomAliveCountAPI.as_view(),
    ),
    path(
        "v1/statistics/anime-store/anime-user-alive-count",
        views.AnimeUserAliveCountAPI.as_view(),
    ),
    path("shields/total-room", views.RoomCountShieldsAPI.as_view()),
    path("shields/total-user", views.UserCountShieldsAPI.as_view()),
    path("shields/total-reaction", views.ReactionCountShieldsAPI.as_view()),
]
