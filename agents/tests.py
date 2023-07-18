from rest_framework import test
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime


class AgentsAPITest(test.APITestCase):
    def setUp(self, *args, **kwargs):
        self.user_data = {
            'username': 'admin',
            'password': 'admin',
        }
        return super().setUp(*args, **kwargs)

    def make_user(self):
        User.objects.create_user(
            username=self.user_data['username'],
            password=self.user_data['password'],
        )

    def get_jwt_refresh_token(self):
        self.make_user()
        response = self.client.post(
            reverse('token_obtain_pair'),
            data={**self.user_data}
        )

        return response.data.get('refresh')

    def get_jwt_access_token(self):
        self.make_user()
        response = self.client.post(
            reverse('token_obtain_pair'),
            data={**self.user_data}
        )

        return response.data.get('access')

    def make_agent(self):
        agent_data = {
            'first_name': 'Lore',
            'last_name': 'Ipsum',
            'email': 'loreipsum@lore.com',
            'phone_number': '22998438864',
            'created_at': datetime.now(),
            'updated_at': datetime.now(),
        }
        create_url = reverse('agents:agents-api-list')
        return self.client.post(
            create_url,
            HTTP_AUTHORIZATION=f'Bearer {self.get_jwt_access_token()}',
            data={**agent_data},
        )

    def test_unauthorized_user_cant_create(self):
        # 401 = unauthorized
        list_url = reverse('agents:agents-api-list')
        response = self.client.post(list_url)
        self.assertEqual(response.status_code, 401)

    def test_authorized_user_can_create(self):
        # 201 = created
        response = self.make_agent()
        self.assertEqual(response.status_code, 201)

    def test_unauthorized_user_cant_see_list_informations(self):
        # 401 = unauthorized
        list_url = reverse('agents:agents-api-list')
        response = self.client.get(list_url)
        self.assertEqual(response.status_code, 401)

    def test_authorized_user_can_see_list_informations(self):
        # 200 = ok
        list_url = reverse('agents:agents-api-list')
        response = self.client.get(
            list_url,
            HTTP_AUTHORIZATION=f'Bearer {self.get_jwt_access_token()}',
        )
        self.assertEqual(response.status_code, 200)

    def test_unauthorized_user_cant_see_detail_informations(self):
        # 401 = unauthorized
        detail_url = reverse('agents:agents-api-detail', kwargs={'pk': 1})
        response = self.client.get(detail_url)
        self.assertEqual(response.status_code, 401)
