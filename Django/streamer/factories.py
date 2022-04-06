import factory
import uuid
from .models import AnimeRoom, AnimeUser


class AnimeRoomFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = AnimeRoom

    room_id = uuid.uuid4()
    num_people = factory.fuzzy.FuzzyInteger(0, 10)
    sum_people = factory.fuzzy.FuzzyInteger(10, 20)
    part_id = uuid.uuid4()
    updated_at = factory.Faker("date")
    created_at = factory.Faker("date")


class AnimeUserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = AnimeUser

    user_id = uuid.uuid4()
    user_name = factory.Faker("name")
    room_id = factory.SubFactory(AnimeRoomFactory)
    is_host = False
    updated_at = factory.Faker("date")
    created_at = factory.Faker("date")
