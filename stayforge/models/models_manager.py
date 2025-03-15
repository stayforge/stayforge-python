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
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class ModelsManager(BaseModel):
    """
    ModelsManager
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default='67d560b7d94852fc2f0185c5', description="The unique ID of this object.")
    metadata: Optional[Dict[str, Any]] = None
    create_at: Optional[datetime]
    update_at: Optional[datetime]
    model: StrictStr = Field(description="The host URL of the model. This is used to generate webhook URLs and other model-related paths.")
    model_version: Optional[StrictStr] = Field(default='latest', description="The version of the model. This helps in tracking updates and ensuring compatibility.")
    local_name: Optional[StrictStr] = None
    permissions: Optional[Dict[str, Any]] = None
    etcd_host: StrictStr
    etcd_port: Optional[StrictInt] = 2379
    etcd_user: StrictStr
    etcd_password: StrictStr
    __properties: ClassVar[List[str]] = ["id", "metadata", "create_at", "update_at", "model", "model_version", "local_name", "permissions", "etcd_host", "etcd_port", "etcd_user", "etcd_password"]

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
        """Create an instance of ModelsManager from a JSON string"""
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

        # set to None if local_name (nullable) is None
        # and model_fields_set contains the field
        if self.local_name is None and "local_name" in self.model_fields_set:
            _dict['local_name'] = None

        # set to None if permissions (nullable) is None
        # and model_fields_set contains the field
        if self.permissions is None and "permissions" in self.model_fields_set:
            _dict['permissions'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ModelsManager from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id") if obj.get("id") is not None else '67d560b7d94852fc2f0185c5',
            "metadata": obj.get("metadata"),
            "create_at": obj.get("create_at"),
            "update_at": obj.get("update_at"),
            "model": obj.get("model"),
            "model_version": obj.get("model_version") if obj.get("model_version") is not None else 'latest',
            "local_name": obj.get("local_name"),
            "permissions": obj.get("permissions"),
            "etcd_host": obj.get("etcd_host"),
            "etcd_port": obj.get("etcd_port") if obj.get("etcd_port") is not None else 2379,
            "etcd_user": obj.get("etcd_user"),
            "etcd_password": obj.get("etcd_password")
        })
        return _obj


