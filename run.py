#!/usr/bin/python

from ims import app

if __name__ == '__main__':
    #host="10.32.100.97"
    host=None
    if not host:
        host = "127.0.0.1"
    app.run(host=host, port=8000)
