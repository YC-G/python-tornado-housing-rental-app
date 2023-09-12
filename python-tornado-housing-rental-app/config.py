# coding:utf-8

import os

settings = {
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
    "template_path": os.path.join(os.path.dirname(__file__), "template"),
    "cookie_secret": "64819E0F-D054-4154-8D1E-5C2F4606F037",
    "xsrf_cookies": "15B8952E-B97F-4AE8-8B3B-31AFC0D1BE3B",
    "debug": True,
}