# coding:utf-8

import os

# Application
settings = {
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
    "template_path": os.path.join(os.path.dirname(__file__), "template"),
    "cookie_secret": "64819E0F-D054-4154-8D1E-5C2F4606F037",
    "xsrf_cookies": True,
    "debug": True,
}

# mysql
mysql_options = dict(
    host="localhost",
    user="root",
    password="Gyc072503",
    database="iHome"
)

#redis
redis_options= dict(
    host="localhost",
    port=6379
)

log_file = os.path.join(os.path.dirname(__file__), "logs/log")
log_level = "debug"