from rest_framework.test import APITestCase
from users.models import User

class TestUserModel(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
        first_name="dorcas",
        last_name="oloo",
        username="dorcas",
        email="oloodorcas@gmail.com",
        password="teddy@123")

        self.superuser = User.objects.create_superuser(
            first_name = "mitchell",
            last_name = "oloo",
            username = "mitchy",
            email = "oloomitchel@gmail.com",
            password = "teddy@123"
        )


    def test_create_user(self):
        self.assertIsInstance(self.user, User)
        self.assertFalse(self.user.is_staff)
        self.assertEqual(self.user.email, "oloodorcas@gmail.com")


    def test_create_super_user(self):
        self.assertIsInstance(self.superuser, User)
        self.assertTrue(self.superuser.is_staff)
        self.assertEqual(self.superuser.email, "oloomitchel@gmail.com")


    def test_raise_value_error_if_username_is_null(self):
        self.assertRaises(ValueError, User.objects.create_user,
        first_name="dorcas",
        last_name="oloo",
        username="",
        email="oloodorcas99@gmail.com",
        password="teddy@123")

    def test_raise_value_error_if_email_is_null(self):
        self.assertRaises(ValueError, User.objects.create_user,
        first_name="cara",
        last_name="oloo",
        username="potty",
        email="",
        password="teddy@123")


    def test_raise_value_error_if_is_staff_false(self):
        self.assertRaises(ValueError, User.objects.create_superuser,
        first_name="cara",
        last_name="oloo",
        username="potty",
        email="oloodorcas@gmail.com",
        password="teddy@123",
        is_staff = False
        )

    def test_raise_value_error_if_is_superuser_false(self):
        self.assertRaises(ValueError, User.objects.create_superuser,
        first_name="cara",
        last_name="oloo",
        username="potty",
        email="oloodorcas@gmail.com",
        password="teddy@123",
        is_superuser = False
        )





