import os
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import status
from distutils.version import LooseVersion, StrictVersion

# Create your views here.
class ChromeExtensionVersionCheckAPI(APIView):
    """chromeの拡張機能のバージョンをチェックし、
    現在のバックエンドと問題なくメッセージ可能なバージョンか否かを通知する
    """

    def get(self, request, format=None):
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
            current_version = request.GET.get("extension-version")
            required_version = str(os.getenv("CHROME_EXTENSION_REQUIRED_VERSION"))
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
