import urllib.parse
from django.shortcuts import render
from django.urls import is_valid_path
from django.views.generic import TemplateView, RedirectView
from streamer.models import AnimeRoom
from django.shortcuts import get_object_or_404
from django.http import Http404

from streamer.models import AnimeRoom, AnimeUser


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Home"
        return context


class UsageView(TemplateView):
    template_name = "usage.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Usage"
        return context


class AdminChartsView(TemplateView):
    template_name = "chart.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Chart"
        return context


class AnimeRoomLobby(TemplateView):
    template_name = "lobby_redirect.html"

    def get(self, request, **kwargs):
        base_url = "https://anime.dmkt-sp.jp/animestore/sc_d_pc?"
        room_id = self.kwargs["room_id"]
        try:
            anime_room = get_object_or_404(AnimeRoom, room_id=room_id)
        except:
            raise Http404()
        if anime_room is None or anime_room.deleted_at is not None:
            raise Http404()
        url_param = urllib.parse.urlencode(
            {
                "partId": anime_room.part_id,
                "party": "join",
                "room_id": room_id,
            }
        )
        url = base_url + url_param
        context = {
            "title": "Lobby",
            "redirect_url": str(url),
        }
        return self.render_to_response(context)
