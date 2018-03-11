import sys
import time
class ProgressConsole(object):
    def process(self, num, total, name):
        now_num = num
        avg = int(now_num/total*50)
        process_now = '>' * avg
        space_now = ' ' * (50 - avg)
        r = '\r当前任务：%s 总计：\033[1;31;31m %s \033[0m 进度：[%s%s] 当前：\033[1;31;33m %s%% \033[0m' % (name, total, process_now, space_now, avg*2)
        sys.stdout.write(r)
        sys.stdout.flush()


if __name__ == '__main__':
    p1 = ProgressConsole()
    p2 = ProgressConsole()
    for i in range(100):
        time.sleep(0.1)
        p1.process(i, 100, '222')