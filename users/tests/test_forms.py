from django.test import Client, TestCase

from users.forms import UserSignupForm


class UserSignupFormTests(TestCase):

    def test_signup_form_saves_names(self):
        client = Client()

        request = client.request().wsgi_request
        request.session = client.session

        form = UserSignupForm(
            data={
                "username": "alex",
                "email": "alex@test.com",
                "password1": "StrongPassword123",
                "password2": "StrongPassword123",
                "first_name": "Alex",
                "last_name": "Doe",
            }
        )

        self.assertTrue(form.is_valid())

        user = form.save(request)

        self.assertEqual(
            user.first_name,
            "Alex",
        )

        self.assertEqual(
            user.last_name,
            "Doe",
        )
