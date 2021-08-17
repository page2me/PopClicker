from requests import post
from time import sleep
from tqdm import tqdm
from json import loads
import warnings

warnings.filterwarnings("ignore")
delay_time = 2
scale = 10
url = 'https://www.popdog.click/clicked/v2'
data = {"clicks" : 2000, "uuid" : "10a63aa0-190a-4dba-bcbd-77024f32c89c", "username" : "page2me"}
while True:
 res = post(url, json=data, verify=False)
 res_json = loads(res.text)
 for i in tqdm(range(scale),desc="POPDOG clicks: "+str(res_json["clicks"])):
  sleep(delay_time/scale)
