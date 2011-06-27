#!/usr/bin/python
import unittest
from basic_tests import BasicTestCase
from admin_tests import AdminTestCase
from todo_tests import TodoTestCase

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(BasicTestCase))
    suite.addTest(unittest.makeSuite(AdminTestCase))
    suite.addTest(unittest.makeSuite(TodoTestCase))
    return suite
