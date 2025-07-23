# これはAPIサーバーとして立てておくもの

from flask import *

app = Flask(__name__)

@app.route('/', methods=['POST'])
def switch():
   switch = request.data.decode('utf-8')  # デコード
   switch = json.loads(switch)
   if switch["set"] == "ON":
       switch_ans = "switch_ON"
   elif switch["set"] == "OFF":
       switch_ans = "switch_OFF"
   else:
       switch_ans = "None"
   return jsonify(switch_ans)

# 送信するJSON
# 　{"set": "ON"}か{"set": "OFF"} それ以外は None が返ってくるようにします。