from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "สวัสดีครับ"

@app.route("/webhook", methods=['GET', 'POST'])
def webhook() :
    if request.method == 'POST'"
        reture 'OK"

if __name__ == '__main__':
    app.run(debug=True)
