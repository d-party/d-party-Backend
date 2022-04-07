from django.urls import path

from . import views

urlpatterns = [
    path(
        "v1/chrome-extension/version-check",
        views.ChromeExtensionVersionCheckAPI.as_view(),
    ),
]
