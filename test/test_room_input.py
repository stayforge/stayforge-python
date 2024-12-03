# coding: utf-8

"""
    Stayforge API

    This is a basic API description.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from stayforge.models.room_input import RoomInput

class TestRoomInput(unittest.TestCase):
    """RoomInput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RoomInput:
        """Test RoomInput
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RoomInput`
        """
        model = RoomInput()
        if include_optional:
            return RoomInput(
                key_id = '674f80b0f905e84218896391',
                room_type_id = '674f80b0f905e84218896392',
                number = '',
                priority = 56
            )
        else:
            return RoomInput(
                number = '',
                priority = 56,
        )
        """

    def testRoomInput(self):
        """Test RoomInput"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
