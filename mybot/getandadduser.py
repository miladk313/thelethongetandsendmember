from telethon import TelegramClient, sync
from telethon.tl.functions.messages import AddChatUserRequest

#api_id and api_hash get from https://my.telegram.org

api_id = '1146959' 
api_hash = '094167c937e300feddb7555d083a61b9'

client = TelegramClient('xxx', api_id, api_hash).start()
	
    
# get all the groups that I can access
groups = {d.entity.id: d.entity
            for d in client.get_dialogs()
            }

# choose the one that I want to list users from
group = groups[398941703]

#target group id
chat_id=341297965

# get all the users and join them to target group
for u in client.get_participants(group):
    if not u.id == 169196065:
        client(AddChatUserRequest(
        chat_id,
        u.id,  #user_id
        fwd_limit=10  # Allow the user to see the 10 last messages
        ))
    print(u.id, u.first_name, u.last_name, u.username)
