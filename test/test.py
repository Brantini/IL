if __name__ == '__main__':
    from utils.factory import RequestFactory
    from data.url_file import ArticelUrl
    from utils import file_util
    from data.xpath_file import ArticelXpath
    from lxml import etree
    import re, html
    req = RequestFactory()
    url = 'http://www.biqiuge.com/book/4772/2940354.html'
    data = req.getRequest(url=url)
    ele = req.find(data, ArticelXpath.content_xpath)[0]
    result = html.unescape(str(etree.tostring(ele, encoding='utf-8'), encoding='utf-8'))
    dd = re.sub(r'<[^>]+>', '', result)
    print(dd)
    dd = re.sub(r'\n', 'flag', dd)
    dd = re.sub(r'\s', '', dd)
    dd = re.sub(r'flag', '\n', dd)
    with open(r'D:\testFile.txt', 'w+') as f:
        f.write(dd)