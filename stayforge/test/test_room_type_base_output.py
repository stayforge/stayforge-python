# coding: utf-8

"""
    Stayforge API

    ![Commit Activity](https://img.shields.io/github/commit-activity/m/tokujun-t/stayforge) ![Codecov](https://codecov.io/gh/tokujun-t/stayforge/branch/main/graph/badge.svg) ![PyPI Version](https://img.shields.io/pypi/v/stayforge)  ### SDK  - [Python SDK](https://github.com/tokujun-t/stayforge-python)  We provided SDKs (currently only the Python version is provided). Before deciding to call the API directly, you may wish to try the SDK to speed up your development.  ![GitHub Workflow Status](https://github.com/tokujun-t/Stayforge/actions/workflows/python-sdk.yml/badge.svg)   ### About Healthcheck  Healthcheck at `/api/healthcheck`. curl to check if the service is working.  ```shell curl -I http://<your service>/api/healthcheck ``` ### Some Links  GitHub Repo [https://github.com/tokujun-t/Stayforge](https://github.com/tokujun-t/Stayforge)  Wiki [https://github.com/tokujun-t/Stayforge/wiki](https://github.com/tokujun-t/Stayforge/wiki) 

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from stayforge.models.room_type_base_output import RoomTypeBaseOutput

class TestRoomTypeBaseOutput(unittest.TestCase):
    """RoomTypeBaseOutput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RoomTypeBaseOutput:
        """Test RoomTypeBaseOutput
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RoomTypeBaseOutput`
        """
        model = RoomTypeBaseOutput()
        if include_optional:
            return RoomTypeBaseOutput(
                parent = '',
                name = '',
                name_visible = '',
                description = '',
                branch = [
                    ''
                    ],
                base_price = '',
                price_policy = '',
                min_usage = 1.337,
                max_usage = 1.337,
                allow_extension = True
            )
        else:
            return RoomTypeBaseOutput(
                name = '',
                name_visible = '',
                base_price = '',
                min_usage = 1.337,
                max_usage = 1.337,
        )
        """

    def testRoomTypeBaseOutput(self):
        """Test RoomTypeBaseOutput"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
