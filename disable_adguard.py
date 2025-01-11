#!/usr/bin/env/python3

from decouple import config
import requests


AUTH_HEADER = config("AUTH_HEADER")
ADGUARD_URL = config("ADGUARD_URL")

while True:
    inp = input("How many seconds would you like to "
                "disable the ad-blocker for? ")
    if not inp.isdigit(): # Check for all numerical first
        continue
    try:
        seconds = int(inp)
        break
    except ValueError:
        continue

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": f"Basic {AUTH_HEADER}",
}
payload = {
    "enabled": False,
    "duration": seconds * 1000,
}

response = requests.post(ADGUARD_URL, headers=headers, json=payload)
print(response.status_code)
