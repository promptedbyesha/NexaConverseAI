import unittest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

class TestEndToEnd(unittest.TestCase):
    def test_root(self):
        response = client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Welcome", response.json().get("message", ""))

    def test_chat_endpoint(self):
        response = client.post("/chat", params={"user_input": "Hello"})
        self.assertEqual(response.status_code, 200)
        self.assertIn("help", response.json().get("response", "").lower())

if __name__ == "__main__":
    unittest.main()