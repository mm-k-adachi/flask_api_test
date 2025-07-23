# flaskのクイックスタートを参考に作成
# https://flask.palletsprojects.com/en/stable/quickstart/

from flask import Flask

app = Flask(__name__)

@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify({"message": "Hello, API!"})

if __name__ == "__main__":
    app.run(debug=True)