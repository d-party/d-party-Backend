"""ルーム人数の導出（``AnimeRoom.objects.with_people_counts()`` ほか）のテスト。

人数は ``AnimeRoom`` のカラムとしては保持せず、``AnimeUser`` から数える:

* ``num_people``: 論理削除されていない ``AnimeUser``（＝現在の在室者）
* ``sum_people``: 論理削除済みも含む全 ``AnimeUser``（＝累計参加者）

``AnimeUser`` は物理削除されないため、退室者も累計に残る。
"""

import pytest

from .factories import AnimeRoomFactory, AnimeUserFactory
from .models import AnimeRoom


def _counts(room):
    annotated = AnimeRoom.objects.with_people_counts().get(pk=room.pk)
    return annotated.num_people, annotated.sum_people


@pytest.mark.django_db
def test_empty_room_counts_zero():
    room = AnimeRoomFactory()

    assert _counts(room) == (0, 0)


@pytest.mark.django_db
def test_counts_host_and_guests():
    room = AnimeRoomFactory()
    AnimeUserFactory(room_id=room, is_host=True)
    AnimeUserFactory(room_id=room)
    AnimeUserFactory(room_id=room)

    assert _counts(room) == (3, 3)


@pytest.mark.django_db
def test_left_user_leaves_num_people_but_stays_in_sum_people():
    room = AnimeRoomFactory()
    AnimeUserFactory(room_id=room, is_host=True)
    leaver = AnimeUserFactory(room_id=room)

    leaver.delete()  # 論理削除（退室）

    assert _counts(room) == (1, 2)


@pytest.mark.django_db
def test_counts_are_scoped_per_room():
    room = AnimeRoomFactory()
    other = AnimeRoomFactory()
    AnimeUserFactory(room_id=room, is_host=True)
    AnimeUserFactory(room_id=other, is_host=True)
    AnimeUserFactory(room_id=other)

    assert _counts(room) == (1, 1)
    assert _counts(other) == (2, 2)


@pytest.mark.django_db
def test_properties_match_annotations():
    room = AnimeRoomFactory()
    AnimeUserFactory(room_id=room, is_host=True)
    leaver = AnimeUserFactory(room_id=room)
    leaver.delete()

    room.refresh_from_db()
    assert (room.alive_user_count, room.total_user_count) == _counts(room)


@pytest.mark.django_db
def test_with_people_counts_keeps_logical_deletion_helpers():
    """``alive()`` などのマネージャ機能が注釈後も使えることを確認する。"""
    alive_room = AnimeRoomFactory()
    dead_room = AnimeRoomFactory()
    AnimeUserFactory(room_id=alive_room, is_host=True)
    dead_room.delete()

    rooms = (
        AnimeRoom.objects.with_people_counts()
        .alive()
        .filter(pk__in=[alive_room.pk, dead_room.pk])
    )

    assert [(r.pk, r.num_people) for r in rooms] == [(alive_room.pk, 1)]
