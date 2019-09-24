from django.test import TestCase, SimpleTestCase

#TestCase is used for testing when databases are involved
#SimpleTestCase can be used when there are no databases involved

# Create your tests here.
#These tests simply test whether or not the webpages exist.

class SimpleTests(SimpleTestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    
    def test_about_page_status_code(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)
