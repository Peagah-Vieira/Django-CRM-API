from rest_framework import test
from django.urls import reverse
from datetime import datetime


class LeadsAPITest(test.APITestCase):
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

    def make_category(self):
        category_data = {
            'name': 'Lore Ipsum',
            'description': 'Help-me',
            'created_at': datetime.now(),
            'updated_at': datetime.now(),
        }
        create_url = reverse('categories:categories-api-list')

        return self.client.post(
            create_url,
            data=category_data,
        )

    def make_lead(self):
        self.make_category()
        self.make_agent()
        lead_data = {
            'first_name': 'Lore',
            'last_name': 'Impsum',
            'email': 'loreimpsum@lore.com',
            'age': 20,
            'category': 1,
            'agent': 1,
            'created_at': datetime.now(),
            'updated_at': datetime.now(),
        }
        create_url = reverse('leads:leads-api-list')

        return self.client.post(
            create_url,
            data=lead_data,
        )

    def test_leads_list_returns__successfully(self):
        # 200 = Ok
        list_url = reverse('leads:leads-api-list')
        response = self.client.get(list_url)
        self.assertEqual(response.status_code, 200)

    def test_lead_create_returns__successfully(self):
        # 201 = Created
        response = self.make_lead()
        self.assertEqual(response.status_code, 201)

    def test_lead_detail_returns_successfully(self):
        # 200 = Ok
        self.make_lead()
        detail_url = reverse(
            'leads:leads-api-detail',
            kwargs={'pk': 1},
        )
        response = self.client.get(detail_url)
        self.assertEqual(response.status_code, 200)

    def test_lead_partial_update_returns_successfully(self):
        # 200 = Ok
        self.make_lead()
        update_data = {
            'first_name': 'Lore Updated',
        }
        patch_url = reverse(
            'leads:leads-api-detail',
            kwargs={'pk': 1},
        )
        response = self.client.patch(
            patch_url,
            data=update_data,
        )
        self.assertEqual(response.status_code, 200)

    def test_lead_delete_return_successfully(self):
        # 204 = No Content
        self.make_lead()
        delete_url = reverse(
            'leads:leads-api-detail',
            kwargs={'pk': 1},
        )
        response = self.client.delete(delete_url)
        self.assertEqual(response.status_code, 204)
