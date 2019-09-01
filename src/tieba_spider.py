import requests


class TieBaSpider:
    def __init__(self, tie_ba_name):
        self.tie_ba_name = tie_ba_name
        self.temp_url = "https://tieba.baidu.com/f?kw=" + tie_ba_name + "&ie=utf-8&pn={}"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"
        }
        pass

    def get_url_list(self):
        url_list = []
        for i in range(5):
            url_list.append(self.temp_url.format(i * 50))
        return url_list

    def parse_url(self, url):
        response = requests.get(url, headers=self.headers)
        return response.content.decode("utf-8")

    def save_html(self, html_str, page_num):
        file_path = "d:/tie_ba/{}-第{}页.html".format(self.tie_ba_name, page_num)
        print(file_path)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(html_str)

    def run(self):
        url_list = self.get_url_list()
        for url in url_list:
            html_str = self.parse_url(url)
            page_num = url_list.index(url) + 1
            self.save_html(html_str, page_num)


if __name__ == '__main__':
    spider = TieBaSpider("lol")
    spider.run()
