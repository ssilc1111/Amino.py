import amino

client = amino.Client()
client.login(email='YOUR EMAIL', password='YOUR PASSWORD')

# Url Example
# https://aminoapps.com/p/EXAMPLE

objectId = client.get_from_code("EXAMPLE").objectId
print(objectId)