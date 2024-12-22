# coding: utf-8

"""
    Stayforge API

    ![Commit Activity](https://img.shields.io/github/commit-activity/m/tokujun-t/stayforge) ![Codecov](https://codecov.io/gh/tokujun-t/stayforge/branch/main/graph/badge.svg) ![PyPI Version](https://img.shields.io/pypi/v/stayforge)  ### SDK  - [Python SDK](https://github.com/tokujun-t/stayforge-python)  We provided SDKs (currently only the Python version is provided). Before deciding to call the API directly, you may wish to try the SDK to speed up your development.  ![GitHub Workflow Status](https://github.com/tokujun-t/Stayforge/actions/workflows/python-sdk.yml/badge.svg)   ### About Healthcheck  Healthcheck at `/api/healthcheck`. curl to check if the service is working.  ```shell curl -I http://<your service>/api/healthcheck ``` ### Some Links  GitHub Repo [https://github.com/tokujun-t/Stayforge](https://github.com/tokujun-t/Stayforge)  Wiki [https://github.com/tokujun-t/Stayforge/wiki](https://github.com/tokujun-t/Stayforge/wiki) 

    The version of the OpenAPI document: 1.0.0
    Contact: support@stayforge.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from stayforge.models.api_branch_view_key_responses import ApiBranchViewKeyResponses

class TestApiBranchViewKeyResponses(unittest.TestCase):
    """ApiBranchViewKeyResponses unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiBranchViewKeyResponses:
        """Test ApiBranchViewKeyResponses
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiBranchViewKeyResponses`
        """
        model = ApiBranchViewKeyResponses()
        if include_optional:
            return ApiBranchViewKeyResponses(
                data = [
                    stayforge.models.key.Key(
                        id = '6768147b858275da0b832bd2', 
                        create_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        update_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        name = '', 
                        postcode = '000-0000', 
                        address = '000-0000', 
                        telephone = '', )
                    ],
                detail = 'Successfully.',
                status = 56,
                used_time = 1.337,
                stayforge = stayforge.models.stayforge.Stayforge(
                    ver = '1.0.0', )
            )
        else:
            return ApiBranchViewKeyResponses(
                data = [
                    stayforge.models.key.Key(
                        id = '6768147b858275da0b832bd2', 
                        create_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        update_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        name = '', 
                        postcode = '000-0000', 
                        address = '000-0000', 
                        telephone = '', )
                    ],
        )
        """

    def testApiBranchViewKeyResponses(self):
        """Test ApiBranchViewKeyResponses"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
