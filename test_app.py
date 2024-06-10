import unittest
from app import app

class StoryGenerationTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_index(self):
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)
        self.assertIn(b"story-generation-api", result.data)

    def test_generate_story_success(self):
        result = self.app.post('/generate_story', json={'prompt': 'Era uma vez em um reino distante...'})
        self.assertEqual(result.status_code, 200)
        self.assertIn('story', result.get_json())

    def test_generate_story_no_prompt(self):
        result = self.app.post('/generate_story', json={})
        self.assertEqual(result.status_code, 400)
        self.assertIn('error', result.get_json())

if __name__ == '__main__':
    unittest.main()


