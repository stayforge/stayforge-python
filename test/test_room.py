# coding: utf-8

"""
    Stayforge API

    This is a basic API description.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from stayforge.models.room import Room

class TestRoom(unittest.TestCase):
    """Room unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Room:
        """Test Room
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Room`
        """
        model = Room()
        if include_optional:
            return Room(
                id = '674f7fd50baf7c4f8c450f5b',
                create_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                update_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                key_id = '674f7fd60baf7c4f8c450f5e',
                room_type_id = '674f7fd60baf7c4f8c450f5f',
                number = '',
                priority = 56
            )
        else:
            return Room(
                create_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                number = '',
                priority = 56,
        )
        """

    def testRoom(self):
        """Test Room"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
