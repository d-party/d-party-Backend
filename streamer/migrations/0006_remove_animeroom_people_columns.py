"""Drop the denormalised people counters from ``AnimeRoom``.

``num_people`` / ``sum_people`` were incremented and decremented on every
join / leave, but ``AnimeUser`` is already the single source of truth for who
is in a room: the counters were only a cache, they were read in exactly one
place (the admin list), and they drifted from reality (whole-row ``save()``
write-backs from a stale per-connection cache, non-atomic read-modify-write on
join, and ``close_active_sessions`` reaping ghost users without decrementing).

Both values are now derived from ``AnimeUser`` via
``AnimeRoom.objects.with_people_counts()``:

* ``num_people``  = alive ``AnimeUser`` rows of the room
* ``sum_people``  = all ``AnimeUser`` rows of the room (they are never hard
  deleted, so this is the cumulative number of participants)

Dropping the columns is destructive but loses nothing: the derived values are
at least as accurate as the stored ones. Reversing the migration re-creates the
columns with their defaults (they are not, and cannot be, back-filled here).
"""

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("streamer", "0005_setting"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="animeroom",
            name="num_people",
        ),
        migrations.RemoveField(
            model_name="animeroom",
            name="sum_people",
        ),
    ]
