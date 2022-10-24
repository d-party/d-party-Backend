from django.contrib import admin
from .models import AnimeRoom, AnimeUser, AnimeReaction
from django_boost.admin import LogicalDeletionModelAdmin

# Register your models here.


@admin.register(AnimeRoom)
class AnimeRoomAdmin(LogicalDeletionModelAdmin):
    pass


@admin.register(AnimeUser)
class AnimeUserAdmin(LogicalDeletionModelAdmin):
    pass


@admin.register(AnimeReaction)
class AnimeReactionAdmin(LogicalDeletionModelAdmin):
    pass
