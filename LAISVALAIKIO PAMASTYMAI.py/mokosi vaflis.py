import csv
import requests
from os import environ

ip_api_url = 'https://freegeoip.app/json/122.35.203.161'
weather_url = 'http://api.openweathermap.org/data/2.5/weather/'
ip_list = ['122.35.203.161', '174.217.10.111', '187.121.176.91', '176.114.85.116', '174.59.204.133', '54.209.112.174',
           '109.185.143.49', '176.114.253.216', '210.171.87.76', '24.169.250.142']

def get_city_country():
    res = requests.get(f"{ip_api_url}").json()
    return res['city'], res['ip']

print(get_city_country())