import pymysql
pymysql.install_as_MySQLdb()

class YandeDbUtil(object):
    conn = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='123456',
        db='yande',
    )

    def insertPic(self, keyword, link):
        try:
            with self.conn.cursor() as cur:
                sql = 'INSERT INTO pic(keyword, link)VALUES(%s,%s)'
                cur.execute(sql, (keyword, link))
            self.conn.commit()
        except Exception as e:
            print(e)
        finally:
            cur.close()
