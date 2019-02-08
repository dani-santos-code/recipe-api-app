from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):
    # A setup function is run before any other tests
    # Here we need to make sure the Client is logged in
    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@admin.com',
            password='pass123'
        )
        self.client.force_login(self.admin_user)
        # the force_login is a helper function that
        # allows us to log the user with django auth
        # without having to do so manually
        self.user = get_user_model().objects.create_user(
            email='anotheruser@regular.com',
            password='pass123',
            name='Test Name'
        )

    def test_users_listed(self):
        """Test that users are listed on User page"""
        url = reverse('admin:core_user_changelist')

        """ this url is defined in the Django Admin documentation.
        It generates the url for our List User page.
        Reverse is used because if you ever change the url
        in the future, you don't need to change your tests,
        since reverse takes care of updating that for you"""

        res = self.client.get(url)
        # res is response
        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

        # assertContains checks that http response was 200
        # it also checks the contents of the page

    def test_user_change_page(self):
        """Test that user edit page works"""
        url = reverse('admin:core_user_change', args=[self.user.id])
        # /admin/core/user/user_id
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_create_user_page(self):
        """Test that the create page works"""
        url = reverse('admin:core_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
