# coding:utf-8

import tornado.web
import tornado.ioloop
import tornado.options
import tornado.httpserver
import config

from tornado.options import define, options
from tornado.web import RequestHandler
from urls import handlers

define("port", type=int, default=8000, help="Run server on the given port.")

class IndexHandler(RequestHandler):
    def get(self):
        pass


def main():
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        handlers, **config.settings
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current.start()

if __name__ == '__main__':
    main()