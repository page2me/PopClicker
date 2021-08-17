from requests import post
from time import sleep
from tqdm import tqdm
from json import loads
import warnings

warnings.filterwarnings("ignore")
url = 'https://www.popdog.click/clicked/v2'
data = {"clicks" : 2000, "uuid" : "10a63aa0-190a-4dba-bcbd-77024f32c89c", "username" : "page2me"}
HTTP200OK = 200
clicks = 0;
pop_count = 2000
while True:
 if clicks >= pop_count:
  break
 res = post(url, json=data, verify=False)
 if res.status_code == HTTP200OK:
  delay_time = 10
  scale = 100
  res_json = loads(res.text)
  clicks += pop_count
  for i in tqdm(range(scale),desc=f"POPDOG {clicks} clicks = {res_json['clicks']} "):
   sleep(delay_time/scale)
 if clicks%24 == 0:
  delay_time = 30
  scale = 100
  for i in tqdm(range(scale),desc=f"POPDOG {clicks} clicks = {res.text} "):
   sleep(delay_time/scale)
