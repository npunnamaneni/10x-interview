"""program to test the service api"""
import unittest
import requests
import json


class TestAPI(unittest.TestCase):
    def setUp(self):
        # Define the base URL of your API
        self.base_url = 'http://127.0.0.1:5000'

    def test_query(self):
        # Define the endpoint to test
        url = f"{self.base_url}/query"
        # Make a GET request to the API endpoint
        response = requests.get(url)
        # Check the response status code
        self.assertEqual(response.status_code, 200)
        # Check that the response content is in JSON format
        self.assertTrue(response.content, 'application/json')
        # Parse the JSON response and check if data is exists
        data = json.loads(response.text)
        self.assertGreater(len(data), 0)

    def test_query_with_limit(self):
        # Define the endpoint to test
        url = f"{self.base_url}/query?limit=5"
        # Make a GET request to the API endpoint
        response = requests.get(url)
        # Check the response status code
        self.assertEqual(response.status_code, 200)
        # Check that the response content is in JSON format
        self.assertTrue(response.content, 'application/json')
        # Parse the JSON response and check if data is exists
        data = json.loads(response.text)
        self.assertGreater(len(data), 0)

    def test_query_with_date(self):
        # Define the endpoint to test
        url = f"{self.base_url}/query?date=2012-06-04"
        # Make a GET request to the API endpoint
        response = requests.get(url)
        # Check the response status code
        self.assertEqual(response.status_code, 200)
        # Check that the response content is in JSON format
        self.assertTrue(response.content, 'application/json')
        # Parse the JSON response and check if data is exists
        data = json.loads(response.text)
        self.assertGreater(len(data), 0)

    def test_query_with_weather(self):
        # Define the endpoint to test
        url = f"{self.base_url}/query?weather=rain"
        # Make a GET request to the API endpoint
        response = requests.get(url)
        # Check the response status code
        self.assertEqual(response.status_code, 200)
        # Check that the response content is in JSON format
        self.assertTrue(response.content, 'application/json')
        # Parse the JSON response and check if data is exists
        data = json.loads(response.text)
        self.assertGreater(len(data), 0)

    def test_multi_query(self):
        # Define the endpoint to test
        url = f"{self.base_url}/query?weather=rain&limit=5"
        # Make a GET request to the API endpoint
        response = requests.get(url)
        # Check the response status code
        self.assertEqual(response.status_code, 200)
        # Check that the response content is in JSON format
        self.assertTrue(response.content, 'application/json')
        # Parse the JSON response and check if data is exists
        data = json.loads(response.text)
        self.assertGreater(len(data), 0)


if __name__ == '__main__':
    unittest.main()
