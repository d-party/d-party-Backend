from operator import truediv
from django.test import TransactionTestCase, TestCase
from channels.testing import ChannelsLiveServerTestCase
from channels.testing import WebsocketCommunicator
from channels.db import database_sync_to_async
import pytest
from .factories import AnimeRoomFactory, AnimeUserFactory
from .models import AnimeRoom, AnimeUser
from d_party import asgi


@pytest.mark.asyncio
class TestAnimePartyConsumer(TestCase):
    def setUp(self):
        self.anime_room1 = AnimeRoomFactory(num_people=1)
        self.anime_room2 = AnimeRoomFactory()
        self.anime_user1 = AnimeUserFactory(room_id=self.anime_room1, is_host=True)
        self.anime_user2 = AnimeUserFactory(room_id=self.anime_room1, is_host=False)

    @pytest.mark.django_db
    @pytest.mark.asyncio
    @pytest.mark.with_async
    async def test_anime_party_consumer_create_ok(self):
        """AnimeConsumerのcreate actionが正しく動作することを確認するテスト"""
        communicator = WebsocketCommunicator(asgi.application, "/anime-store/party/")
        connected, subprotocol = await communicator.connect()
        assert connected
        user_name1 = "user_name1"
        await communicator.send_json_to(
            {
                "action": "create",
                "user_name": user_name1,
                "part_id": "123456",
                "request_id": 100,
            }
        )
        response = await communicator.receive_json_from()
        assert response["action"] == "create"
        assert response["user"]["user_name"] == user_name1
        # userがデータベースに作られていることを確認
        assert self.anime_user_exist(response["user"]["user_id"])
        # roomがデータベースに作られていることを確認
        assert self.anime_room_exist(response["room_id"])

    @pytest.mark.django_db
    @pytest.mark.asyncio
    @pytest.mark.with_async
    async def test_anime_party_consumer_join_ok(self):
        """AnimeConsumerのjoin actionが正しく動作することを確認するテスト"""
        communicator = WebsocketCommunicator(asgi.application, "/anime-store/party/")
        connected, subprotocol = await communicator.connect()
        assert connected
        user_name = "user_name"
        await communicator.send_json_to(
            {
                "action": "join",
                "user_name": user_name,
                "room_id": self.anime_room1.room_id,
                "part_id": "123456",
                "request_id": 100,
            }
        )
        response = await communicator.receive_json_from()

    @database_sync_to_async
    def anime_user_exist(self, user_id):
        return AnimeUser.objects.filter(user_id=user_id).exists()

    @database_sync_to_async
    def anime_room_exist(self, room_id):
        return AnimeRoom.objects.filter(room_id=room_id).exists()
