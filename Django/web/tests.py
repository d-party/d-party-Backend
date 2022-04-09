from http import client
from django.test import Client, TestCase
import pytest
from http import HTTPStatus


class TestIndexView(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.endpoint = "/"

    @pytest.mark.django_db
    def test_ok_200(self):
        response = self.client.get(self.endpoint)
        assert response.status_code == HTTPStatus.OK


class TestUsageView(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.endpoint = "/usage"

    @pytest.mark.django_db
    def test_ok_200(self):
        response = self.client.get(self.endpoint)
        assert response.status_code == HTTPStatus.OK
