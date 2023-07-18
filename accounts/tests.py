from rest_framework import test
from django.contrib.auth.models import User
from django.urls import reverse


class AccountsAPITest(test.APITestCase):
    def setUp(self, *args, **kwargs):
        self.userdata = {
            'username': 'admin',
            'password': 'admin',
        }
        return super().setUp(*args, **kwargs)

    def make_user(self):
        User.objects.create_user(
            username=self.userdata['username'],
            password=self.userdata['password'],
        )

    def get_jwt_refresh_token(self):
        self.make_user()
        response = self.client.post(
            reverse('token_obtain_pair'),
            data={**self.userdata}
        )

        return response.data.get('refresh')

    def get_jwt_access_token(self):
        self.make_user()
        response = self.client.post(
            reverse('token_obtain_pair'),
            data={**self.userdata}
        )

        return response.data.get('access')

    def test_unauthorized_user_cant_see_informations(self):
        me_url = reverse('accounts:accounts-api-me')
        response = self.client.get(me_url)
        self.assertEqual(response.status_code, 401)  # 401 = unauthorized

    def test_authorized_user_can_see_informations(self):
        me_url = reverse('accounts:accounts-api-me')
        response = self.client.get(
            me_url,
            HTTP_AUTHORIZATION=f'Bearer {self.get_jwt_access_token()}',
        )
        self.assertEqual(response.status_code, 200)
