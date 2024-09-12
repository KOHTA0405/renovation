from os import replace
from bs4 import BeautifulSoup
from google.oauth2 import service_account
import gspread
import re
import requests

scopes = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive",
]

credentials = service_account.Credentials.from_service_account_file(
    "./secret/spread_sheet_sa_key.json", scopes=scopes
)

gc = gspread.authorize(credentials)

spreadsheet_url = "https://docs.google.com/spreadsheets/d/1bTMOKgRDPEYP9DE_LtVQ9oJ-0UjciDi5jUhgj-yc0aY"

# スプレッドシートオブジェクトを取得
spreadsheet = gc.open_by_url(spreadsheet_url)

# シート名を指定して、その中の値を取得
# F列には、リクエスをしたいwikipediaのURLが載っている
# spreadsheet.worksheet("対象候補の駅リスト").get_all_values("G2:G")


# シートを指定
worksheet = spreadsheet.worksheet("foo")

# 書き込むデータ（リスト形式）
data = [["A1"], ["B1"], ["C1"]]

# A1セルから、指定した範囲にデータを書き込む
worksheet.update("B2", data)
