from lxml import etree

if __name__ == '__main__':
    html_str = """
                <div>
                    <ul>
                        <li class="item-1"><a href="link1.html">first item</li>
                        <li class="item-1"><a href="link2.html">second item</li>
                        <li class="item-1"><a>third item</li>
                        <li class="item-0"><a href="link4.html">four item</li>
                    </ul>
                </div>
                """
    html = etree.HTML(html_str)
    ret = html.xpath("//li[@class='item-1']")
    for ele in ret:
        item = dict()
        item["title"] = ele.xpath("./a/text()")[0] if len(ele.xpath("./a/text()")) > 0 else None
        item["href"] = ele.xpath("./a/@href")[0] if len(ele.xpath("./a/@href")) > 0 else None
        print(item)
