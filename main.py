import os
import tornado.httpserver
import tornado.ioloop
import tornado.web


testJson = {
    tag: "stuff",
    anotherTag: "things"
}

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello world again!")

class TilesHandler(tornado.web.RequestHandler):
    def get(self):
        self.write(testJson)

def main():
    application = tornado.web.Application([
        (r"/", MainHandler),
        (r"/tiles", TilesHandler),
    ])
    http_server = tornado.httpserver.HTTPServer(application)
    port = int(os.environ.get("PORT", 5000))
    http_server.listen(port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()