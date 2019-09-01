import requests
import json
import re

headers = {
    "User-Agent": "Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1",
}
url = "http://www.budejie.com/text/"

if __name__ == '__main__':
    r = requests.get(url, headers=headers)
    data = r.content.decode()
    # <a href="/detail-29695966.html">记得小时候大人总是嘱咐“走路不要踩...</a>
    # data = re.findall(r"<a href=\"/detail-[0-9]*\.html\"></a>", data, re.S)
    ret = re.findall(r"<a href=\"/detail\-[0-9]*.html\">(.*?)</a>", data, re.S)
    for single in ret:
        print(single)
