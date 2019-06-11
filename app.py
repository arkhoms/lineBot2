from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "สวัสดีครับ"

@app.route("/webhook", methods=['POST'])
def webhook():
#    if request.method === 'POST':
        return "OK"

@app.route('/callback', methods=['POST'])
def callback():
  json_line = request.get_json()
  json_line = json.dumps(json_line)
  decoded = json.loads(json_line)
  user = decoded["events"][0]['replyToken']
  #id=[d['replyToken'] for d in user][0]
  #print(json_line)
  print("ผู้ใช้：",user)
  sendText(user,'งง') # ส่งข้อความ งง
  return '',200

if __name__ == '__main__':
    app.run()
