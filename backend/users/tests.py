from typing import override
from django_tenants.utils import tenant_context
from rest_framework import status
from django_tenants.test.cases import TenantTestCase
from django_tenants.test.client import TenantClient, TenantRequestFactory
from rest_framework.test import force_authenticate

from schoolERPCode.setup_tests import create_test_superuser
from tenants.models import School
from users.models import User


from django_tenants.test.cases import TenantTestCase

from users.views import CreateUser


class UserTests(TenantTestCase):
    @override
    def setUp(self):
        super().setUp()
        self.factory = TenantRequestFactory(self.tenant)
        self.client = TenantClient(self.tenant)
        self.superuser = create_test_superuser()

    def test_create_account(self):
        """
        Ensure we can create a new account object.
        """

        prev_count = User.objects.count()
        url = "/api/users/create/"
        data = {
            "email": "test_man@testemail.com",
            "username": "testman",
            "first_name": "Test",
            "last_name": "Man",
            "password": "test_password",
        }
        request = self.factory.post(url, data, format="json")
        force_authenticate(request, user=self.superuser)
        response = CreateUser.as_view()(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.data)
        self.assertEqual(User.objects.count(), prev_count+ 1)
        self.assertEqual(User.objects.latest("id").full_name, "Test Man")
