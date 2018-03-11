if __name__ == '__main__':
    import time
    s = time.clock()
    time.sleep(2)
    s2 = time.clock()
    print((s2 - s)> 2)