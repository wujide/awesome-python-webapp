# coding=utf-8
# __author__='wujide'
import urllib

import mock
import unittest
import client
from client import visit_baidu


class TestClient(unittest.TestCase):

    def test_success_request(self):
        success_send = mock.Mock(return_value='200')
        client.send_request = success_send
        self.assertEqual(visit_baidu(), '200')

    def test_fail_request(self):
        fail_send = mock.Mock(return_value='404')
        client.send_request = fail_send
        self.assertEqual(visit_baidu(), '404')

    def test_call_send_request_with_right_arguments(self):
        client.send_request = mock.Mock()
        client.visit_baidu()
        self.assertEqual(client.send_request.called, True)
        call_args = client.send_request.call_args
        self.assertIsInstance(call_args[0][0], str)
        print call_args[0][0]

    def runTest(self):
        pass

if __name__ == "__main__":
    tc = TestClient()
    tc.test_success_request()
    tc.test_fail_request()
    tc.test_call_send_request_with_right_arguments()
