import requests
import time
import schedule

#  SCRIPT BY GR6Y

def func():
    payload = {
    'content': "MESSAGE HERE"
}

    header = {
    'authorization': 'YOUR AUTH HERE'
}

    r = requests.post("https://discord.com/api/v9/channels/CHANNEL ID/messages",
                     data=payload, headers=header)

schedule.every(1).minute.do(func)

while True:
    schedule.run_pending()
    time.sleep(1)
