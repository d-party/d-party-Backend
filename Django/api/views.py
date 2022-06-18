from cProfile import label
import os
import datetime
import pandas as pd

from streamer.models import AnimeUser, AnimeRoom, AnimeReaction, ReactionType
from django.shortcuts import render
from django.db.models import Count
from django_dynamic_shields.views import DynamicShieldsView
from django_dynamic_shields.data import ShieldsData
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, AllowAny

from rest_framework import status
from distutils.version import LooseVersion, StrictVersion

# Create your views here.
class ChromeExtensionVersionCheckAPI(APIView):
    """chromeの拡張機能のバージョンをチェックし、
    現在のバックエンドと問題なくメッセージ可能なバージョンか否かを通知する
    """

    permission_classes = [AllowAny]

    def get(self, request, format=None) -> Response:
        """chromeのバージョンをgetのパラメータとして受け取り、
        バックエンドが問題なく処理できるバージョンであるかを確認する

        Args:
            request ([type]): [description]
            format ([type], optional): [description]. Defaults to None.

        Returns:
            [Response]: {"description": "理由を記述"}
            バージョンチェックの成否は

        """
        if "extension-version" in request.GET:
            current_version: str = str(request.GET.get("extension-version"))
            required_version: str = str(os.getenv("CHROME_EXTENSION_REQUIRED_VERSION"))
            try:
                current_strict_version = StrictVersion(current_version)
                required_strict_version = StrictVersion(required_version)
            except:
                return Response(
                    {"message": "求めているバージョンの記法と一致しません"},
                    status=status.HTTP_406_NOT_ACCEPTABLE,
                )

            return Response(
                {"is_possible": current_strict_version >= required_strict_version},
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                {"message": "extension-versionパラメータが存在しません"},
                status=status.HTTP_400_BAD_REQUEST,
            )


class AnimeActiveUserPerDayAPI(APIView):
    """アクティブユーザー数を返す
    アクティブユーザー数とは、ルーム内に存在していたユーザーである
    """

    permission_classes = [IsAdminUser]

    def get(self, request, format=None) -> Response:
        """アクティブユーザー数のdictを返す

        Args:
            request ([type]): [description]
            format ([type], optional): [description]. Defaults to None.

        Returns:
            [Response]: {"description": "理由を記述"}

        """
        Active_User_Per_Day_Set = (
            AnimeUser.objects.extra(select={"day": "date( created_at )"})
            .values("day")
            .annotate(count=Count("created_at"))
            .order_by("day")
        )
        Active_User_Per_Day = list(Active_User_Per_Day_Set)
        if (
            len(Active_User_Per_Day) == 0
            or Active_User_Per_Day[-1]["day"] != datetime.date.today()
        ):
            Active_User_Per_Day.append({"day": datetime.date.today(), "count": 0})

        Active_User_Per_Day_Pd = (
            pd.DataFrame(Active_User_Per_Day)
            .set_index("day")
            .asfreq("1D", fill_value=0)
        )

        Active_User_Per_Day_Pd["day"] = Active_User_Per_Day_Pd.index.map(
            lambda x: x.to_pydatetime().date()
        )
        return Response(
            {
                "data": Active_User_Per_Day_Pd.to_dict(orient="records"),
            }
        )


class AnimeActiveRoomPerDayAPI(APIView):
    """アクティブルーム数を返す
    アクティブルーム数とは、ユーザーによって作られたルームの合計である
    """

    permission_classes = [IsAdminUser]

    def get(self, request, format=None) -> Response:
        """アクティブルーム数のdictを返す

        Args:
            request ([type]): [description]
            format ([type], optional): [description]. Defaults to None.

        Returns:
            [Response]: {"description": "理由を記述"}

        """
        Active_Room_Per_Day_Set = (
            AnimeRoom.objects.extra(select={"day": "date( created_at )"})
            .values("day")
            .annotate(count=Count("created_at"))
            .order_by("day")
        )
        Active_User_Room_Day = list(Active_Room_Per_Day_Set)
        if (
            len(Active_User_Room_Day) == 0
            or Active_User_Room_Day[-1]["day"] != datetime.date.today()
        ):
            Active_User_Room_Day.append({"day": datetime.date.today(), "count": 0})
        Active_Room_Per_Day_Pd = (
            pd.DataFrame(Active_User_Room_Day)
            .set_index("day")
            .asfreq("1D", fill_value=0)
        )

        Active_Room_Per_Day_Pd["day"] = Active_Room_Per_Day_Pd.index.map(
            lambda x: x.to_pydatetime().date()
        )
        return Response(
            {
                "data": Active_Room_Per_Day_Pd.to_dict(orient="records"),
            }
        )


