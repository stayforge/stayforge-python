# coding: utf-8

"""
    Stayforge API

    ![Commit Activity](https://img.shields.io/github/commit-activity/m/tokujun-t/stayforge) ![Codecov](https://codecov.io/gh/tokujun-t/stayforge/branch/main/graph/badge.svg) ![PyPI Version](https://img.shields.io/pypi/v/stayforge)  ### SDK  - [Python SDK](https://github.com/tokujun-t/stayforge-python)  We provided SDKs (currently only the Python version is provided). Before deciding to call the API directly, you may wish to try the SDK to speed up your development.  ![GitHub Workflow Status](https://github.com/tokujun-t/Stayforge/actions/workflows/python-sdk.yml/badge.svg)   ### About Healthcheck  Healthcheck at `/api/healthcheck`. curl to check if the service is working.  ```shell curl -I http://<your service>/api/healthcheck ``` ### Some Links  GitHub Repo [https://github.com/tokujun-t/Stayforge](https://github.com/tokujun-t/Stayforge)  Wiki [https://github.com/tokujun-t/Stayforge/wiki](https://github.com/tokujun-t/Stayforge/wiki) 

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from stayforge.models.models_manager import ModelsManager

class TestModelsManager(unittest.TestCase):
    """ModelsManager unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ModelsManager:
        """Test ModelsManager
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ModelsManager`
        """
        model = ModelsManager()
        if include_optional:
            return ModelsManager(
                id = '67d36ad2047a5c2885906e9d',
                create_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                update_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                model = '',
                model_version = 'latest',
                local_name = '',
                permissions = None,
                etcd_host = '',
                etcd_port = 56,
                etcd_user = '',
                etcd_password = ''
            )
        else:
            return ModelsManager(
                create_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                model = '',
                etcd_host = '',
                etcd_user = '',
                etcd_password = '',
        )
        """

    def testModelsManager(self):
        """Test ModelsManager"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
