import requests
import json
from datetime import datetime

#道路種別を指定．この例は一般道
road_type = "3"

#日時を指定
time_code_from = "20250512"+"0000"
time_code_to   = "20250512"+"2355"

#緯度経度を指定．この例は東京
min_x = 139.45
min_y = 35.55
max_x = 139.93
max_y = 35.82

api = f"https://api.jartic-open-traffic.org/geoserver?service=WFS&version=2.0.0&request=GetFeature&typeNames=t_travospublic_measure_5m&srsName=EPSG:4326&outputFormat=application/json&exceptions=application/json&cql_filter=道路種別={road_type} AND 時間コード>={time_code_from} AND 時間コード<={time_code_to} AND BBOX(ジオメトリ,{min_x},{min_y},{max_x},{max_y},'EPSG:4326')"
response = requests.get(api)

print(response.text[:200])

data = json.loads(response.text)