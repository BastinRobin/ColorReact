import os
import tornado.httpserver
import tornado.ioloop
import tornado.web
 
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')
 
def main():
    settings = dict(
        cookie_secret=str(os.urandom(45)),
        template_path=os.path.join(os.path.dirname(__file__), "templates"),
        static_path=os.path.join(os.path.dirname(__file__), "static"),
        xsrf_cookies=True,
        autoreload=True,
        gzip=True,
        debug=True,
        login_url='/login',
        autoescape=None
    )
    application = tornado.web.Application([
        (r"/", MainHandler),
    ], **settings)
    http_server = tornado.httpserver.HTTPServer(application)
    port = int(os.environ.get("PORT", 5000))
    http_server.listen(port)
    tornado.ioloop.IOLoop.instance().start()
 
if __name__ == "__main__":
    main()