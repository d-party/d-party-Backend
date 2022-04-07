from django.contrib import admin
from .models import AnimeRoom, AnimeUser, TVRoom
from django_boost.admin import LogicalDeletionModelAdmin

# Register your models here.


@admin.register(AnimeRoom)
class AnimeRoomAdmin(LogicalDeletionModelAdmin):
    pass


@admin.register(AnimeUser)
class AnimeUserAdmin(LogicalDeletionModelAdmin):
    pass


@admin.register(TVRoom)
class TVRoomAdmin(LogicalDeletionModelAdmin):
    pass
