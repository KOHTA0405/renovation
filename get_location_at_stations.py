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
# spreadsheet.worksheet("対象候補の駅リスト").get_all_values("F2:F")

# r = requests.get("https://ja.wikipedia.org/wiki/高輪台駅")
# soup = BeautifulSoup(r.content, "html.parser")


def fetch_and_grep_and_replace(url, keyword, pattern):
    """
    指定したURLのコンテンツから、キーワードを含む行を抽出する関数

    Args:
        url: 対象のURL
        keyword: 検索するキーワード
        pattern: 除外したいタグ情報などの正規表現パターン

    Returns:
        html内でキーワードを含む要素の文字列
    """

    response = requests.get(url)
    response.raise_for_status()  # ステータスコードが異常な場合、例外を発生させる

    text = response.text
    matches = re.findall(r".*" + keyword + r".*", text, re.MULTILINE)
    before_replace_text = "".join(matches)
    replace_text = re.sub(pattern, "", before_replace_text)

    return replace_text


def get_ward(plain_text, split_word):
    """
    テキストとキーワードを受け取って、区(ward)名を返す

    Args:
        plain_text: 前の処理で終わったhtml内の該当キーワードを含む要素の文字列
        split_word: 区切り文字。今回は"区"の前後で切り分ける想定

    Returns:
        対象の区名
    """

    splited_text = plain_text.split(split_word)[0]
    replaced_text = splited_text.replace("東京都", "")
    return replaced_text + split_word


if __name__ == "__main__":
    url = "https://ja.wikipedia.org/wiki/高輪台駅"
    keyword = "北緯"
    results = fetch_and_grep_and_replace(url, keyword, "<[^>]*>")
    print(get_ward(results, "区"))
