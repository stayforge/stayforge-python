# coding: utf-8

"""
    Stayforge API

    ![Commit Activity](https://img.shields.io/github/commit-activity/m/tokujun-t/stayforge) ![Codecov](https://codecov.io/gh/tokujun-t/stayforge/branch/main/graph/badge.svg) ![PyPI Version](https://img.shields.io/pypi/v/stayforge)  ### SDK  - [Python SDK](https://github.com/tokujun-t/stayforge-python)  We provided SDKs (currently only the Python version is provided). Before deciding to call the API directly, you may wish to try the SDK to speed up your development.  ![GitHub Workflow Status](https://github.com/tokujun-t/Stayforge/actions/workflows/python-sdk.yml/badge.svg)   ### About Healthcheck  Healthcheck at `/api/healthcheck`. curl to check if the service is working.  ```shell curl -I http://<your service>/api/healthcheck ``` ### Some Links  GitHub Repo [https://github.com/tokujun-t/Stayforge](https://github.com/tokujun-t/Stayforge)  Wiki [https://github.com/tokujun-t/Stayforge/wiki](https://github.com/tokujun-t/Stayforge/wiki) 

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from stayforge.api.room_types_api import RoomTypesApi


class TestRoomTypesApi(unittest.TestCase):
    """RoomTypesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = RoomTypesApi()

    def tearDown(self) -> None:
        pass

    def test_create_room_type_api_room_type_rooms_post(self) -> None:
        """Test case for create_room_type_api_room_type_rooms_post

        Create Room Type
        """
        pass

    def test_delete_room_type_api_room_type_room_types_room_type_id_delete(self) -> None:
        """Test case for delete_room_type_api_room_type_room_types_room_type_id_delete

        Delete Room Type
        """
        pass

    def test_get_room_type_api_room_type_room_types_room_type_id_get(self) -> None:
        """Test case for get_room_type_api_room_type_room_types_room_type_id_get

        Get Room Type
        """
        pass

    def test_get_room_types_api_room_type_rooms_get(self) -> None:
        """Test case for get_room_types_api_room_type_rooms_get

        Get Room Types
        """
        pass

    def test_update_room_type_api_room_type_room_types_room_type_id_put(self) -> None:
        """Test case for update_room_type_api_room_type_room_types_room_type_id_put

        Update Room Type
        """
        pass


if __name__ == '__main__':
    unittest.main()
