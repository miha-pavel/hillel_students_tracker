# coding=utf-8
import json
import datetime

from django.urls import reverse
from django.test import TestCase
from django.test.client import Client

from faker import Faker

from students.models import Student, Group


fake = Faker()


class CommonTest(TestCase):
    """ This test checking next test cases:
    1. Check render home page
    2. Check render contact page
    """

    def test_visit_home_page(self):
        """ 1. Check render home page

        :param:
        :return:
        """
        url = reverse('home_page')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_visit_contact_page(self):
        """ 2. Check render contact page

        :param:
        :return:
        """
        url = reverse('contact')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


class StudentTest(TestCase):
    """ This test checking next test cases:
    1. Check render random student page
    2. Check render students list page
    3. Check render add student page
    """

    @classmethod
    def setUpClass(cls):
        super(StudentTest, cls).setUpClass()
        cls.client = Client()
        Student.objects.create(
            first_name='Test_first_name',
            last_name='Test_last_name',
            birth_date=fake.simple_profile(sex=None).get('birthdate'),
            email=fake.email(),
            phone=int(''.join([n for n in fake.phone_number() if n.isdigit()])),
            address=fake.simple_profile(sex=None).get('address'))
        Group.objects.create(number=111)
        cls.post_data = {
            'first_name': 'New_first_name',
            'last_name': 'New_last_name',
            'birth_date': datetime.date.today(),
            'email': 'New_email@gmail.com',
            'group': Group.objects.last().id,
            'phone': '2562374527'
            }
    
    def test_visit_get_random_student_page(self):
        """ 1. Check render random student page

        :param:
        :return:
        """
        url = reverse('get_student')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
    
    def test_visit_get_students_list_page(self):
        """ 2. Check render students list page

        :param:
        :return:
        """
        url = reverse('get_students')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_visit_add_student_page(self):
        """ 3. Check render add student page

        :param:
        :return:
        """
        url = reverse('student_add')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_add_new_student(self):
        """4. Create new student
        """
        before = Student.objects.count()
        url = reverse('student_add')
        response = self.client.post(url, self.post_data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(before + 1, Student.objects.count())
    
    def test_edit_student(self):
        """4. Create edit student
        """
        before = Student.objects.count()
        url = reverse('student_edit', args=[Student.objects.last().id])
        response = self.client.post(url, self.post_data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(before, Student.objects.count())


class GroupTest(TestCase):
    """ This test checking next test cases:
    1. Check render random group page
    2. Check render groups list page
    3. Check render add group page
    """
    
    def test_visit_get_random_group_page(self):
        """ 1. Check render random group page

        :param:
        :return:
        """
        url = reverse('get_group')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
    
    def test_visit_get_groups_list_page(self):
        """ 2. Check render groups list page

        :param:
        :return:
        """
        url = reverse('get_groups')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_visit_add_group_page(self):
        """ 3. Check render add group page

        :param:
        :return:
        """
        url = reverse('group_add')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

#     def test_get_taxonomy_no_uri(self):
#         """2. Check getting taxonomy json without URI params.
#         """
#         self.string_number_test_method = inspect.stack()[0][2]-3
#         self.current_test_method = inspect.stack()[0][3]
#         self.url = reverse('core-api-taxonomy')
#         self.response = self.client.get(self.url)
#         response_data = json.loads(self.response.content)
#         self.expected_status = status.HTTP_400_BAD_REQUEST
#         self.assertEqual(self.response.status_code, self.expected_status)
#         self.assertEqual(
#             response_data['vertical'][0],
#             'This field is required.')
#         self.is_test_failed = 'FALSE'

#     #TODO: This test checks view, which use Yaroslav manualy.
#     # def test_get_taxonomy_no_login(self):
#     #     """3. Check getting taxonomy json with URI params.
#     #     """
#     #     self.url = reverse('core-api-taxonomy')
#     #     self.response = self.client.get(self.url, {'vertical': 'auto'})
#     #     self.expected_status = status.HTTP_200_OK
#     #     self.assertEqual(self.response.status_code, self.expected_status)
#     #     response_data = json.loads(self.response.content)
#     #     self.assertTrue(len(response_data))
#         # self.is_test_failed = 'FALSE'

#     @unittest.skipIf(settings.LANDING_PAGE != "lp_engine_app", 'This test is for lp_engine only')
#     def test_get_channel_version(self):
#         """4. Check getting channel version.
#         """
#         self.string_number_test_method = inspect.stack()[0][2]-3
#         self.current_test_method = inspect.stack()[0][3]
#         channel = Channel.objects.first()
#         self.url = reverse('check_channel_version', args=[channel.code])
#         self.response = self.client.post(self.url)
#         self.expected_status = status.HTTP_200_OK
#         self.assertEqual(self.response.status_code, self.expected_status)
#         self.is_test_failed = 'FALSE'

#     # TODO -> problem with permission_classes = (IsAuthenticated,). ASK Yaroslav
#     # @unittest.skipIf(settings.LANDING_PAGE != "lp_engine_app", 'This test is for lp_engine only')
#     # def test_send_to_landing_page(self):
#     #     """4_1. Check send to landing page.
#     #     """
#     #     channel = Channel.objects.first()
#     #     self.url = reverse('send_to_landing_page', args=[channel.code])
#     #     self.response = self.client.post(self.url)
#     #     self.expected_status = status.HTTP_200_OK
#     #     self.assertEqual(self.response.status_code, self.expected_status)

#     # TODO -> problem with permission_classes = (IsAuthenticated,). ASK Yaroslav
#     # @unittest.skipIf(settings.LANDING_PAGE != "lp_engine_app", 'This test is for lp_engine only')
#     # def test_get_flow_data(self):
#     #     """4_2. Check getting flow data.
#     #     """
#     #     channel = Channel.objects.first()
#     #     self.url = reverse('get_flow_data', args=[channel.code])
#     #     self.response = self.client.get(self.url)
#     #     response_data = json.loads(self.response.content)
#     #     self.expected_status = status.HTTP_200_OK
#     #     self.assertEqual(self.response.status_code, self.expected_status)
#     #     self.assertTrue(len(response_data))

#     def test_checking_valid_zipcode(self):
#         """5. Check getting location by valid zipcode.
#         """
#         self.string_number_test_method = inspect.stack()[0][2]-3
#         self.current_test_method = inspect.stack()[0][3]
#         location = CoreApiConnection.get_location_info(
#             zipcode=self.valid_zipcode, use_local_cache=True)['location']
#         self.url = reverse('geo-validate-location')
#         self.response = self.client.get(self.url, {'zipcode': self.valid_zipcode})
#         self.expected_status = status.HTTP_200_OK
#         self.assertEqual(self.response.status_code, self.expected_status)
#         response_data = json.loads(self.response.content)['content']
#         for key, value in response_data.items():
#             self.assertEqual(response_data[key], location[key])
#         self.is_test_failed = 'FALSE'

#     def test_checking_invalid_zipcode(self):
#         """6. Check we could not get location by invalid zipcode.
#         """
#         self.string_number_test_method = inspect.stack()[0][2]-3
#         self.current_test_method = inspect.stack()[0][3]
#         self.url = reverse('geo-validate-location')
#         self.response = self.client.get(self.url, {'zipcode': self.invalid_zipcode})
#         self.expected_status = status.HTTP_400_BAD_REQUEST
#         self.assertEqual(self.response.status_code, self.expected_status)
#         response_data = json.loads(self.response.content)['content']
#         self.assertEqual(
#             response_data, 'Oops! This isn\'t a valid US zip code.')
#         self.is_test_failed = 'FALSE'

#     def test_checking_valid_phone(self):
#         """7. Check getting location by valid phone.
#         """
#         self.string_number_test_method = inspect.stack()[0][2]-3
#         self.current_test_method = inspect.stack()[0][3]
#         phone_type = CoreApiConnection.get_phone_type(
#             phone_number=self.valid_phone, use_local_cache=True)['result']
#         self.url = reverse('generic-phone-type')
#         self.response = self.client.get(self.url, {'phone_number': self.valid_phone})
#         self.expected_status = status.HTTP_200_OK
#         response_data = json.loads(self.response.content)['content']
#         self.assertEqual(self.response.status_code, self.expected_status)
#         for key, value in response_data.items():
#             self.assertEqual(response_data[key], phone_type[key])
#         self.is_test_failed = 'FALSE'

#     def test_checking_invalid_phone(self):
#         """8. Check validation phone (phone is invalid).
#         """
#         self.string_number_test_method = inspect.stack()[0][2]-3
#         self.current_test_method = inspect.stack()[0][3]
#         self.url = reverse('generic-phone-type')
#         self.response = self.client.get(self.url, {'phone_number': self.invalid_phone})
#         response_data = json.loads(self.response.content)
#         self.expected_status = status.HTTP_400_BAD_REQUEST
#         self.assertEqual(self.response.status_code, self.expected_status)
#         self.assertEqual(
#             response_data['phone_number'][0], 'Ensure this field has at least 10 characters.')
#         self.is_test_failed = 'FALSE'

#     def test_submit_category_subcategory(self):
#         """9. Check submit category an subcategory with valid zipcode.
#         """
#         self.string_number_test_method = inspect.stack()[0][2]-3
#         self.current_test_method = inspect.stack()[0][3]
#         category, subcategory = MockCategory.get_category_with_sub_category()
#         self.url = reverse('submit-click')
#         self.post_data = {
#             'category': category,
#             'subcategory': subcategory,
#             'zipcode': self.valid_zipcode,
#         }
#         self.response = self.client.post(self.url, self.post_data)
#         response_data = json.loads(self.response.content)
#         self.expected_status = status.HTTP_200_OK
#         self.assertEqual(self.response.status_code, self.expected_status)
#         self.assertTrue(response_data['content'])
#         self.is_test_failed = 'FALSE'

#     def test_submit_with_invalid_zipcode(self):
#         """10. Check submit category an subcategory with invalid zipcode.
#         """
#         self.string_number_test_method = inspect.stack()[0][2]-3
#         self.current_test_method = inspect.stack()[0][3]
#         category, subcategory = MockCategory.get_category_with_sub_category()
#         self.url = reverse('submit-click')
#         post_data = {
#             'category': category,
#             'subcategory': subcategory,
#             'zipcode': self.not_full_zipcode,
#         }
#         self.response = self.client.post(self.url, post_data)
#         response_data = json.loads(self.response.content)
#         self.expected_status = status.HTTP_400_BAD_REQUEST
#         self.assertEqual(self.response.status_code, self.expected_status)
#         self.assertEqual(response_data['zipcode'][0],
#                          'Ensure this field has at least 5 characters.')
#         self.is_test_failed = 'FALSE'

#     def test_submit_with_incorrect_category_id(self):
#         """11. Check submit category an subcategory with incorrect category id.
#         """
#         self.string_number_test_method = inspect.stack()[0][2]-3
#         self.current_test_method = inspect.stack()[0][3]
#         category, subcategory = MockCategory.get_category_with_sub_category()
#         self.url = reverse('submit-click')
#         post_data = {
#             'category': 'Incorrect_ID',
#             'subcategory': subcategory,
#             'zipcode': self.valid_zipcode,
#         }
#         self.response = self.client.post(self.url, post_data)
#         response_data = json.loads(self.response.content)
#         self.expected_status = status.HTTP_400_BAD_REQUEST
#         self.assertEqual(self.response.status_code, self.expected_status)
#         self.assertEqual(response_data['content'][0],
#                          'Incorrect category and subcategory IDs')
#         self.is_test_failed = 'FALSE'

#     # TODO -> This test failed. We should fix serializer
#     # def test_no_submit_with_incorrect_subcategory_id(self):
#     #     """12. Check we can not submit category an subcategory with incorrect subcategory id.
#     #     """
#     #     category, subcategory = MockCategory.get_category_with_sub_category()
#     #     self.url = reverse('submit-click')
#     #     post_data = {
#     #         'category': category,
#     #         'subcategory': 'Incorrect_ID',
#     #         'zipcode': self.valid_zipcode,
#     #     }
#     #     self.response = self.client.post(self.url, post_data)
#     #     response_data = json.loads(self.response.content)
#         # self.expected_status = status.HTTP_400_BAD_REQUEST
#     #     self.assertEqual(self.response.status_code, self.expected_status)
#     #     self.assertEqual(response_data['content'][0],
#     #                      'Incorrect category and subcategory IDs')

# # TODO -> delete after "api/v1/check-phone' will be deleted
# # class CheckPhonePrefixTest(TestCase):
# #     def setUp(self):
# #         self.phone_prefixes = {
# #             MockPhoneNumberPrefix.get_valid_phone_prefix(): status.HTTP_200_OK,
# #             None: status.HTTP_400_BAD_REQUEST,
# #             '2012011': status.HTTP_400_BAD_REQUEST,
# #             False: status.HTTP_400_BAD_REQUEST,
# #             MockPhoneNumberPrefix.get_valid_phone_prefix(): status.HTTP_200_OK
# #         }
# #
# #     def test_check_phone(self):
# #         for phone_prefix, response_status in self.phone_prefixes.items():
# #             self.response = self.client.post(reverse('check-phone'), data={'phone_prefix': phone_prefix})
# #             print(response)
# #             if self.response.status_code != response_status:
# #                 print(phone_prefix, response_status, self.response.status_code)
# #                 print(self.response.json())
# #             self.assertEqual(self.response.status_code, response_status)

#     # def test_get_consumer_links(self):
#     #     for zip_code, response_status in self.zip_codes.items():
#     #         self.response = self.client.post(
#     #             reverse('get-consumer-links'), data={'zipcode': zip_code})
#     #         if self.response.status_code != response_status:
#     #             print(zip_code, response_status)
#     #             print(self.response.json())
#     #         self.assertEqual(self.response.status_code, response_status)

#     def test_redirect_to_home(self):
#         """13. Check redirect to home page.
#         """
#         self.string_number_test_method = inspect.stack()[0][2]-3
#         self.current_test_method = inspect.stack()[0][3]
#         self.url = reverse('home')
#         self.response = self.client.get(self.url)
#         self.expected_status = status.HTTP_200_OK
#         self.assertEqual(self.response.status_code, self.expected_status)
#         self.assertTrue(len(self.response.context))
#         self.assertTemplateUsed(self.response, 'home.html')
#         self.is_test_failed = 'FALSE'

#     def test_redirect_to_lead_form(self):
#         """14. Check redirect to lead_form page.
#         """
#         self.string_number_test_method = inspect.stack()[0][2]-3
#         self.current_test_method = inspect.stack()[0][3]
#         self.url = reverse('lead-form')
#         self.response = self.client.get(self.url)
#         self.expected_status = status.HTTP_200_OK
#         self.assertEqual(self.response.status_code, self.expected_status)
#         self.assertTrue(len(self.response.context))
#         self.assertTemplateUsed(self.response, 'lead-form.html')
#         self.is_test_failed = 'FALSE'

#     def test_api_v1_channel_questions_correct_category(self):
#         """15. Check geting channel question correct category.
#         """
#         self.string_number_test_method = inspect.stack()[0][2]-3
#         self.current_test_method = inspect.stack()[0][3]
#         category, subcategory = MockCategory.get_category_with_sub_category()
#         query_dictionary = QueryDict('', mutable=True)
#         query_dictionary.update(
#             {
#                 'category': category,
#                 'subcategory': subcategory,
#             }
#         )
#         self.url = '%s?%s' % (reverse('api-v1-channel-questions'),
#                          query_dictionary.urlencode())
#         self.response = self.client.get(self.url)
#         response_data = json.loads(self.response.content)
#         self.expected_status = status.HTTP_200_OK
#         self.assertEqual(self.response.status_code, self.expected_status)
#         self.assertNotEqual(len(response_data), 0)
#         self.is_test_failed = 'FALSE'

#     #TODO: Test is failed. We should fix serializer and model
#     # def test_api_v1_channel_questions_incorrect_category(self):
#     #     """16. Check geting channel question incorrect category.
#     #     """
#     #     self.url = reverse('api-v1-channel-questions')+'?category=0'
#     #     self.response = self.client.get(self.url)
#         # self.expected_status = status.HTTP_404_NOT_FOUND
#     #     self.assertEqual(self.response.status_code, self.expected_status)
#     #     response_data = json.loads(self.response.content)
#     #     self.assertEqual(len(response_data), 0)
#     def test_api_v1_category(self):
#         """16. Check getting category data.
#         """
#         self.string_number_test_method = inspect.stack()[0][2]-3
#         self.current_test_method = inspect.stack()[0][3]
#         channel = Channel.objects.first()
#         category = Channel.objects.select_related('taxonomy', 'parent').filter(level=1, parent=channel).first()
#         self.url = reverse('api-v1-category', args=[category.id])
#         self.response = self.client.get(self.url)
#         import ipdb; ipdb.set_trace()
#         self.expected_status = status.HTTP_200_OK
#         self.assertEqual(self.response.status_code, self.expected_status)
#         self.is_test_failed = 'FALSE'
