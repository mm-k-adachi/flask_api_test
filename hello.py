# flaskのクイックスタートを参考に作成
# https://flask.palletsprojects.com/en/stable/quickstart/

from flask import Flask
from markupsafe import escape # 入力文字列のエスケープ
from flask import request # HTTPリクエスト 

app = Flask(__name__)

# ルーティング
@app.route('/') # どのURLが関数のトリガーとなるか
def index():
    return "<p>This is Index</p>"

# 末尾に/helloが付くと画面にHello World!と表示される
@app.route('/hello') 
def hello():
    return "<p>Hello World!</p>"

# <>で囲まれた部分が可変。関数で受け取れる。型指定可能。pathとすれば/含めて受け取れる
@app.route('/user/<string:username>') 
def show_use_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}' # エスケープすることで意図しないスクリプト実行を防ぐ


# # HTTPメソッドもある
# @app.route('/login', methods=['GET', 'PSOT'])
# def login():
#     if request.method == 'POST':
#         return do_the_login()
#     else:
#         return show_the_login_form()

# # 明示的にメソッドを指定ることも可能
# @app.get('/login')
# def login_get():
#     return show_the_login_form()  


# if __name__ == "__main__":
#     app.run(debug=True)