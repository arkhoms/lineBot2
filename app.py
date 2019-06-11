from flask import Flask, jsonify, request
import json
#import requests

app = Flask(__name__)

@app.route('/')
def index():
    return "สวัสดีครับ"

@app.route("/webhook", methods=['POST'])
def webhook():
    if request.method == 'POST':
        return "OK"

@app.route('/callback', methods=['POST'])
def callback():
    text='งง'
    json_line = request.get_json()
    json_line = json.dumps(json_line)
    decoded = json.loads(json_line)
    user = decoded["events"][0]['replyToken']
    #id=[d['replyToken'] for d in user][0]
    #print(json_line)
#    print("ผู้ใช้：",user)
#    sendText(user,'งง')
    LINE_API = 'https://api.line.me/v2/bot/message/reply'
    Authorization = 'Bearer bNSZWdvzwydRYzhK14gMTbhCuYThxxXGoP+78YvKw5wOFsOiFh11bEcbJjvB7UORayyWvkZtjZKcBiqQHpr79VgdCS4UBG5m38NSiNhCX0Vw6scv/QDB5DUHo6zVhGY449Basd6Y5Em+KzasZtxErgdB04t89/1O/w1cDnyilFU=' # ใส่ ENTER_ACCESS_TOKEN เข้าไป
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization': Authorization
    }
#    data = json.dumps({
#        "replyToken":user,
#        "messages":[{"type":"text","text":text}]
#    })
#    r = requests.post(LINE_API, headers=headers, data=data) # ส่งข้อมูล
    return '',200

def sendText(user, text):
  LINE_API = 'https://api.line.me/v2/bot/message/reply'
  Authorization = 'Bearer bNSZWdvzwydRYzhK14gMTbhCuYThxxXGoP+78YvKw5wOFsOiFh11bEcbJjvB7UORayyWvkZtjZKcBiqQHpr79VgdCS4UBG5m38NSiNhCX0Vw6scv/QDB5DUHo6zVhGY449Basd6Y5Em+KzasZtxErgdB04t89/1O/w1cDnyilFU=' # ใส่ ENTER_ACCESS_TOKEN เข้าไป
  headers = {
    'Content-Type': 'application/json; charset=UTF-8',
    'Authorization': Authorization
  }
  data = json.dumps({
    "replyToken":user,
    "messages":[{"type":"text","text":text}]
  })
  r = requests.post(LINE_API, headers=headers, data=data) # ส่งข้อมูล

if __name__ == '__main__':
    app.run()
