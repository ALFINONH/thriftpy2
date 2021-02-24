from line.client import LineClient

client = LineClient()
client.qr_login()

print(client.client.getProfile())
