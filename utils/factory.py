import requests, re
from lxml import etree

class RequestFactory(object):
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36',
        'Host': 'yande.re',
        'Upgrade-Insecure-Requests': 1,
        'Connection': 'keep-alive',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'
    }

    def getRequest(self, url, timeout=3, proxies=None):
        request = None
        while True:
            try:
                if proxies is None:
                    request = requests.get(url=url, headers=self.header, timeout=timeout)
                else:
                    request = requests.get(url=url, headers=self.header, timeout=timeout, proxies=proxies)
            except Exception as e:
                pass
            if request is not None:
                if request.status_code == 200:
                    break
        content = request.content.decode('gbk', 'ignore')
        return etree.HTML(content)

    def getContent(self, url, timeout=3, proxies=None):
        request = None
        while True:
            try:
                if proxies is None:
                    request = requests.get(url=url, headers=self.header, timeout=timeout)
                else:
                    request = requests.get(url=url, headers=self.header, timeout=timeout, proxies=proxies)
            except Exception as e:
                pass
            if request is not None:
                if request.status_code == 200:
                    break
        return request.content

    def find(self, html, xpath):
        element = html.xpath(xpath)
        return element
