from flask import Flask, jsonify, request
import os
import json
import requests

app = Flask(__name__)

@app.route('/')
def index():
    a=os.environ['Authorization']
    try:
        f = open("student.csv", "r")
        for line in f.readlines():
#            print(line)
            a = line.split(",")
            if(a[0]=="21007"):
                return a[4]
        f.close()
    except Exception:
        return "Could not read to file"
    
    return "นายอาคม สุวรรณประเสริฐ เลขที่ 0 ชั้น ม.4/"

@app.route("/webhook", methods=['POST'])
def webhook():
    if request.method == 'POST':
        return "OK"

@app.route('/callb', methods=['POST'])
def callb():
    json_line = request.get_json()
    json_line = json.dumps(json_line)
    decoded = json.loads(json_line)
#    user = decoded["events"][0]['replyToken']
#    userText = decoded["events"][0]['message']['text']
    user = decoded['originalDetectIntentRequest']['payload']['data']['replyToken']
    userText = decoded['queryResult']['intent']['displayName']
    userAction = decoded['queryResult']['parameters']['studentId']
    if(userText=="ถามชื่อ"):
        try:
            f = open("student.csv", "r")
            for line in f.readlines():
                a = line.split(",")
                if(userAction==a[0]):
#                   nameList=nameList+", "+a[4]
                    sendText(user,a[4])
            f.close()
#           sendText(user,nameList)
        except Exception:
            sendText(user,"ขออภัย..ไม่สามารถเปิดไฟล์ได้")
    elif(userText=="ไอ้บ้า"):
        sendText(user,"ไม่บ้านะ")

    return '',200

@app.route('/callback', methods=['POST'])
def callback():
    json_line = request.get_json()
    json_line = json.dumps(json_line)
    decoded = json.loads(json_line)
    user = decoded['originalDetectIntentRequest']['payload']['data']['replyToken']
    userText = decoded['queryResult']['intent']['displayName']
    if(userText=="ถามชื่อ"):
        sendText(user,"น้องฟ้าจ้าาา")

    return '',200

def sendText(user, text):
  LINE_API = 'https://api.line.me/v2/bot/message/reply'
  headers = {
    'Content-Type': 'application/json; charset=UTF-8',
    'Authorization': os.environ['Authorization']    # ตั้ง Config vars ใน heroku พร้อมค่า Access token
  }
  data = json.dumps({
    "replyToken":user,
    "messages":[{"type":"text","text":text}]
  })
  r = requests.post(LINE_API, headers=headers, data=data) # ส่งข้อมูล

if __name__ == '__main__':
    app.run()
