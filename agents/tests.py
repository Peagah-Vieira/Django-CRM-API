from rest_framework import test
from django.urls import reverse
from datetime import datetime


class AgentsAPITest(test.APITestCase):
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
            data=agent_data,
        )

    def test_agents_list_returns__successfully(self):
        # 200 = Ok
        list_url = reverse('agents:agents-api-list')
        response = self.client.get(list_url)
        self.assertEqual(response.status_code, 200)

    def test_agent_create_returns_successfully(self):
        # 201 = Created
        response = self.make_agent()
        self.assertEqual(response.status_code, 201)

    def test_agent_detail_returns_successfully(self):
        # 200 = Ok
        self.make_agent()
        detail_url = reverse(
            'agents:agents-api-detail',
            kwargs={'pk': 1},
        )
        response = self.client.get(detail_url)
        self.assertEqual(response.status_code, 200)

    def test_agent_partial_update_returns_successfully(self):
        # 200 = Ok
        self.make_agent()
        update_data = {
            'first_name': 'Lore Updated',
        }
        patch_url = reverse(
            'agents:agents-api-detail',
            kwargs={'pk': 1},
        )
        response = self.client.patch(
            patch_url,
            data=update_data,
        )
        self.assertEqual(response.status_code, 200)

    def test_agent_delete_return_successfully(self):
        # 204 = No Content
        self.make_agent()
        delete_url = reverse(
            'agents:agents-api-detail',
            kwargs={'pk': 1},
        )
        response = self.client.delete(delete_url)
        self.assertEqual(response.status_code, 204)
