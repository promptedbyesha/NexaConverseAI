import unittest
from modules import dialogue_manager

class TestDialogueManager(unittest.TestCase):
    def test_help_intent(self):
        response = dialogue_manager.handle_conversation("I need help")
        self.assertIn("assist", response)

    def test_bye_intent(self):
        response = dialogue_manager.handle_conversation("Bye")
        self.assertIn("Goodbye", response)

    def test_default_response(self):
        response = dialogue_manager.handle_conversation("Unknown query")
        self.assertIn("help", response)

if __name__ == "__main__":
    unittest.main()