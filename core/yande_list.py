from utils.factory import RequestFactory
from data.url_file import YandeUrl
from utils import file_util
from utils.process import ProgressConsole
from data.xpath_file import YandeXpath
import re
import html
from lxml import etree
from data import proxies
from utils.database import YandeDbUtil

if __name__ == '__main__':
    req = RequestFactory()
    pro = ProgressConsole()
    db = YandeDbUtil()
    keyword = 'thighhighs'
    content = req.getRequest(url=YandeUrl.index_url % ('', keyword), timeout=30)
    total_page_ele = req.find(content, YandeXpath.total_page)
    if total_page_ele is not None:
        total_page = int(total_page_ele[0].text)
        for i in range(total_page):
            msg = '第' + str(i + 1) + '页'
            pro.process(i + 1, total_page, msg)
            temp_c = req.getRequest(url=YandeUrl.index_url % (i + 1, keyword))
            temp_i = req.find(content, YandeXpath.detail_img)
            for j in temp_i:
                # with open('D:\\Yande\\' + keyword + '.txt', 'a') as wr:
                #     wr.write(j + '\n')
                db.insertPic(keyword, j)
