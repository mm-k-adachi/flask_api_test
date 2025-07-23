# APIサーバーが立っている前提で
# pythonコードとして実行するとAPIを叩ける

import requests
import json

post_url = "https://12nr4wkcil.execute-api.ap-northeast-1.amazonaws.com/prod/gen_random"
json = {"x": 200, "y": 100}

# POST送信
response = requests.post(
    post_url, 
    json=json, 
    verify=False # SSL証明書の検証に失敗するので、証明書の検証をスキップ（本番ではNG）
)
print(response.json())