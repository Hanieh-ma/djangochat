from django.test import TestCase
from django.test import Client
from users.models import Users



class CreateUserTest(TestCase):

    def test_valid_signup(self):
        c = Client()
        response = c.post(
            '/users/item/',
            {
                'first_name': 'john',
                'last_name': 'smith',
                'number_of_friends': 10,
                'birthday': '2019-06-01'
            }
        )
        self.assertEqual(response.status_code, 200)

        u = Users.objects.get(first_name='john')
        self.assertEqual(u.last_name, 'smith')

    def test_invalid_signup(self):
        c = Client()
        response = c.post(
            '/users/item/',
            {
                'first_name': 'john',
                'last_name': 'smith',
                'number_of_friends': -10
            }
        )
        self.assertEqual(response.status_code, 400)
