# coding: utf-8

"""
    Stayforge API

    ![Commit Activity](https://img.shields.io/github/commit-activity/m/tokujun-t/stayforge) ![Codecov](https://codecov.io/gh/tokujun-t/stayforge/branch/main/graph/badge.svg) ![PyPI Version](https://img.shields.io/pypi/v/stayforge)  ### SDK  - [Python SDK](https://github.com/tokujun-t/stayforge-python)  We provided SDKs (currently only the Python version is provided). Before deciding to call the API directly, you may wish to try the SDK to speed up your development.  ![GitHub Workflow Status](https://github.com/tokujun-t/Stayforge/actions/workflows/python-sdk.yml/badge.svg)   ### About Healthcheck  Healthcheck at `/api/healthcheck`. curl to check if the service is working.  ```shell curl -I http://<your service>/api/healthcheck ``` ### Some Links  GitHub Repo [https://github.com/tokujun-t/Stayforge](https://github.com/tokujun-t/Stayforge)  Wiki [https://github.com/tokujun-t/Stayforge/wiki](https://github.com/tokujun-t/Stayforge/wiki) 

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from stayforge.models.retry_times import RetryTimes
from typing import Optional, Set
from typing_extensions import Self

class WebhooksManager(BaseModel):
    """
    WebhooksManager
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default='67d6bc5eb4d9feb12a5a2a03', description="The unique ID of this object.")
    metadata: Optional[Dict[str, Any]] = None
    create_at: Optional[datetime]
    update_at: Optional[datetime]
    webhook_name: StrictStr = Field(description="The name of the webhook configuration.")
    endpoint: Annotated[str, Field(min_length=1, strict=True, max_length=2083)] = Field(description="The URL where webhook events will be sent.")
    catch_path: StrictStr = Field(description="The path to monitor for webhook events.")
    catch_method: StrictStr = Field(description="HTTP method to be captured.")
    catch_status: Optional[StrictInt] = None
    retry_status_code: Optional[List[StrictStr]] = None
    retry_times: Optional[RetryTimes] = None
    __properties: ClassVar[List[str]] = ["id", "metadata", "create_at", "update_at", "webhook_name", "endpoint", "catch_path", "catch_method", "catch_status", "retry_status_code", "retry_times"]

    @field_validator('catch_method')
    def catch_method_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['POST', 'GET', 'PUT', 'DELETE']):
            raise ValueError("must be one of enum values ('POST', 'GET', 'PUT', 'DELETE')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of WebhooksManager from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of retry_times
        if self.retry_times:
            _dict['retry_times'] = self.retry_times.to_dict()
        # set to None if metadata (nullable) is None
        # and model_fields_set contains the field
        if self.metadata is None and "metadata" in self.model_fields_set:
            _dict['metadata'] = None

        # set to None if create_at (nullable) is None
        # and model_fields_set contains the field
        if self.create_at is None and "create_at" in self.model_fields_set:
            _dict['create_at'] = None

        # set to None if update_at (nullable) is None
        # and model_fields_set contains the field
        if self.update_at is None and "update_at" in self.model_fields_set:
            _dict['update_at'] = None

        # set to None if catch_status (nullable) is None
        # and model_fields_set contains the field
        if self.catch_status is None and "catch_status" in self.model_fields_set:
            _dict['catch_status'] = None

        # set to None if retry_status_code (nullable) is None
        # and model_fields_set contains the field
        if self.retry_status_code is None and "retry_status_code" in self.model_fields_set:
            _dict['retry_status_code'] = None

        # set to None if retry_times (nullable) is None
        # and model_fields_set contains the field
        if self.retry_times is None and "retry_times" in self.model_fields_set:
            _dict['retry_times'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of WebhooksManager from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id") if obj.get("id") is not None else '67d6bc5eb4d9feb12a5a2a03',
            "metadata": obj.get("metadata"),
            "create_at": obj.get("create_at"),
            "update_at": obj.get("update_at"),
            "webhook_name": obj.get("webhook_name"),
            "endpoint": obj.get("endpoint"),
            "catch_path": obj.get("catch_path"),
            "catch_method": obj.get("catch_method"),
            "catch_status": obj.get("catch_status"),
            "retry_status_code": obj.get("retry_status_code"),
            "retry_times": RetryTimes.from_dict(obj["retry_times"]) if obj.get("retry_times") is not None else None
        })
        return _obj


