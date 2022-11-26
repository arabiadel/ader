from django.test import SimpleTestCase
from django.urls import reverse 

class HomePageTest(SimpleTestCase):
    def test_url_exist_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)


    def test_url_exist_if_by_name(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

class AboutPageTest(SimpleTestCase):
    def test_url_exist_at_correct_location(self):
        response = self.client.get("/about/")
        self.assertEquals(response.status_code, 200)


    def test_url_exist_if_by_name(self):
        response = self.client.get(reverse("about"))
        self.assertEquals(response.status_code, 200)