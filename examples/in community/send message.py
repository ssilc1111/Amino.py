import amino

client = amino.Client()
client.login(email='YOUR EMAIL', password='YOUR PASSWORD')
subclient = amino.SubClient(comId='COMMUNITY ID', profile=client.profile)

subclient.send_message(message='MESSAGE', chatId='CHAT ID')