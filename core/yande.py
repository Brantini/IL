import sys
sys.path.append('/projects/Intrest')
from utils.factory import RequestFactory
from data.url_file import YandeUrl
from utils import file_util
from utils.process import ProgressConsole
from data.xpath_file import YandeXpath
import re
import html
from lxml import etree
from data import proxies

if __name__ == '__main__':
    req = RequestFactory()
    pro = ProgressConsole()
    # keyword = 'fairy_fencer_f'
    keyword = 'tsunako'
    content = req.getRequest(url=YandeUrl.index_url % ('', keyword), timeout=30)
    total_page_ele = req.find(content, YandeXpath.total_page)
    if total_page_ele is not None:
        total_page = int(total_page_ele[0].text)
        for i in range(total_page):
            temp_c = req.getRequest(url=YandeUrl.index_url % (i + 1, keyword))
            with open('/projects/pic/pages.txt', 'a') as vv:
                vv.write('第' + str(i) + '页：' + YandeUrl.index_url % (i + 1, keyword) + '\n')
            temp_i = req.find(temp_c, YandeXpath.detail_img)
            for j in range(temp_i.__len__()):
                msg = '第' + str(i + 1) + '页'
                pro.process(j + 1, temp_i.__len__(), msg)
                pic = req.getContent(url=temp_i[j], timeout=300)
                with open('/projects/pic/record.txt', 'a') as ss:
                    ss.write(temp_i[j] + '\n')
                if pic is None:
                    continue
                try:
                    path = '/projects/pic/1/' + keyword + str(i) + str(j) + '.' + temp_i[j].split('.')[-1]
                    with open(path, 'wb') as wr:
                        wr.write(pic)
                except Exception as e:
                    print(e)