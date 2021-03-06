from match.models.chatroom import ChatRoom
from match.models.chatroomuser import ChatRoomUser
from match.models.chatmessage import ChatMessage
from match.models.userinfo import UserInfo
from match.models.posts import Posts

def create(current_user_id, post_id):
    # 自分の持っているチャットルームを取得
    current_user_chat_rooms = __toRoomIdsArray(ChatRoomUser.objects.filter(user_id=current_user_id))
    # 自分の持っているチャットルームからチャット相手のいるルームを探す
    chat_rooms = ChatRoomUser.objects.filter(chat_room_id__in=current_user_chat_rooms, post_id=post_id)
    # 募集したユーザーのレコードを抽出
    post_user = Posts.objects.get(pk=post_id)

    roomid = 0
    if(len(chat_rooms) == 0):
        room = ChatRoom()
        room.save()
        roomid = room.id

        chat_room_me = ChatRoomUser(chat_room=ChatRoom.objects.get(pk=roomid), post=Posts.objects.get(pk=post_id), user=UserInfo.objects.get(pk=current_user_id))
        chat_room_you = ChatRoomUser(chat_room=ChatRoom.objects.get(pk=roomid), post=Posts.objects.get(pk=post_id), user=UserInfo.objects.get(pk=post_user.userinfo_id))
        chat_room_me.save()
        chat_room_you.save()
    else:
        roomid = chat_rooms[0].chat_room.id
    return roomid

def messages(room_id):
    room = ChatRoom.objects.get(pk=room_id)
    chatmessages = ChatMessage.objects.filter(chat_room=room)
    retmessages = []
    for chatmessage in chatmessages:
        retmessages.append({
            "name": chatmessage.user.name,
            "message": chatmessage.message
        })
    return retmessages

def registmessage(room_id, user_id, post_id, message):
    messages = ChatMessage()
    user = UserInfo.objects.get(pk=user_id)
    post = Posts.objects.get(pk=post_id)
    room = ChatRoom.objects.get(pk=room_id)
    messages.chat_room = room
    messages.user = user
    messages.post = post
    messages.message = message
    messages.save()

def __toRoomIdsArray(roomusers):
    roomidlist = list()
    for roomuser in roomusers:
        roomidlist.append(roomuser.chat_room_id)
    return roomidlist