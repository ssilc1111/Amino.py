import amino

client = amino.Client()
client.login(email='YOUR EMAIL', password='YOUR PASSWORD')

# Send Images
with open('file.png', 'rb') as file:
    client.send_message(message='MESSAGE', chatId='CHAT ID', file=file)

# Send Audios
with open('file.mp3', 'rb') as file:
    client.send_message(message='MESSAGE', chatId='CHAT ID', file=file, fileType="audio")