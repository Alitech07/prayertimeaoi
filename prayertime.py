import requests

from pprint import pprint as print

def times(city):

  url = f"https://api.pray.zone/v2/times/today.json?city={city}&school=3"
  r = requests.get(url)
  rj = r.json()
  vaqtlar = rj['results']['datetime']

  return vaqtlar[0]['times']