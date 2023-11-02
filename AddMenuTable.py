from pyproj import Proj, transform
import pandas as pd
import numpy as np
import pymysql
import requests

# DB 연결 설정
DB_HOST = "localhost"
DB_USER = "sf-user"
DB_PW = "A4q8EEdh3c"

# DB 연결
CONNECT = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PW, charset='utf8')
CURSOR = CONNECT.cursor()

CURSOR.execute("USE SelectFood")
CURSOR.execute("Select 사업장명, \
               (6371 * ACos(Cos(Radians(latitude)) * Cos(Radians(37.2092017)) * Cos(Radians(126.9769365) - Radians(longitude)) + Sin(Radians(latitude)) * Sin(Radians(37.2092017)))) as Distance \
                From restaurant \
                Having Distance <= 50 \
                Order By Distance ASC;")

RESTAURANTS = CURSOR.fetchall()

for RESTAURANT in RESTAURANTS:
    uri = "https://www.happytanuki.kr/GetMenusByName?Name=" + RESTAURANT[0]
    print("URI:" + uri)
    print("Data:", end='')
    print(requests.get(uri).json())

CURSOR.close()
CONNECT.close()