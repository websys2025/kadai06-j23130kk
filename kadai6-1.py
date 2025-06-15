import requests
import json

API_ID= "024e858486448bd459008ceb45416feb236a80f7"

API_URL= "https://api.e-stat.go.jp/rest/3.0/app/json/getStatsData"

# ▼ 家計調査の統計表
params = {
    "appId": API_ID,
    "statsDataId": "0003411957",  # 家計調査（二人以上の世帯）2023年
    "lang": "J",  # 日本語を指定
    "metaGetFlg": "N",
    "cntGetFlg": "N",
    "explanationGetFlg": "N",
    "sectionHeaderFlg": "1"
}

# ▼ APIを叩いてデータ取得
response = requests.get(API_URL, params=params)
data = response.json()

# ▼ データの一部を表示
print(json.dumps(data["GET_STATS_DATA"], indent=2, ensure_ascii=False))


#【データ種別】 家計調査（消費支出）

#【エンドポイント】 https://api.e-stat.go.jp/rest/3.0/app/json/getStatsData

#【使い方】 appId（APIキー）と statsDataId を指定

