import datetime

from django.urls import reverse
from django.test import TestCase
from django.test.client import Client

from faker import Faker

from students.models import Student, Group


fake = Faker()


class BaseTest(TestCase):
    """ This is the Base test class:
    """
    def setUp(self):
        super(BaseTest, self).setUp()
        self.email = 'email@email.email'
        self.phone = '123456789'
        Student.objects.create(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            birth_date=fake.simple_profile(sex=None).get('birthdate'),
            email=self.email,
            phone=self.phone,
            address=fake.simple_profile(sex=None).get('address'))
        Group.objects.create(number=111)


class CommonTest(TestCase):
    """ This test checking next test cases:
    1. Check render home page
    2. Check render contact page
    """

    def test_visit_home_page(self):
        """ 1. Check render home page
        """
        url = reverse('home_page')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_visit_contact_page(self):
        """ 2. Check render contact page
        """
        url = reverse('contact')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


class StudentTest(BaseTest):
    """ This test checking next test cases:
    1. Check render random student page
    2. Check render students list page
    3. Check render add student page
    4. Create new student
    5. Create new student with incorrect data
    6. Delete student
    7. Create edit student
    8. Create new student by incorrect data
    9. Create new student with not unique email
    10. Create new student with not unique phone
    """

    @classmethod
    def setUpClass(cls):
        super(StudentTest, cls).setUpClass()
        cls.client = Client()
        Group.objects.create(number=111)
        cls.post_data = {
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
            'birth_date': datetime.date.today(),
            'email': fake.email(),
            'group': Group.objects.last().id,
            'phone': fake.phone_number(),
            }
        cls.incorrect_post_data = {
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
            'birth_date': datetime.date.today(),
            'email': 'New_email@gma',
            'group': Group.objects.last().id,
            'phone': fake.phone_number(),
            }

    def setUp(self):
        super(StudentTest, self).setUp()
        self.before = Student.objects.count()

    def test_visit_get_random_student_page(self):
        """ 1. Check render random student page
        """
        url = reverse('get_student')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_visit_get_students_list_page(self):
        """ 2. Check render students list page
        """
        url = reverse('get_students')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_visit_add_student_page(self):
        """ 3. Check render add student page
        """
        url = reverse('student_add')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_add_new_student(self):
        """4. Create new student
        """
        url = reverse('student_add')
        response = self.client.post(url, self.post_data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.before + 1, Student.objects.count())

    def test_add_new_student_with_incorrect_data(self):
        """5. Create new student with incorrect data
        """
        url = reverse('student_add')
        response = self.client.post(url, self.incorrect_post_data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue('Enter a valid email address.' in str(response.content))
        self.assertEqual(self.before, Student.objects.count())

    def test_delete_student(self):
        """6. Delete student
        """
        url = reverse('student_delete', args=[Student.objects.last().id])
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.before-1, Student.objects.count())

    def test_edit_student(self):
        """7. Create edit student
        """
        url = reverse('student_edit', args=[Student.objects.last().id])
        response = self.client.post(url, self.post_data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.before, Student.objects.count())

    def test_edit_student_by_incorrect_data(self):
        """8. Create new student by incorrect data
        """
        url = reverse('student_edit', args=[Student.objects.last().id])
        response = self.client.post(url, self.incorrect_post_data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue('Enter a valid email address.' in str(response.content))
        self.assertEqual(self.before, Student.objects.count())

    def test_unique_email(self):
        """9. Create new student with not unique email
        """
        url = reverse('student_add')
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
        self.assertEqual(self.before, Student.objects.count())

    def test_unique_phone(self):
        """10. Create new student with not unique phone
        """
        url = reverse('student_add')
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
        self.assertTrue(f'{self.phone} is already used!' in str(response.content))
        self.assertEqual(self.before, Student.objects.count())

    def test_invalid_phone(self):
        """11. Create new student with invalid phone
        """
        url = reverse('student_add')
        phone = '+38(097)-123-456-789'
        post_data = {
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
            'birth_date': fake.simple_profile(sex=None).get('birthdate'),
            'email': fake.email(),
            'phone': phone,
            'address': fake.simple_profile(sex=None).get('address')
        }
        response = self.client.post(url, post_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.before+1, Student.objects.count())
        self.assertEqual(''.join([n for n in phone if n.isdigit()]), Student.objects.last().phone)


class GroupTest(BaseTest):
    """ This test checking next test cases:
    1. Check render random group page
    2. Check render groups list page
    3. Check render add group page
    4. Create new student
    5. Create new group with incorrect data
    6. Delete group
    """

    def setUp(self):
        super(GroupTest, self).setUp()
        self.before = Group.objects.count()

    def test_visit_get_random_group_page(self):
        """ 1. Check render random group page
        """
        url = reverse('get_group')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_visit_get_groups_list_page(self):
        """ 2. Check render groups list page
        """
        url = reverse('get_groups')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_visit_add_group_page(self):
        """ 3. Check render add group page
        """
        url = reverse('group_add')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_add_new_group(self):
        """4. Create new student
        """
        url = reverse('group_add')
        post_data = {
            'number': 913,
            'created_year': 2017,
            'department': 3,
            'specialty_number': 913,
            'specialty_name': 'IT',
            'head_student': Student.objects.last().id
            }
        response = self.client.post(url, post_data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.before+1, Group.objects.count())

    def test_add_new_group_with_incorrect_data(self):
        """5. Create new group with incorrect data
        """
        url = reverse('group_add')
        incorrect_post_data = {
            'number': 'Some_string',
            'created_year': 2017,
            'department': 3,
            'specialty_number': 913,
            'specialty_name': 'IT',
            'head_student': Student.objects.last().id
            }
        response = self.client.post(url, incorrect_post_data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue('Enter a whole number.' in str(response.content))
        self.assertEqual(self.before, Group.objects.count())

    def test_delete_group(self):
        """6. Delete group
        """
        url = reverse('group_delete', args=[Group.objects.last().id])
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.before-1, Group.objects.count())
