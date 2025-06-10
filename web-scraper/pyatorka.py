import json

import requests

# cookies = {
#     "SRV": " e77e1143-d1ec-4f57-ab82-ae1840bbd83d",
#     "_ym_uid": "1749510379361247225",
#     "spsc": "1749586259393_345536e882f483167efb71f522556c39_ze8mXWDaxU0teM1tGNbZ05ysqJVhw32YGftSFK8wPyMZ",
#     "spid": "1749510198062_933c2e08d4f3482c74ce5229d57be26e_hpr4gqf5d67co31x",
#     "_ym_d": "1749510379",
#     "TS01658276": "01a2d8bbf415f7a4815ed8d6776539b9a6863d16ba6ac07a37370dab1aa76b61e84fcb7ae0505497b12f74199fc1606220ee6c3d0ee4cc209e8f22934c3b267ee8d802ccb1a596867397d77674d9c3da9a5c01d471b283ec0889a433d19794fbe903f005243b5e496513c147251262725c7ad0ede3",
#     "TS018c7dc5": "01a2d8bbf4e681ceab401f1eda71b87f5d0120ebfb65e3501a560ccebc43fa952250cbb72c448fff8bb512e90fbe9841457377f90e98746cfcfeda193f43b7a1e8a08837b0",
# }


session = requests.Session()

# Set cookies directly
session.cookies.set(
    "__Host-next-auth.csrf-token",
    "dfd38a7ec6af6ebf749775a3ba79c41a93229a3e3f2d9aa2d048d93ac537e4bb",
    domain="5ka.ru",
    path="/",
)
session.cookies.set(
    "__Secure-next-auth.callback-url",
    "https://5ka.ru/",
    domain="5ka.ru",
    path="/",
)

headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "Connection": "keep-alive",
    "Cookie": "TS018c7dc5=01a2d8bbf473b76274e75b5d6f0c958a5d382771e25699643840c55653070d9313a3c780cb82633b545e59e28013d8fb4b5a581ddf94e8e434e37f08bcdd59e034f9fc0f8b; TS01658276=01a2d8bbf4a1d5c1937b749f573ab4c906eba022774ce6cb3d0d45243d8b07bb84fe019258f8a22692dd828d2c8f4144060344f6ca4b7ddf9af678e79f819bfd5f848830f6bff5d08412fc6d72224fa6471de1beb06a48e4a7d2087f233dffea96b4e85bf335239d28936c5b3e45d856e4c42f2aa2; spsc=1749588305832_4e30197ae989dfaea2cf5f173ba19471_ze8mXWDaxU0teM1tGNbZ05ysqJVhw32YGftSFK8wPyMZ; SRV=e77e1143-d1ec-4f57-ab82-ae1840bbd83d; _ym_d=1749510379; _ym_uid=1749510379361247225; spid=1749510198062_933c2e08d4f3482c74ce5229d57be26e_hpr4gqf5d67co31x",
    "Host": "5d.5ka.ru",
    "Origin": "https://5ka.ru",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.1 Safari/605.1.15",
    "X-APP-VERSION": "0.1.1.dev",
    "X-DEVICE-ID": "8f58907b-0502-4ba7-9501-c62deff783d8",
    "X-PLATFORM": "webapp",
}

response = session.get(
    "https://5d.5ka.ru/api/catalog/v2/stores/Y232/categories",
    headers=headers,
)

print(response.text)
