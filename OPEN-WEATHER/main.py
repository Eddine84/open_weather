#2YW26WX1MVUWQHALYQGKBH4W


#n 'oubliaez pas pythob anywhere pour lancer le scypte quand je veux en ligne
from twilio.rest import Client
import requests

account_sid = "AC2c1f8341377b4e0905d0563ea9441f87"
auth_token = "99126ce7de79bcccdaf24c17215bf130"




END_POINT = "https://api.openweathermap.org/data/2.5/forecast"
parameters = {
    "lat":45.070339,
    "lon":7.686864,
    "appid":"8dc66af07140846505c55719064dfbe7",
    "ctn":4
}

response = requests.get(url=END_POINT,params=parameters)
response.raise_for_status()

data = response.json()

meoteo_list = data["list"]
will_rain = False
for object in meoteo_list:
   condition =  object["weather"][0]["id"]
   if condition < 700:
      will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
                              body="SBah el khir Hobi ! aujourdhuis il va pleuvoir ! svp n'oubli pas de prendre un parapluit avec toi ♥",
                              from_="+19292961782",
                              to="+41774811118"
                          )
    print(message.status)