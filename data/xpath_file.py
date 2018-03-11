# coding:utf8

class JianDanXpath(object):
    index_title = 'h2/a/text()'
    index_title_link = 'h2/a/@href'
    index = '//div[@class="indexs"]'
    content = '//div[@class="post f"]'

class BaiduImage(object):
    pass

class ArticelXpath(object):
    content_xpath = '//div[@id="content"]'
    msg_xpath = '//div[@id="list"]/dl/dd'
    title = 'a/text()'
    link = 'a/@href'

class YandeXpath(object):
    detail_img = '//a[@class="directlink largeimg"]/@href'
    total_page = '//div[@class="pagination"]/a[last()-1]'