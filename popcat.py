from cloudscraper import create_scraper
from time import sleep
from tqdm import tqdm
from json import loads

scraper = create_scraper()
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJDb3VudHJ5Q29kZSI6IlRIIiwiQ291bnRyeU5hbWUiOiJUaGFpbGFuZCIsIklQIjoiMTgwLjE4My4xNTMuMjMiLCJJRCI6MzAsImV4cCI6MTYyOTA0OTU0M30.ZHk25AqVJcibQQI2_FhNYgOENmFcRL-zcQ5Njd3zc-Y"
captcha_token = "03AGdBq24ogIg7hFppU7PK7QvsspohvIOTHGObGhuR6sbnz43U1pv7uH5AogiPVuFrBAU95HIGrKLthMsFNJPb79hZmWXHoFKVqOC1xWlNjOh49gon_UFNgo55qiSqNvEi2N2Cs8cnlnnt1aG2lrLM1vxPjpO1z-q-OmUokhuS2AYViFjSN8gH_f5E6PtWgwfHAaPbvv91uBBVmr5Qlx16POMt3g9j5jMRCiwk28nSA6L969sSrpCinaSGoGTdsmyMovs-I9HdGHfpbXspOGvxs7HEope5vg-mpiKRJa-sqA03Tm206lhbugpJzUd_XobD_FRpBwTbxbQn9QChZBb0KHw-KiYrpvKq5bWCr_7lTEF-8AAmlSzQiwZrEJ5y2JTeWlvAvNQaXFGVhw0ujSTCMOO2-9jPCfbdgrNv19ocoV6i_KNM3L8R-e-qTKgYyAMrxeT2FfKmUuRY"
HTTP201Created = 201
pop_count = 800
delay_time = 30
scale = 100
clicks = 0
while True:
 url = f"https://stats.popcat.click/pop?pop_count={pop_count}&captcha_token={captcha_token}&token={token}"
 res = scraper.get(url)
 if res.status_code == HTTP201Created:
  res_json = loads(res.text)
  token = res_json["Token"]
  clicks += pop_count
 for i in tqdm(range(scale), desc="POPCAT clicks: "+str(clicks)):
  sleep(delay_time/scale)
