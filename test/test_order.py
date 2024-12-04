# coding: utf-8

"""
    Stayforge API

    ![Commit Activity](https://img.shields.io/github/commit-activity/m/tokujun-t/stayforge) ![Codecov](https://codecov.io/gh/tokujun-t/stayforge/branch/main/graph/badge.svg) ![PyPI Version](https://img.shields.io/pypi/v/stayforge) ![PyPI Downloads](https://img.shields.io/pypi/dm/stayforge) ![GitHub Workflow Status](https://github.com/tokujun-t/Stayforge/actions/workflows/python-sdk.yml/badge.svg) 

    The version of the OpenAPI document: 1.0.0
    Contact: support@stayforge.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from stayforge.models.order import Order

class TestOrder(unittest.TestCase):
    """Order unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Order:
        """Test Order
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Order`
        """
        model = Order()
        if include_optional:
            return Order(
                id = '67501c3e268f832449a2ed5d',
                create_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                update_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                num = '',
                room_id = '',
                guest = stayforge.models.guest.Guest(
                    first_name = '', 
                    middle_name = '', 
                    last_name = '', 
                    gender = '', 
                    birthday = '', 
                    nationality = '', 
                    email = '', 
                    phone_number = '', 
                    address = '', 
                    occupation = '', 
                    passport_number = '', 
                    id_document = stayforge.models.id_document.IDDocument(
                        mrz = '', 
                        photocopy = null, ), ),
                type = '',
                scheduled_checkin_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                scheduled_checkout_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return Order(
                create_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                type = '',
        )
        """

    def testOrder(self):
        """Test Order"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
