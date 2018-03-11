#-*-coding:utf-8-*-
if __name__ == '__main__':
    from utils.factory import RequestFactory
    from data.xpath_file import JianDanXpath
    from data.url_file import JianDanUrl
    from lxml import etree
    import html as hhh
    from utils import file_util
    import re
    req = RequestFactory()
    html = req.getRequest(url=JianDanUrl.index_url)
    index_data = req.find(html, JianDanXpath.index)
    title_list = []
    for i in index_data:
        temp = {}
        temp['title'] = req.find(i, JianDanXpath.index_title)[0]
        temp['href'] = req.find(i, JianDanXpath.index_title_link)[0]
        title_list.append(temp)
    print(title_list.__str__())

    for i in title_list:
        temp_html = req.getRequest(url=i['href'])
        i['content'] = hhh.unescape(str(etree.tostring(req.find(temp_html, JianDanXpath.content)[0], encoding='utf-8'), encoding='utf-8'))
        pt = r'<p>.*</p>'
        rept = re.compile(pt)
        temp = re.findall(rept, i['content'])
        s = ''
        for j in range(temp.__len__()):
            s = s + temp[j]
        i['result'] = s

    for i in title_list:
        file_util.save(r'JianDan\\' + i['title'] + '.html', i['result'])