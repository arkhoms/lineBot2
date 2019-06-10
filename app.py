from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "สวัสดีครับ"

@app.route('/webhook', methods=['POST'])
def webhook() :
#    if request.method == 'POST':
        return "OK"

if __name__ == '__main__':
    app.run()
