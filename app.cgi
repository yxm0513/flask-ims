#!/usr/bin/python
from wsgiref.handlers import CGIHandler
from ims import app

if __name__ == '__main__':
	CGIHandler().run(app)
