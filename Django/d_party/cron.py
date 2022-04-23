from web.views import AnimeRoom, AnimeUser


def my_scheduled_job():
    AnimeRoom.objects.all().delete(hard=True)
    AnimeRoom.objects.all().save()
