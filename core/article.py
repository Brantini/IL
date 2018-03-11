def download_book(book_no, book_name):
    from utils.factory import RequestFactory
    from data.url_file import ArticelUrl
    from utils import file_util
    from utils.process import ProgressConsole
    from data.xpath_file import ArticelXpath
    import re
    import html
    from lxml import etree
    req = RequestFactory()
    pro = ProgressConsole()
    # content = req.getContent(url=ArticelUrl.book_url % book_no)
    content = req.getRequest(url=ArticelUrl.book_url % book_no)
    # patt1 = r'<a href="(\d+?.html)">(.+?)</a>'
    # ass = re.findall(patt1, content.decode('gbk'))
    ass = req.find(content, ArticelXpath.msg_xpath)
    datas = []
    # for i in ass:
    #     temp = {}
    #     temp['title'] = i[1]
    #     temp['link'] = ArticelUrl.content_detail % (book_no, i[0])
    #     datas.append(temp)
    for i in ass:
        try:
            temp = {}
            temp['title'] = req.find(i, ArticelXpath.title)[0]
            temp['link'] = ArticelUrl.content_detail % (book_no, req.find(i, ArticelXpath.link)[0])
            datas.append(temp)
        except Exception:
            continue
    for i in range(datas.__len__()):
        data = req.getRequest(url=datas[i]['link'])
        ele = req.find(data, ArticelXpath.content_xpath)[0]
        result = html.unescape(str(etree.tostring(ele, encoding='utf-8'), encoding='utf-8'))
        dd = re.sub(r'<[^>]+>', '', result)
        dd = re.sub(r'\n', 'flag', dd)
        dd = re.sub(r'\s', '', dd)
        dd = re.sub(r'(flag)+', '\n    ', dd)
        with open('D:\\Article\\' + book_name, 'a') as f:
            f.write('\n' + datas[i]['title'] + '\n')
            f.close()
        with open('D:\\Article\\' + book_name, 'a') as f:
            f.write(dd)
            f.close()
        pro.process(i + 1, datas.__len__(), book_name)
    print('已完成！')

import threading

if __name__ == '__main__':
    threads = []
    # t1 = threading.Thread(target=download_book, args=('9868', '超级全能学生.txt',))
    # t2 = threading.Thread(target=download_book, args=('24276', '元尊.txt',))
    # t3 = threading.Thread(target=download_book, args=('24277', '飞剑问道.txt',))
    # t4 = threading.Thread(target=download_book, args=('4772', '圣墟.txt',))
    # t5 = threading.Thread(target=download_book, args=('3840', '神荒龙帝', ))
    # t6 = threading.Thread(target=download_book, args=('7356', '不死不灭',))
    # t7 = threading.Thread(target=download_book, args=('6169', '遮天',))
    t8 = threading.Thread(target=download_book, args=('3', '莽荒纪.txt',))
    t9 = threading.Thread(target=download_book, args=('4805', '天域苍穹.txt',))
    t10 = threading.Thread(target=download_book, args=('6010', '武动乾坤.txt',))
    t11 = threading.Thread(target=download_book, args=('92', '不死武尊',))
    t12 = threading.Thread(target=download_book, args=('7629', '盘龙.txt'))
    t13 = threading.Thread(target=download_book, args=('5617', '超凡传.txt'))
    t14 = threading.Thread(target=download_book, args=('8', '完美世界.txt'))
    # threads.append(t1)
    # threads.append(t2)
    # threads.append(t3)
    # threads.append(t4)
    # threads.append(t6)
    # threads.append(t7)
    # threads.append(t8)
    # threads.append(t9)
    # threads.append(t10)
    # threads.append(t11)
    # threads.append(t12)
    # threads.append(t13)
    threads.append(t14)
    for tt in threads:
        tt.start()
    for tt in threads:
        tt.join()
    print('任务已经结束！')