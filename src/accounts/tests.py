from django.contrib.auth import get_user_model
from django.test import TestCase

class CustomUserTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        
        user = User.objects.create_user(
            username = 'example',
            email    = 'example@email.com',
            password = 'examplepass'
        )

        self.assertEqual(user.username,'example')
        self.assertEqual(user.email,'example@email.com')
        self.assertTrue(user.check_password('examplepass'),True)
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
    
    def test_create_superuser(self):
        User = get_user_model()

        superuser = User.objects.create_superuser(
            username = 'superexample',
            email    = 'superexample@email.com',
            password = 'superexamplepass'
        )

        self.assertEqual(superuser.username,'superexample')
        self.assertEqual(superuser.email,'superexample@email.com')
        self.assertTrue(superuser.check_password('superexamplepass'),True)
        self.assertTrue(superuser.is_active)
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_superuser)



