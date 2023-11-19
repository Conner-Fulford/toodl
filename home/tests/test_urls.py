"""Import necessary components for test cases"""
from django.test import TestCase
from django.urls import reverse, resolve
from home.views import calendar, login_page, logout_view, register, index


class TestUrls(TestCase):
    """Class containing the tests for each url in urls.py"""

    def test_login(self):
        url = reverse("login")
        print(resolve(url))
        self.assertEqual(resolve(url).func, login_page)

    def test_logout(self):
        url = reverse("logout")
        print(resolve(url))
        self.assertEqual(resolve(url).func, logout_view)

    def test_register(self):
        url = reverse("register")
        print(resolve(url))
        self.assertEqual(resolve(url).func, register)

    def test_calendar(self):
        url = reverse("calendar")
        print(resolve(url))
        self.assertEqual(resolve(url).func, calendar)

    def test_index(self):
        url = reverse("index")
        print(resolve(url))
        self.assertEqual(resolve(url).func, index)
