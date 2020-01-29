import datetime

from django.urls import reverse
from django.test import TestCase
from django.test.client import Client

from faker import Faker

from teachers.models import Teacher

fake = Faker()


class TeacherTest(TestCase):
    """ This test checking next test cases:
    1. Check render random teacher page
    2. Check render teachers list page
    3. Check render add teacher page
    4. Create new teacher
    5. Create new teacher with incorrect data
    6. Delete teacher
    7. Create edit teacher
    8. Create new teacher by incorrect data
    9. Create new teacher with not unique email
    10. Create new teacher with not unique phone
    """

    @classmethod
    def setUpClass(cls):
        super(TeacherTest, cls).setUpClass()
        cls.client = Client()
        cls.post_data = {
            'first_name': 'New_first_name',
            'last_name': 'New_last_name',
            'birth_date': datetime.date.today(),
            'email': 'New_email@gmail.com',
            'phone': '2562374527'
            }
        cls.incorrect_post_data = {
            'first_name': 'New_first_name',
            'last_name': 'New_last_name',
            'birth_date': datetime.date.today(),
            'email': 'New_email@gma',
            'phone': '2562374527'
            }

    def setUp(self):
        super(TeacherTest, self).setUp()
        self.email = 'email@email.email'
        self.phone = '123456789'
        Teacher.objects.create(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            birth_date=fake.simple_profile(sex=None).get('birthdate'),
            email=self.email,
            phone=self.phone,
            address=fake.simple_profile(sex=None).get('address'))
        self.before = Teacher.objects.count()

    def test_visit_get_random_teacher_page(self):
        """ 1. Check render random teacher page
        """
        url = reverse('get_teacher')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_visit_get_teachers_list_page(self):
        """ 2. Check render teachers list page
        """
        url = reverse('get_teachers')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_visit_add_teacher_page(self):
        """ 3. Check render add teacher page
        """
        url = reverse('teacher_add')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_add_new_teacher(self):
        """4. Create new teacher
        """
        url = reverse('teacher_add')
        response = self.client.post(url, self.post_data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.before + 1, Teacher.objects.count())

    def test_add_new_teacher_with_incorrect_data(self):
        """5. Create new teacher with incorrect data
        """
        url = reverse('teacher_add')
        response = self.client.post(url, self.incorrect_post_data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue('Enter a valid email address.' in str(response.content))
        self.assertEqual(self.before, Teacher.objects.count())

    def test_deletet_teacher(self):
        """6. Deletet_teacher
        """
        url = reverse('teacher_delete', args=[Teacher.objects.last().id])
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.before-1, Teacher.objects.count())

    def test_edit_teacher(self):
        """7. Create edit teacher
        """
        url = reverse('teacher_edit', args=[Teacher.objects.last().id])
        response = self.client.post(url, self.post_data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.before, Teacher.objects.count())

    def test_edit_teacher_by_incorrect_data(self):
        """8. Create new teacher by incorrect data
        """
        url = reverse('teacher_edit', args=[Teacher.objects.last().id])
        response = self.client.post(url, self.incorrect_post_data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue('Enter a valid email address.' in str(response.content))
        self.assertEqual(self.before, Teacher.objects.count())

    def test_unique_email(self):
        """9. Create new teacher with not unique email
        """
        url = reverse('teacher_add')
        post_data = {
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
            'birth_date': fake.simple_profile(sex=None).get('birthdate'),
            'email': self.email,
            'phone': int(''.join([n for n in fake.phone_number() if n.isdigit()])),
            'address': fake.simple_profile(sex=None).get('address')
        }
        response = self.client.post(url, post_data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(f'{self.email} is already used!' in str(response.content))
        self.assertEqual(self.before, Teacher.objects.count())

    def test_unique_phone(self):
        """10. Create new teacher with not unique phone
        """
        url = reverse('teacher_add')
        post_data = {
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
            'birth_date': fake.simple_profile(sex=None).get('birthdate'),
            'email': fake.email(),
            'phone': self.phone,
            'address': fake.simple_profile(sex=None).get('address')
        }
        response = self.client.post(url, post_data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue('Teacher with this Phone already exists.' in str(response.content))
        self.assertEqual(self.before, Teacher.objects.count())
