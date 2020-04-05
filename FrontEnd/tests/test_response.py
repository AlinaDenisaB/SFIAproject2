from application import app
import unittest
from flask import abort, url_for
from flask_testing import TestCase
import app
import requests
from unittest import mock

def getRequest(*args, **kwargs):
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data

    if args[0] =='http://51.104.244.89:5004/passGen1':
        return MockResponse({"PasswordGenerator":"DF340sjkd?@oi"}, 200)

class TestFrontEnd(unittest.TestCase):
    @mock.patch('requests.get', side_effect=getRequest)
    def test_passGen1(self, mock_get):
        response=requests.get('http://51.104.244.89:5004/passGen1').json()
        self.assertEqual(response, {"PasswordGenerator":"DF340sjkd?@oi"})

if __name__ == '__main__':
	unittest.main()
