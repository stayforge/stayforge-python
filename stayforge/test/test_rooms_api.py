# coding: utf-8

"""
    Stayforge API

    ![Commit Activity](https://img.shields.io/github/commit-activity/m/tokujun-t/stayforge) ![Codecov](https://codecov.io/gh/tokujun-t/stayforge/branch/main/graph/badge.svg) ![PyPI Version](https://img.shields.io/pypi/v/stayforge)  ### SDK  - [Python SDK](https://github.com/tokujun-t/stayforge-python)  We provided SDKs (currently only the Python version is provided). Before deciding to call the API directly, you may wish to try the SDK to speed up your development.  ![GitHub Workflow Status](https://github.com/tokujun-t/Stayforge/actions/workflows/python-sdk.yml/badge.svg)   ### About Healthcheck  Healthcheck at `/api/healthcheck`. curl to check if the service is working.  ```shell curl -I http://<your service>/api/healthcheck ``` ### Some Links  GitHub Repo [https://github.com/tokujun-t/Stayforge](https://github.com/tokujun-t/Stayforge)  Wiki [https://github.com/tokujun-t/Stayforge/wiki](https://github.com/tokujun-t/Stayforge/wiki) 

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from stayforge.api.rooms_api import RoomsApi


class TestRoomsApi(unittest.TestCase):
    """RoomsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = RoomsApi()

    def tearDown(self) -> None:
        pass

    def test_create_room_api_room_post(self) -> None:
        """Test case for create_room_api_room_post

        Create Room
        """
        pass

    def test_delete_room_api_room_id_delete(self) -> None:
        """Test case for delete_room_api_room_id_delete

        Delete Room
        """
        pass

    def test_get_room_api_room_id_get(self) -> None:
        """Test case for get_room_api_room_id_get

        Get Room
        """
        pass

    def test_get_rooms_api_room_get(self) -> None:
        """Test case for get_rooms_api_room_get

        Get Rooms
        """
        pass

    def test_put_room_api_room_id_put(self) -> None:
        """Test case for put_room_api_room_id_put

        Put Room
        """
        pass


if __name__ == '__main__':
    unittest.main()
