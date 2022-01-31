import logging
import kitesettings
from kiteconnect import KiteConnect

logging.basicConfig(level=logging.DEBUG)

kite = KiteConnect(kitesettings.API_KEY)

# https://kite.zerodha.com/connect/login?v=4&API_KEY=Q8JPzjkt8ftXgqvmXa

request_token = input("Request Token: ")
data = kite.generate_session(request_token, kitesettings.api_secret)
kite.set_access_token(data["access_token"])

print("====================")
print("Access Token: ", data["access_token"])
