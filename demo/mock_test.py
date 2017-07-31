# coding=utf-8
# __author__='wujide'
import urllib

import mock
import unittest
import import_test
from import_test import visit_ustack


class TestClient(unittest.TestCase):

    def test_success_request(self):
        success_send = mock.Mock(return_value='200')
        import_test.send_request = success_send
        self.assertEqual(visit_ustack(), '200')

    def test_fail_request(self):
        fail_send = mock.Mock(return_value='404')
        import_test.send_request = fail_send
        self.assertEqual(visit_ustack(), '404')

    def runTest(self):
        pass

if __name__ == "__main__":
    tc = TestClient()
    tc.test_success_request()
    tc.test_fail_request()
