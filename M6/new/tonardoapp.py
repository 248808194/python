import tornado.ioloop
import tornado.web


# pip3 install tornado

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        print(111)
        u = self.get_argument('username')
        p = self.get_argument('password')
        if u == 'zhoutao' and p == '123':
            print(123)
            self.write("OK")
        else:
            self.write("滚")

    def post(self, *args, **kwargs):
        u = self.get_argument('username')
        p = self.get_argument('password')
        print(u, p)
        self.write('POST')


application = tornado.web.Application([
    (r"/index", MainHandler),
])
if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
