from django.db import models
import uuid
from django_boost.models.mixins import LogicalDeletionMixin
from django_cryptography.fields import encrypt


class AnimeRoom(LogicalDeletionMixin):
    room_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    num_people = models.PositiveSmallIntegerField(default=1)
    sum_people = models.PositiveSmallIntegerField(default=1)
    part_id = models.CharField(max_length=16)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class AnimeUser(LogicalDeletionMixin):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_name = encrypt(models.CharField(default="user", max_length=20))
    room_id = models.ForeignKey(
        AnimeRoom, on_delete=models.CASCADE, related_name="inroom"
    )
    is_host = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user_name


class ReactionType(models.TextChoices):
    cry = "C", "cry"
    middle_finger = "MF", "middle_finger"
    smile = "S", "smile"
    thumbs_up = "TU", "thumbs_up"
    fav = "F", "favorite"


class AnimeReaction(LogicalDeletionMixin):
    reaction_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    room_id = models.ForeignKey(AnimeRoom, on_delete=models.CASCADE)
    reaction_type = models.CharField(max_length=3, choices=ReactionType.choices)
    created_at = models.DateTimeField(auto_now_add=True)


class AnimeRoomHistory(models.Model):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    room_id = models.ForeignKey(AnimeRoom, on_delete=models.CASCADE)
    type = models.CharField(max_length=20)
