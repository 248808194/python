from multiprocessing import Process, Manager
import os


def f(d, l):
    d[os.getpid()] = os.getpid()
    l.append(os.getpid())
    print(l)


if __name__ == '__main__':
    with Manager() as manager:
        d = manager.dict() # 专用语法 生成一个字典， 在多个进程之间传递共享

        l = manager.list(range(5)) # 生成一个列表，在多个进程之间传递共享
        p_list = [] #plist 一会儿要生成多个进程，将多个进程单独join，
        for i in range(10):
            p = Process(target=f, args=(d, l))
            p.start()
            p_list.append(p) #为join使用。
        for res in p_list:
            res.join()

        print(d)
        print(l)