from django.test import TestCase
from home.models import CustomUser


class CustomUserTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        CustomUser.objects.create(
            username="testcase", email="testcase@testcase.com", password="testcase123!"
        )

    def test_username(self):
        customuser = CustomUser.objects.get(id=1)
        field_label = customuser._meta.get_field("username").verbose_name
        print(field_label)
        self.assertEqual(field_label, "username")

    def test_email(self):
        customuser = CustomUser.objects.get(id=1)
        field_label = customuser._meta.get_field("email").verbose_name
        print(field_label)
        self.assertEqual(field_label, "email")

    def test_password(self):
        customeruser = CustomUser.objects.get(id=1)
        field_label = customeruser._meta.get_field("password").verbose_name
        print(field_label)
        self.assertEqual(field_label, "password")
