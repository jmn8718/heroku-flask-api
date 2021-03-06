import unittest
import json

from app import app


class StatusTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_healt_get_successful(self):
        response = self.app.get('/')

        self.assertEqual(bool, type(response.json['status']))
        self.assertEqual(True, response.json['status'])
        self.assertEqual(200, response.status_code)
