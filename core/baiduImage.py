if __name__ == '__main__':
    from utils.factory import RequestFactory
    from data.url_file import BaiduImageUrl
    from utils import file_util
    import re
    req = RequestFactory()
    index = 0
    key = '英格兰'
    for page in range(10):
        content = req.getContent(url=BaiduImageUrl.search_url % (key, page*20))
        pattern_pic = r'"objURL":"(.*?)",'
        img_urls = re.findall(pattern_pic, content.decode('utf-8'), re.S)
        print('第' + str(page + 1) + '页开始下载！')
        for i in range(img_urls.__len__()):
            pic = req.getContent(url=img_urls[i])
            if pic is None:
                continue
            file_util.saveImage('BaiduImage' + '\\' + key + str(index) + '.jpg', pic)
            index = index + 1
        print('第' + str(page + 1) + '页下载完毕！')
