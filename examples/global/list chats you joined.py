import amino

client = amino.Client()
client.login(email='YOUR EMAIL', password='YOUR PASSWORD')

chats = client.get_chat_threads()
for chatName, chatId in zip(chats.title, chats.chatId):
    print(chatName, chatId)