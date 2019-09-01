import requests
from lxml import etree

headers = {
    "User-Agent": "Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1",
}
url = "http://www.budejie.com/text/"

if __name__ == '__main__':
    r = requests.get(url, headers=headers)
    data = r.content.decode()
    html = etree.HTML(data)
    text_list = html.xpath("//div[@class='j-r-list-c-desc']/a")
    for text in text_list:
        href = text.xpath('./@href')[0]
        text_list = text.xpath('./text()')
        text = "".join(text.xpath('./text()'))
        print(href + "-----" + text)
        print("*" * 100)
