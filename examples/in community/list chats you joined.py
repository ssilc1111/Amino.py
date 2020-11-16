import amino

client = amino.Client()
client.login(email='YOUR EMAIL', password='YOUR PASSWORD')
subclient = amino.SubClient(comId='COMMUNITY ID', profile=client.profile)

chats = subclient.get_chat_threads()
for chatName, chatId in zip(chats.title, chats.chatId):
    print(chatName, chatId)