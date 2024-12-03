# coding: utf-8

"""
    Stayforge API

    This is a basic API description.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from stayforge.models.api_branch_models_key import ApiBranchModelsKey

class TestApiBranchModelsKey(unittest.TestCase):
    """ApiBranchModelsKey unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiBranchModelsKey:
        """Test ApiBranchModelsKey
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiBranchModelsKey`
        """
        model = ApiBranchModelsKey()
        if include_optional:
            return ApiBranchModelsKey(
                id = '674f7fd50baf7c4f8c450f5b',
                create_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                update_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                name = '',
                postcode = '000-0000',
                address = '000-0000',
                telephone = ''
            )
        else:
            return ApiBranchModelsKey(
                create_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                name = '',
                telephone = '',
        )
        """

    def testApiBranchModelsKey(self):
        """Test ApiBranchModelsKey"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
