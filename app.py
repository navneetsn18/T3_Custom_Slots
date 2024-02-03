import json
from datetime import datetime, timedelta
from pytz import timezone 
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
    'Cookie': '__dcfduid=71a5e270e21911eda7d527c35b533d1e; __sdcfduid=71a5e271e21911eda7d527c35b533d1eee1da1e23a275b8013c901c63bcaee7367cf44d366b133dafd9cadeee693dfa7; __cfruid=84f26683734a341bbf2183fe0872e1537c9142c2-1695244587; cf_clearance=u8dspIx6OXzjipIMSj1B_FVuZXGTsI3SMYf72PQY_sE-1695244592-0-1-7ab1e94a.8d7dd66c.2e092a70-0.2.1695244592; __cfruid=66fce3e8dbb31112285712e12fdce56b093da831-1695246154; __dcfduid=9e7dd8a657fe11eea37d0e3f2b1973ab; __sdcfduid=9e7dd8a657fe11eea37d0e3f2b1973abc74593cdc688e1f3eef563de743b29f38ba8ff6f4c18815c9c2157621ae95dd0',
    'authorization': '',
    'Content-Type': 'application/json'
}


def sendMessage(channel_id, token):
    headers["authorization"] = token
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

    while True:
        current_time = datetime.now(timezone("Asia/Kolkata")).strftime("%H:%M:%S")
        target_time = data[str(index)]["execution_time"]
        next_target_time = (datetime.strptime(
            target_time, "%H:%M:%S") + timedelta(minutes=1)).strftime("%H:%M:%S")

        if selectedSlots[index]:
            
            if current_time >= target_time and current_time <= next_target_time:
                flag = False
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
