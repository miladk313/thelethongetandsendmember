from telethon import TelegramClient, sync
from telethon.tl.functions.channels import InviteToChannelRequest

#Get User From Channel And Add To Another Channel
#You have to be admin in both channels
#api_id and api_hash get from https://my.telegram.org

api_id = '1146959' 
api_hash = '094167c937e300feddb7555d083a61b9'

client = TelegramClient('xxx', api_id, api_hash).start()

# get all the channels that I can access
channels = {d.entity.username: d.entity
            for d in client.get_dialogs()
            if d.is_channel}

# choose the one that I want to list users from
channel = channels['miladk313test']

# get all the users and print them
for u in client.get_participants(channel):
    if not u.id == 169196065:
        client(InviteToChannelRequest(
        channel,
        u.id,  #user_id
        ))
    print(u.id, u.first_name, u.last_name, u.username)
