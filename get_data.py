import json
import requests

# APIキー
with open("./secret/secret.json") as f:
    api_key = json.load(f)["api_key"]

# 取引時期(年)
year_param = "2023"

# APIのURL
url = (
    f"https://www.reinfolib.mlit.go.jp/ex-api/external/XIT001?year={year_param}&area=13"
)

# ヘッダーを作成
headers = {"Ocp-Apim-Subscription-Key": api_key}

# GETリクエストを送信
response = requests.get(url, headers=headers)

# ステータスコードを確認
if response.status_code == 200:
    # 成功した場合
    data = response.json()
    # print(data)
else:
    # 失敗した場合
    print("API呼び出しに失敗しました:", response.status_code)
