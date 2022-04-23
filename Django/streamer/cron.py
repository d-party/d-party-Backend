import datetime
import os

from .models import AnimeRoom, AnimeUser, AnimeReaction


def animeroom_auto_logical_delete():
    """一定の日数以上生き残ってしまったAnimeRoomを論理削除します"""
    logical_divide_day: str = os.getenv("LOGICAL_DIVIDE_DAY", default="3")
    logical_divide_day_int: int = int(logical_divide_day)

    divide_datetime: datetime.datetime = datetime.datetime.now() - datetime.timedelta(
        days=logical_divide_day_int
    )
    animeroom_queryset = AnimeRoom.objects.alive().filter(
        updated_at__lte=divide_datetime
    )
    animeroom_queryset.delete()
    animeroom_queryset.save()


def animeroom_auto_hard_delete():
    """一定の日数以上生き残ってしまったAnimeRoomを削除します"""
    hard_divide_day: str = os.getenv("HARD_DIVIDE_DAY", default="365")
    hard_divide_day_int: int = int(hard_divide_day)

    divide_datetime: datetime.datetime = datetime.datetime.now() - datetime.timedelta(
        days=hard_divide_day_int
    )
    animeroom_queryset = AnimeRoom.objects.all().filter(updated_at__lte=divide_datetime)
    animeroom_queryset.delete(hard=True)
    animeroom_queryset.save()


def animeuser_auto_logical_delete():
    """一定の日数以上生き残ってしまったAnimeUserを論理削除します"""
    logical_divide_day: str = os.getenv("LOGICAL_DIVIDE_DAY", default="3")
    logical_divide_day_int: int = int(logical_divide_day)

    divide_datetime: datetime.datetime = datetime.datetime.now() - datetime.timedelta(
        days=logical_divide_day_int
    )
    animeroom_queryset = AnimeUser.objects.alive().filter(
        updated_at__lte=divide_datetime
    )
    animeroom_queryset.delete()
    animeroom_queryset.save()


def animeuser_auto_hard_delete():
    """一定の日数以上生き残ってしまったAnimeUserを削除します"""
    hard_divide_day: str = os.getenv("HARD_DIVIDE_DAY", default="365")
    hard_divide_day_int: int = int(hard_divide_day)

    divide_datetime: datetime.datetime = datetime.datetime.now() - datetime.timedelta(
        days=hard_divide_day_int
    )
    animeroom_queryset = AnimeUser.objects.all().filter(updated_at__lte=divide_datetime)
    animeroom_queryset.delete(hard=True)
    animeroom_queryset.save()


def animereaction_auto_hard_delete():
    """一定の日数以上生き残ってしまったAnimeReactionを削除します"""
    hard_divide_day: str = os.getenv("REACTION_HARD_DIVIDE_DAY", default="90")
    hard_divide_day_int: int = int(hard_divide_day)

    divide_datetime: datetime.datetime = datetime.datetime.now() - datetime.timedelta(
        days=hard_divide_day_int
    )
    animeroom_queryset = AnimeReaction.objects.all().filter(
        created_at__lte=divide_datetime
    )
    animeroom_queryset.delete(hard=True)
    animeroom_queryset.save()
