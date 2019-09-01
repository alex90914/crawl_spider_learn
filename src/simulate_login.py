import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"
}
'''模拟登陆'''
if __name__ == '__main__':
    post_url = "http://www.renren.com/ajaxLogin/login"
    post_data = {
        "email": "email",
        "password": "password."
    }
    session = requests.session()
    r = session.post(post_url, data=post_data, headers=headers)
    print(r.content.decode())
    print(requests.utils.dict_from_cookiejar(r.cookies))
