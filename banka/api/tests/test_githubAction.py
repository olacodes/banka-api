from rest_framework.test import APITestCase


class TestGithubAction(APITestCase):
    def test_github_actions(self):
        self.assertEqual(2 + 2, 4)

    def test_github_action(self):
        self.assertFalse(not True)