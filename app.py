import json
from datetime import datetime, timedelta
from pytz import timezone 
import time
import requests
from flask import Flask, request
import threading

app = Flask(__name__)

data = {
    "0": {
        "channel_id": "1120747716675379270",
        "execution_time": "15:59:58",
        "slot_time": "20:00:00"
    },
    "1": {
        "channel_id": "871660033346273310",
        "execution_time": "16:00:58",
        "slot_time": "20:10:00"
    },
    "2": {
        "channel_id": "1120747891556892783",
        "execution_time": "16:01:58",
        "slot_time": "20:20:00"
    },
    "3": {
        "channel_id": "931014584398151680",
        "execution_time": "16:02:58",
        "slot_time": "20:30:00"
    },
    "4": {
        "channel_id": "979602165213560852",
        "execution_time": "16:03:58",
        "slot_time": "20:40:00"
    },
    "5": {
        "channel_id": "1099611138255245362",
        "execution_time": "16:04:58",
        "slot_time": "20:50:00"
    },
    "6": {
        "channel_id": "1120747950310703185",
        "execution_time": "16:05:58",
        "slot_time": "21:00:00"
    },
    "7": {
        "channel_id": "871660106738192395",
        "execution_time": "16:06:58",
        "slot_time": "21:10:00"
    },
    "8": {
        "channel_id": "1120748006921207919",
        "execution_time": "16:07:58",
        "slot_time": "21:20:00"
    },
    "9": {
        "channel_id": "931014658691850312",
        "execution_time": "16:08:58",
        "slot_time": "21:30:00"
    },
    "10": {
        "channel_id": "936436671547838464",
        "execution_time": "16:09:58",
        "slot_time": "21:40:00"
    },
    "11": {
        "channel_id": "1099608890028597318",
        "execution_time": "16:10:58",
        "slot_time": "21:50:00"
    },
    "12": {
        "channel_id": "1120748075586179123",
        "execution_time": "16:11:58",
        "slot_time": "22:00:00"
    },
    "13": {
        "channel_id": "871661544109408287",
        "execution_time": "16:12:58",
        "slot_time": "22:10:00"
    },
    "14": {
        "channel_id": "1120748170159329421",
        "execution_time": "16:13:58",
        "slot_time": "22:20:00"
    },
    "15": {
        "channel_id": "931014715075870830",
        "execution_time": "16:14:58",
        "slot_time": "22:30:00"
    },
    "16": {
        "channel_id": "936436721007083630",
        "execution_time": "16:15:58",
        "slot_time": "22:40:00"
    },
    "17": {
        "channel_id": "1099608995620196372",
        "execution_time": "16:16:58",
        "slot_time": "22:50:00"
    },
    "18": {
        "channel_id": "1120748242733367316",
        "execution_time": "16:17:58",
        "slot_time": "23:00:00"
    },
    "19": {
        "channel_id": "926299147991146637",
        "execution_time": "16:18:58",
        "slot_time": "23:10:00"
    },
    "20": {
        "channel_id": "1120748302305067048",
        "execution_time": "16:19:58",
        "slot_time": "23:20:00"
    },
    "21": {
        "channel_id": "931014770394533919",
        "execution_time": "16:20:58",
        "slot_time": "23:30:00"
    },
    "22": {
        "channel_id": "987204034920341514",
        "execution_time": "16:21:58",
        "slot_time": "23:40:00"
    },
    "23": {
        "channel_id": "1099611246963200020",
        "execution_time": "16:22:58",
        "slot_time": "23:50:00"
    },
    "24": {
        "channel_id": "1120748435658772693",
        "execution_time": "16:23:58",
        "slot_time": "00:00:00"
    },
    "25": {
        "channel_id": "935386195192606760",
        "execution_time": "16:24:58",
        "slot_time": "00:10:00"
    },
    "26": {
        "channel_id": "1120748506810962060",
        "execution_time": "16:25:58",
        "slot_time": "00:20:00"
    },
    "27": {
        "channel_id": "970903197411577887",
        "execution_time": "16:26:58",
        "slot_time": "00:30:00"
    },
    "28": {
        "channel_id": "1099611366488289320",
        "execution_time": "16:27:58",
        "slot_time": "00:40:00"
    },
    "29": {
        "channel_id": "1128513565821780008",
        "execution_time": "16:28:58",
        "slot_time": "00:50:00"
    },
    "30": {
        "channel_id": "1128514391516651611",
        "execution_time": "16:29:58",
        "slot_time": "01:00:00"
    }
}

payload = json.dumps({
    "mobile_network_type": "unknown",
    "content": "TEAM NAME - Team NS\n\nIGN- NS彡Negi\nID - 5118720160\nDISCORD TAG- <@518717935351627817> \n\nIGN - NS彡RAWAT\nID - 5142138048\nDISCORD TAG - <@683524169731670067> \n\nIGN - botlikeDEEPZI\nID - 55525406801\nDISCORD TAG- <@758947828696875030> \n\nIGN - atankwadiboss\nID - 570448226\nDISCORD TAG - <@659383817160622080> \n\n(OPTIONALS)\n\nIGN - NS彡LUV\nID - 583882197\nDISCORD TAG - <@544885539439116299>",
    "tts": False,
    "flags": 0
})

testPayload = json.dumps({
    "mobile_network_type": "unknown",
    "content": "Booking Slots for Today!!",
    "tts": False,
    "flags": 0
})

