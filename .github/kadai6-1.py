
import requests
# APIキーをセット（自身のものに置き換えること）
API_KEY = "3ecf19dfb9f0feff73e52189d434238c9232265e"
# APIエンドポイント
url = "http://api.e-stat.go.jp/rest/3.0/app/json/getStatsData"
# 労働力調査（statsDataIdは例。最新のものはeStatサイトで要確認）
STATS_DATA_ID = "00200573"  # 労働力調査のID（例）

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

# 結果のステータス確認
if data["GET_STATS_DATA"]["RESULT"]["STATUS"] != 0:
    print("APIエラー:", data["GET_STATS_DATA"]["RESULT"]["ERROR_MSG"])
    exit()

# データ抽出例：VALUE一覧（値のリスト）
values = data["GET_STATS_DATA"]["STATISTICAL_DATA"]["DATA_INF"]["VALUE"]

# 取得したデータの一部表示
for val in values[:10]:  # 最初の10件を表示
    print(f"時間: {val.get('@time')}, 値: {val.get('#text')}")
