## parser.py
import requests
from bs4 import BeautifulSoup

## HTTP GET Request
req = requests.get('https://beomi.github.io/beomi.github.io_old/')

## HTML 소스 가져오기
html = req.text

## HTTP Header 가져오기
header = req.headers

## HTTP Status 가져오기 (200: 정상)
status = req.status_code

## HTTP가 정상적으로 되었는지 (True/False)
is_ok = req.ok

soup = BeautifulSoup(html, 'html.parser')
