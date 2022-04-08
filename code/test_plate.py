import unittest
import json
from app import app, db


class TestPlate(unittest.TestCase):

    def setUp(self):
        self.ctx = app.app_context()
        self.db = db
        self.db.init_app(app)
        self.ctx.push()
        self.client = app.test_client()

    def tearDown(self):
        self.ctx.pop()

    def test_valid_plate(self):
        payload = json.dumps({
            "plate": "XXX-X2123",
            "owner": "Max"
        })

        # When
        response = self.client.post('/plate', headers={"Content-Type": "application/json"}, data=payload)
        # Then
        self.assertEqual("Plate is valid", response.json['message'])
        self.assertEqual(200, response.status_code)

    def test_invalid_plate_starts_with_zero(self):
        payload = json.dumps({
            "plate": "XXX-X0123",
            "owner": "Max"
        })

        # When
        response = self.client.post('/plate', headers={"Content-Type": "application/json"}, data=payload)
        # Then
        self.assertEqual("Plate is invalid", response.json['message'])
        self.assertEqual(422, response.status_code)

    def test_request_without_plate(self):
        payload = json.dumps({
            "owner": "Jedi"
        })

        # When
        response = self.client.post('/plate', headers={"Content-Type": "application/json"}, data=payload)
        # Then
        self.assertEqual("Request body should have plate field.", response.json['message'])
        self.assertEqual(400, response.status_code)