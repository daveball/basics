from unittest import TestCase
from posts import Posts


class TestPosts(TestCase):
    def test_create_posts(self):
        p = Posts('Test', 'Test Content')
        self.assertEqual('Test', p.title)
        self.assertEqual('Test Content', p.content)

    def test_json(self):
        p = Posts('Test', 'Test Content')
        expected = {'title': 'Test', 'content': 'Test Content'}

        self.assertDictEqual(expected, p.json())
