# coding: utf-8

# flake8: noqa

"""
    Stayforge API

    ![Commit Activity](https://img.shields.io/github/commit-activity/m/tokujun-t/stayforge) ![Codecov](https://codecov.io/gh/tokujun-t/stayforge/branch/main/graph/badge.svg) ![PyPI Version](https://img.shields.io/pypi/v/stayforge)  ### SDK  - [Python SDK](https://github.com/tokujun-t/stayforge-python)  We provided SDKs (currently only the Python version is provided). Before deciding to call the API directly, you may wish to try the SDK to speed up your development.  ![GitHub Workflow Status](https://github.com/tokujun-t/Stayforge/actions/workflows/python-sdk.yml/badge.svg)   ### About Healthcheck  Healthcheck at `/api/healthcheck`. curl to check if the service is working.  ```shell curl -I http://<your service>/api/healthcheck ``` ### Some Links  GitHub Repo [https://github.com/tokujun-t/Stayforge](https://github.com/tokujun-t/Stayforge)  Wiki [https://github.com/tokujun-t/Stayforge/wiki](https://github.com/tokujun-t/Stayforge/wiki) 

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


__version__ = "0.0.0-7116e2a"

# import apis into sdk package
from stayforge.api.message_queue_api import MessageQueueApi
from stayforge.api.models_etcd_api import ModelsEtcdApi
from stayforge.api.models_manager_api import ModelsManagerApi
from stayforge.api.webhooks_manager_api import WebhooksManagerApi
from stayforge.api.branch_api import BranchApi
from stayforge.api.order_api import OrderApi
from stayforge.api.room_api import RoomApi
from stayforge.api.room_type_api import RoomTypeApi

# import ApiClient
from stayforge.api_response import ApiResponse
from stayforge.api_client import ApiClient
from stayforge.configuration import Configuration
from stayforge.exceptions import OpenApiException
from stayforge.exceptions import ApiTypeError
from stayforge.exceptions import ApiValueError
from stayforge.exceptions import ApiKeyError
from stayforge.exceptions import ApiAttributeError
from stayforge.exceptions import ApiException

# import models into sdk package
from stayforge.models.branch_base import BranchBase
from stayforge.models.http_validation_error import HTTPValidationError
from stayforge.models.key_value_request import KeyValueRequest
from stayforge.models.mq_enqueue import MQEnqueue
from stayforge.models.models_manager import ModelsManager
from stayforge.models.models_manager_input import ModelsManagerInput
from stayforge.models.models_manager_responses import ModelsManagerResponses
from stayforge.models.retry_times import RetryTimes
from stayforge.models.room_base import RoomBase
from stayforge.models.room_type_base import RoomTypeBase
from stayforge.models.stayforge import Stayforge
from stayforge.models.validation_error import ValidationError
from stayforge.models.validation_error_loc_inner import ValidationErrorLocInner
from stayforge.models.webhooks_manager import WebhooksManager
from stayforge.models.webhooks_manager_input import WebhooksManagerInput
from stayforge.models.webhooks_manager_responses import WebhooksManagerResponses
