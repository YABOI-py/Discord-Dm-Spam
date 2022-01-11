import requests
import json
import threading
import time
from fake_useragent import UserAgent

ua = UserAgent()

f = open("config.json")
config = json.load(f)
iden = config.get("id")

with open("tokens.txt", "r") as r:
    for each in r:
        token = each.strip()

    userID = input("Input user ID to mass spam => ")
    delay = int(input("Delay => "))


    def request():
        i = 0
        try:
            while True:
                time.sleep(delay)
                headers = {"authorization": token, "user-agent": ua.random}
                r = requests.put('https://discord.com/api/v9/channels/%7B%7D/recipients/%7B%7D%22.format(iden, userID), headers=headers')
                if r.status_code == 201:
                    print(r.status_code)
                    i += 1
                    print("Made {} gc".format(i))
                else:
                    print("ratelimit")
        except:
            print("switching token")

threads = []

for i in range(2):
    t = threading.Thread(target=request)
    t.daemon = True
    threads.append(t)

for i in range(2):
    threads[i].start()

for i in range(2):
    threads[i].join()

request()
