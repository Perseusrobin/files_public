import requests
import random
import httpx
import time

keys = ['49m3Ul2I-b860MJ5h-Xo563e7u', '9bu7q5J6-1z4dyK75-Y019wEr7', '42l76YcR-38S1MEi5-3j5Iw4Y8', 'zo943YU0-UH0o597u-6FYV209G', '3K9WA08O-v238iCt9-5no7yb10', '2lNz873o-C02T6Mg8-KJ9x4O78\n']

while True:

  try:
    headers = {
      "CF-Client-Version": "a-6.11-2223",
      "Host": "api.cloudflareclient.com",
      "Connection": "Keep-Alive",
      "Accept-Encoding": "gzip",
      "User-Agent": "okhttp/3.12.1",
    }

    with httpx.Client(base_url="https://api.cloudflareclient.com/v0a2223",
                      headers=headers,
                      timeout=30.0) as client:

      r = client.post("/reg")
      id = r.json()["id"]
      license = r.json()["account"]["license"]
      token = r.json()["token"]

      r = client.post("/reg")
      id2 = r.json()["id"]
      token2 = r.json()["token"]

      headers_get = {"Authorization": f"Bearer {token}"}
      headers_get2 = {"Authorization": f"Bearer {token2}"}
      headers_post = {
        "Content-Type": "application/json; charset=UTF-8",
        "Authorization": f"Bearer {token}",
      }

      json = {"referrer": f"{id2}"}
      client.patch(f"/reg/{id}", headers=headers_post, json=json)

      client.delete(f"/reg/{id2}", headers=headers_get2)

      key = random.choice(keys)

      json = {"license": f"{key}"}
      client.put(f"/reg/{id}/account", headers=headers_post, json=json)

      json = {"license": f"{license}"}
      client.put(f"/reg/{id}/account", headers=headers_post, json=json)

      r = client.get(f"/reg/{id}/account", headers=headers_get)
      account_type = r.json()["account_type"]
      referral_count = r.json()["referral_count"]
      license = r.json()["license"]

      client.delete(f"/reg/{id}", headers=headers_get)
      print("取得到的 WARP+ 金鑰為：" + license)
      url = "https://api.telegram.org/bot6495173524:AAE-C2sScxOQtNbaKbjMdsWyYcuylLtLNrM/sendMessage?chat_id=6333495069&text=" + str(license)
      print(requests.get(url).json())
  except:
    time.sleep(15)
