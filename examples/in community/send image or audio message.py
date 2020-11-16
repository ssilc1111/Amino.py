import amino

client = amino.Client()
client.login(email='YOUR EMAIL', password='YOUR PASSWORD')
subclient = amino.SubClient(comId='COMMUNITY ID', profile=client.profile)

# Send Images
with open('file.png', 'rb') as file:
    subclient.send_message(message='MESSAGE', chatId='CHAT ID', file=file)

# Send Audios
with open('file.mp3', 'rb') as file:
    subclient.send_message(message='MESSAGE', chatId='CHAT ID', file=file, fileType="audio")