headers = {
  "authority": "discord.com",
  "method": "POST",
  "scheme": "https",
  "Accept": "*/*",
  "Accept-Encoding": "gzip, deflate, br",
  "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
  "Authorization": "",
  "Content-Length": "505",
  "Content-Type": "application/json",
  "Cookie": "__dcfduid=98a26bb05fb311ee812e37455704b97f; __sdcfduid=98a26bb15fb311ee812e37455704b97f93f259c5e370d3de7441346312cc0958c998619ff509ac07915616f4c95987b2; _ga=GA1.1.443817457.1696093550; __cfruid=81cb73d76db9afbc222c2bae88a7c7a0b8ff5ef4-1706954315; _cfuvid=tLm5NRyT3yQxEh1DC3cCCdmK_7JyUjRPiZtnm5p7RrA-1706954315405-0-604800000; cf_clearance=GYlrm__WYLv7_Z0pMtsszQegG_1ESqc8vNymwu6IKEU-1706954319-1-ARDjFK/BJrgYz4icfO7Q2ymg6/CNqffoPFyh4lPxq4EOVeMzsytrfqOW7wDd67JDocwj3iYqvINDLhzh64Rw9Uk=; _gcl_au=1.1.1255555462.1706954330; OptanonConsent=isIABGlobal=false&datestamp=Sat+Feb+03+2024+15%3A28%3A50+GMT%2B0530+(India+Standard+Time)&version=6.33.0&hosts=&landingPath=https%3A%2F%2Fdiscord.com%2F&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1; _ga_Q149DFWHT7=GS1.1.1706954330.2.0.1706954330.0.0.0",
  "Origin": "https://discord.com",
  "Sec-Ch-Ua": "\"Not A(Brand\";v=\"99\", \"Google Chrome\";v=\"121\", \"Chromium\";v=\"121\"",
  "Sec-Ch-Ua-Mobile": "?0",
  "Sec-Ch-Ua-Platform": "\"macOS\"",
  "Sec-Fetch-Dest": "empty",
  "Sec-Fetch-Mode": "cors",
  "Sec-Fetch-Site": "same-origin",
  "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
  "X-Debug-Options": "bugReporterEnabled",
  "X-Discord-Locale": "en-GB",
  "X-Discord-Timezone": "Asia/Calcutta",
  "X-Super-Properties": "eyJvcyI6Ik1hYyBPUyBYIiwiYnJvd3NlciI6IkNocm9tZSIsImRldmljZSI6IiIsInN5c3RlbV9sb2NhbGUiOiJlbi1HQiIsImJyb3dzZXJfdXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChNYWNpbnRvc2g7IEludGVsIE1hYyBPUyBYIDEwXzE1XzcpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS8xMjEuMC4wLjAgU2FmYXJpLzUzNy4zNiIsImJyb3dzZXJfdmVyc2lvbiI6IjEyMS4wLjAuMCIsIm9zX3ZlcnNpb24iOiIxMC4xNS43IiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjI2MzU4MiwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
}




def sendMessage(channel_id, token):
    print("Inside Sned Message")
    headers["Authorization"] = token
    url = url = "https://discord.com/api/v9/channels/"+channel_id+"/messages"
    response = requests.request("POST", url, headers=headers, data=payload)
    if response.status_code == 200:
        print("Message sent!")
        return True
    return False


def sendTestMessage(channel_id, token):
    headers["authorization"] = token
    url = url = "https://discord.com/api/v9/channels/"+channel_id+"/messages"
    response = requests.request("POST", url, headers=headers, data=payload)
    if response.status_code == 200:
        print("Test Message Sent")
        return True
    return False


def slotBooking(selectedSlots, token, backup_token):

    index = 0
    timer = 0
    while True:
        current_time = datetime.now(timezone("Asia/Kolkata")).strftime("%H:%M:%S")
        target_time = data[str(index)]["execution_time"]
        next_target_time = (datetime.strptime(
            target_time, "%H:%M:%S") + timedelta(minutes=1)).strftime("%H:%M:%S")
        if timer==0 or time == 30:
            print("Current time: "+current_time+" Next Target Time: "+next_target_time)
            timer+=1
        else:
            timer = 0
        if selectedSlots[index]:
            
            if current_time >= target_time and current_time <= next_target_time:
                flag = False
                print("Will send a message now!!")
                if sendMessage(data[str(index)]["channel_id"], token):
                    index += 1
                    flag = True
                if flag == False:
                    if sendMessage(data[str(index)]["channel_id"], backup_token):
                        index += 1
            elif current_time > next_target_time:
                index += 1
                print("Time Overpassed")
        else:
            index += 1
        if index == len(selectedSlots):
            break


def testLogin(token):
    # 1118099267421212732
    if sendTestMessage("1131234133000069140", token):
        print("Send Test Login with token sucess: "+ token)
        return True
    return False


@app.route("/run")
def run():
    token = request.args.get('token1')
    backup_token = request.args.get('token2')

    print("Slot Booking Started on : "+datetime.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M:%S.%f'))

    selectedSlots = [False,False,False, # 8 - 8:20
                     False,False,False, # 8:30 - 8:50
                     False,False,False, # 9 - 9:20
                     False,False,False, # 9:30 - 9:50
                     False,False,False, # 10 - 10:20
                     False,True,False, # 10:30 - 10:50
                     True,False,True,# 11 - 11:20
                     False,True,False, # 11:30 - 11:50
                     True,False,True,# 12 - 12:20
                     False,True,False, # 12:30 - 12:50
                     True]# 1
    if testLogin(token) and testLogin(backup_token):
        print("Tokens Loaded Successfully.")
        thread = threading.Thread(target=slotBooking, args=(selectedSlots,token,backup_token,))
        thread.start()
        # slotBooking(selectedSlots,token,backup_token)
    else:
        return "Tokens Expired"
    
    print("Slot Booking Ended on : "+datetime.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M:%S.%f'))
    return "Done"

@app.route("/")
def home():
    return "Hello World!"
