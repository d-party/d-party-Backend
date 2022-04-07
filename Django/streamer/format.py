import imp
from pydantic import BaseModel
from uuid import UUID
from typing import Dict, List, Optional, Any, Union


class User(BaseModel):
    """Userの定義

    attributes:
        user_id ([UUID]): uuid形式で記述されたid
        user_name([str]): strで記述された名前
    """

    user_id: UUID
    user_name: str


class ResponseBaseFormat(BaseModel):
    """ResponseBaseFormatの定義
    受信するデータはactionというカラムを使って判定する
    このクラスを継承して受信時のデータの型チェックを行う

    attirbutes:
        action ([str]): joinやleaveなどの文字列
    """

    action: str


class Join(ResponseBaseFormat):
    action: str = "join"
    room_id: UUID
    user: User


class Leave(ResponseBaseFormat):
    action: str = "leave"
    user: User


class Create(ResponseBaseFormat):
    action: str = "create"
    room_id: UUID
    user: User


class Option(BaseModel):
    time: float
    src: Union[str, None]
    paused: str
    rate: str
    part_id: str


class VideoOperation(ResponseBaseFormat):
    action: str = "video_operation"
    room_id: UUID
    operation: str
    user: User
    option: Option


class OperationNotification(ResponseBaseFormat):
    action: str = "operation_notification"
    room_id: UUID
    operation: str
    user: User


class Reaction(ResponseBaseFormat):
    action: str = "reaction"
    reaction_type: str


class SyncRequest(ResponseBaseFormat):
    action: str = "sync_request"
    user: User


class SyncResponse(ResponseBaseFormat):
    action: str = "sync_response"
    option: Option


class UserAdd(ResponseBaseFormat):
    action: str = "user_add"
    user: User


class Leave(ResponseBaseFormat):
    action: str = "leave"
    user: User


class ServerMessage(ResponseBaseFormat):
    action: str = "server_message"
    message_type: str


class UserList(ResponseBaseFormat):
    action: str = "user_list"
    user_list: List[User]


class BaseGroupSend(BaseModel):
    type: str
    sender_channel_name: str
    response: ResponseBaseFormat


class GroupSend(BaseGroupSend):
    type: str = "group_send"


class RoomSend(BaseGroupSend):
    type: str = "room_send"


class HostSend(BaseGroupSend):
    type: str = "host_send"


class UserSend(BaseGroupSend):
    type: str = "user_send"
    to_user: User
