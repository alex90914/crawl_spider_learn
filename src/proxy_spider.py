import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"
}
proxies = {
    "http": "http://116.50.60.66:53281"
}

if __name__ == '__main__':
    r = requests.get("http://www.baidu.com", proxies=proxies, headers=headers)
    print(r.status_code)