class AnimeRoomReactionCountAPI(APIView):
    """アニメルーム内のリアクションのカウント結果を返すAPI"""

    permission_classes = [IsAdminUser]

    def get(self, request, format=None) -> Response:
        response = []
        for x in ReactionType.choices:
            response.append(
                {
                    "count": AnimeReaction.objects.filter(reaction_type=x[0])
                    .all()
                    .count(),
                    "reaction_type": x[1],
                }
            )
        return Response({"data": response})


class AnimeRoomReactionAllCountAPI(APIView):
    """アニメルーム内のリアクションの累計カウント結果を返すAPI"""

    permission_classes = [IsAdminUser]

    def get(self, request, format=None) -> Response:
        return Response({"data": {"count": AnimeReaction.objects.all().count()}})


class AnimeUserAllCountAPI(APIView):
    """アニメルーム内のユーザー数の累計カウント結果を返すAPI"""

    permission_classes = [IsAdminUser]

    def get(self, request, format=None) -> Response:
        return Response({"data": {"count": AnimeUser.objects.all().count()}})


class AnimeRoomAllCountAPI(APIView):
    """アニメルーム数の累計カウント結果を返すAPI"""

    permission_classes = [IsAdminUser]

    def get(self, request, format=None) -> Response:
        return Response({"data": {"count": AnimeRoom.objects.all().count()}})


class AnimeUserAliveCountAPI(APIView):
    """現在接続中のアニメルーム内のユーザー数のカウント結果を返すAPI"""

    permission_classes = [IsAdminUser]

    def get(self, request, format=None) -> Response:
        return Response({"data": {"count": AnimeUser.objects.alive().count()}})


class AnimeRoomAliveCountAPI(APIView):
    """現在接続中のアニメルーム数の現在のカウント結果を返すAPI"""

    permission_classes = [IsAdminUser]

    def get(self, request, format=None) -> Response:
        return Response({"data": {"count": AnimeRoom.objects.alive().count()}})


class RoomCountShieldsAPI(DynamicShieldsView):
    def create_shields_data(self):
        self.shields_data = ShieldsData(
            label="TotalRoom", message=str(AnimeRoom.objects.all().count())
        )


class RoomCountParDayShieldsAPI(DynamicShieldsView):
    def create_shields_data(self):
        """アクティブルーム数の平均バッジ

        Args:
            request ([type]): [description]
            format ([type], optional): [description]. Defaults to None.

        Returns:
            [Response]: {"description": "理由を記述"}

        """
        Active_Room_Per_Day_Set = (
            AnimeRoom.objects.extra(select={"day": "date( created_at )"})
            .values("day")
            .annotate(count=Count("created_at"))
            .order_by("day")
        )
        Active_User_Room_Day = list(Active_Room_Per_Day_Set)
        if (
            len(Active_User_Room_Day) == 0
            or Active_User_Room_Day[-1]["day"] != datetime.date.today()
        ):
            Active_User_Room_Day.append({"day": datetime.date.today(), "count": 0})
        Active_Room_Per_Day_Pd = (
            pd.DataFrame(Active_User_Room_Day)
            .set_index("day")
            .asfreq("1D", fill_value=0)
        )

        Active_Room_Per_Day_Pd["day"] = Active_Room_Per_Day_Pd.index.map(
            lambda x: x.to_pydatetime().date()
        )
        Active_Room_Per_Day_Mean = str(Active_Room_Per_Day_Pd["count"].mean()) + "/day"
        self.shields_data = ShieldsData(label="Room", message=Active_Room_Per_Day_Mean)


class UserCountShieldsAPI(DynamicShieldsView):
    def create_shields_data(self):
        self.shields_data = ShieldsData(
            label="TotalUser", message=str(AnimeUser.objects.all().count())
        )


class ReactionCountShieldsAPI(DynamicShieldsView):
    def create_shields_data(self):
        self.shields_data = ShieldsData(
            label="TotalReaction", message=str(AnimeReaction.objects.all().count())
        )
