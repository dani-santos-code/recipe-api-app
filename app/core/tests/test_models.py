from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        email = 'dani@berlin.com'
        password = 'password123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password, password)

        """Note that password in encrypted.
        The check_password is a helper function that comes with the
        Django User Model. And it returns True if
        the password is correct and False if it's incorrect.
        """

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        email = 'dani@BERLIN.COM'
        user = get_user_model().objects.create_user(email, 'pass123')
        # since the password has already been tested,
        # we just pass in a random string here
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'pass123')

    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'dani@berlin.com',
            'pass123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
