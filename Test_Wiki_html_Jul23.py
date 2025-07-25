# Test_Wiki_html_Jul23 - структура Wiki - html

from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

# ru.wikipedia.org/wiki    стр солнечной системы:
url = "https://ru.wikipedia.org/wiki/%D0%A1%D0%BE%D0%BB%D0%BD%D0%B5%D1%87%D0%BD%D0%B0%D1%8F_%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D0%B0"
response = requests.get(url)
html = response.text
print(html)


