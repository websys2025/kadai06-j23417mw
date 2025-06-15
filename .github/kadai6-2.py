# kadai6-2.py


import requests

# APIキー (e-Statで登録して取得)
API_KEY = "3ecf19dfb9f0feff73e52189d434238c9232265e"

# APIエンドポイント
url = "http://api.e-stat.go.jp/rest/3.0/app/json/getStatsData"

# 労働力調査の統計データID
STATS_DATA_ID = "00200573"

# パラメータ設定
params = {
    "appId": API_KEY,
    "statsDataId": STATS_DATA_ID,
    "metaGetFlg": "Y",
    "cntGetFlg": "N",
    "sectionHeaderFlg": "2",
}

# リクエスト送信
response = requests.get(url, params=params)

# JSON形式で受け取る
data = response.json()

# 結果ステータス確認
if data["GET_STATS_DATA"]["RESULT"]["STATUS"] != 0:
    print("APIエラー:", data["GET_STATS_DATA"]["RESULT"]["ERROR_MSG"])
    exit()

# VALUEリストを抽出
values = data["GET_STATS_DATA"]["STATISTICAL_DATA"]["DATA_INF"]["VALUE"]

# 最初の10件を表示
print("\n■ 労働力調査データ (先頭10件):")
for val in values[:10]:
    time = val.get("@time")
    area = val.get("@area")
    cat01 = val.get("@cat01")
    value = val.get("$")
    print(f"時期: {time}, 地域: {area}, 区分: {cat01}, 値: {value}")
