import unittest
from modules import intent_recognition

class TestIntentRecognition(unittest.TestCase):
    def test_greeting(self):
        # Should return "greeting" for a greeting input
        self.assertEqual(intent_recognition.recognize_intent("Hello there!"), "greeting")

    def test_goodbye(self):
        # Should return "goodbye" for a goodbye input
        self.assertEqual(intent_recognition.recognize_intent("Bye now"), "goodbye")

    def test_order_status(self):
        # Should match "Track my order"
        self.assertEqual(intent_recognition.recognize_intent("Track my order"), "order_status")

    def test_unknown(self):
        # For random input, should return "unknown"
        self.assertEqual(intent_recognition.recognize_intent("This should not match"), "unknown")

if __name__ == "__main__":
    unittest.main()
