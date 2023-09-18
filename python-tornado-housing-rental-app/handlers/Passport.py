# coding:utf-8

import logging
from .BaseHandler import BaseHandler

class IndexHandler(BaseHandler):
    def get(self):
        logging.debug("debug msg")
        logging.info("info msg")
        logging.warning("warning msg")
        logging.error("error msg")
        print("print msg")
        self.write("Hello first")
