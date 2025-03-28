# coding: utf-8

"""
    Stayforge API

    ![Commit Activity](https://img.shields.io/github/commit-activity/m/tokujun-t/stayforge) ![Codecov](https://codecov.io/gh/tokujun-t/stayforge/branch/main/graph/badge.svg) ![PyPI Version](https://img.shields.io/pypi/v/stayforge)  ### SDK  - [Python SDK](https://github.com/tokujun-t/stayforge-python)  We provided SDKs (currently only the Python version is provided). Before deciding to call the API directly, you may wish to try the SDK to speed up your development.  ![GitHub Workflow Status](https://github.com/tokujun-t/Stayforge/actions/workflows/python-sdk.yml/badge.svg)   ### About Healthcheck  Healthcheck at `/api/healthcheck`. curl to check if the service is working.  ```shell curl -I http://<your service>/api/healthcheck ``` ### Some Links  GitHub Repo [https://github.com/tokujun-t/Stayforge](https://github.com/tokujun-t/Stayforge)  Wiki [https://github.com/tokujun-t/Stayforge/wiki](https://github.com/tokujun-t/Stayforge/wiki) 

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from stayforge.api.room_type_api import RoomTypeApi


class TestRoomTypeApi(unittest.TestCase):
    """RoomTypeApi unit test stubs"""

    def setUp(self) -> None:
        self.api = RoomTypeApi()

    def tearDown(self) -> None:
        pass

    def test_room_type_create(self) -> None:
        """Test case for room_type_create

        room_type_create
        """
        pass

    def test_room_type_delete(self) -> None:
        """Test case for room_type_delete

        room_type_delete
        """
        pass

    def test_room_type_get(self) -> None:
        """Test case for room_type_get

        room_type_get
        """
        pass

    def test_room_type_list(self) -> None:
        """Test case for room_type_list

        room_type_list
        """
        pass

    def test_room_type_update(self) -> None:
        """Test case for room_type_update

        room_type_update
        """
        pass


if __name__ == '__main__':
    unittest.main()
