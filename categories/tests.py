from rest_framework import test
from django.urls import reverse
from datetime import datetime


class CategoriesAPITest(test.APITestCase):
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

    def test_categories_list_returns__successfully(self):
        # 200 = Ok
        list_url = reverse('categories:categories-api-list')
        response = self.client.get(list_url)
        self.assertEqual(response.status_code, 200)

    def test_category_create_returns_successfully(self):
        # 201 = Created
        response = self.make_category()
        self.assertEqual(response.status_code, 201)

    def test_category_detail_returns_successfully(self):
        # 200 = Ok
        self.make_category()
        detail_url = reverse(
            'categories:categories-api-detail',
            kwargs={'pk': 1},
        )
        response = self.client.get(detail_url)
        self.assertEqual(response.status_code, 200)

    def test_category_partial_update_returns_successfully(self):
        # 200 = Ok
        self.make_category()
        update_data = {
            'name': 'Lore Updated',
        }
        patch_url = reverse(
            'categories:categories-api-detail',
            kwargs={'pk': 1},
        )
        response = self.client.patch(
            patch_url,
            data=update_data,
        )
        self.assertEqual(response.status_code, 200)

    def test_category_delete_return_successfully(self):
        # 204 = No Content
        self.make_category()
        delete_url = reverse(
            'categories:categories-api-detail',
            kwargs={'pk': 1},
        )
        response = self.client.delete(delete_url)
        self.assertEqual(response.status_code, 204)
