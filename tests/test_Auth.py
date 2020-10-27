import unittest
import json

from app import app


class AuthTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_successful_authentication(self):
        payload = json.dumps({
            "username": "tester01",
            "password": "testerPass"
        })

        response = self.app.post(
            '/auth', headers={"Content-Type": "application/json"}, data=payload)

        self.assertEqual(str, type(response.json['access_token']))
        self.assertEqual(200, response.status_code)

    def test_fail_authentication_missing_username(self):
        payload = json.dumps({
            "email": "tester01@test.test",
            "password": "testerPass"
        })

        response = self.app.post(
            '/auth', headers={"Content-Type": "application/json"}, data=payload)

        self.assertEqual(400, response.status_code)
        self.assertEqual(str, type(response.json['message']['username']))
        self.assertEqual('Username is missing',
                         response.json['message']['username'])

    def test_fail_authentication_missing_password(self):
        payload = json.dumps({
            "username": "tester01@test.test"
        })

        response = self.app.post(
            '/auth', headers={"Content-Type": "application/json"}, data=payload)

        self.assertEqual(400, response.status_code)
        self.assertEqual(str, type(response.json['message']['password']))
        self.assertEqual('Password is missing',
                         response.json['message']['password'])
