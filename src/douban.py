import requests
import json

headers = {
    "Referer": "https://m.douban.com/movie/beta",
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive",
    "User-Agent": "Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1",
    "Cookie": """ll="118318"; bid=G3Xa-kE9DK8; __utma=30149280.1652097654.1567333314.1567333314.1567333314.1; __utmz=30149280.1567333314.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmt=1; ap_v=0,6.0; _vwo_uuid_v2=DB086BB3D85098D235107D6AC1B7F4AC8|5b2390b656cc5aba37ed2768567a0e03; __utmb=30149280.3.10.1567333314; Hm_lvt_6d4a8cfea88fa457c3127e14fb5fabc2=1567333427,1567333560; talionnav_show_app="0"; _ck_desktop_mode=; vmode=; _ga=GA1.2.1652097654.1567333314; _gid=GA1.2.1899148727.1567333577; Hm_lpvt_6d4a8cfea88fa457c3127e14fb5fabc2=1567333669"""
}
url = "https://m.douban.com/rexxar/api/v2/movie/suggestion"
req_data = {
    "start": 0,
    "count": 10,
    "new_struct": 1,
    "with_review": 1,
    "for_mobile": 1
}

if __name__ == '__main__':
    r = requests.get(url, data=req_data, headers=headers)
    data = r.content.decode()
    with open("douban.json", "w", encoding="utf-8") as f:
        data = json.loads(data)
        f.write(json.dumps(data, ensure_ascii=False, indent=2))
