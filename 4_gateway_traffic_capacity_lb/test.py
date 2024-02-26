import requests # need to install through pip install requests
import time

url = " http://34.117.254.167"

requests_per_second = 10
sleep_interval = 1.0 / requests_per_second

def send_requests(url, total_seconds=600):
    for _ in range(total_seconds * requests_per_second):
        try:
            response = requests.get(url)
            print(f"Time: {time.strftime('%Y-%m-%d %H:%M:%S')}, Response Code: {response.status_code}")
        except requests.RequestException as e:
            print(f"Request failed: {e}")
        finally:
            time.sleep(sleep_interval)

send_requests(url)
