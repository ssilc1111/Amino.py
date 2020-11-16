import amino

client = amino.Client()
client.login(email='YOUR EMAIL', password='YOUR PASSWORD')

client.send_message(message='MESSAGE', chatId='CHAT ID')