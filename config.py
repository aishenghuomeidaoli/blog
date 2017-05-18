# _*_ coding: utf-8 _*_
import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SQL_URL = 'sqlite:///' + os.path.join(basedir, 'db.sqlite3')
    HOST = '127.0.0.1'
    PORT = 5010
    DEBUG = True
