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
            return a[1]
        f.close()
    except Exception:
        return "Could not read to file"
    
    return "นายอาคม สุวรรณประเสริฐ เลขที่ 0 ชั้น ม.4/"

@app.route("/webhook", methods=['POST'])
def webhook():
    if request.method == 'POST':
        return "OK"

@app.route('/callback', methods=['POST'])
def callback():
    json_line = request.get_json()
    json_line = json.dumps(json_line)
    decoded = json.loads(json_line)
#    user = decoded["events"][0]['replyToken']
#    userText = decoded["events"][0]['message']['text']
    user = decoded['originalDetectIntentRequest']['payload']['data']['replyToken']
    userText = decoded['queryResult']['intent']['displayName']
#    sendText(user,"ไม่บ้าน้าาา")
#    sendText(user,userText)
    try:
        f = open("student.csv", "r")
        for line in f.readlines():
            sendText(user,line)
        f.close()
    except Exception:
        sendText(user,"ขออภัย..ไม่สามารถเปิดไฟล์ได้")
    
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
