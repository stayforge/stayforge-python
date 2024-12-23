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

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from stayforge.models.id_document import IDDocument
from typing import Optional, Set
from typing_extensions import Self

class Guest(BaseModel):
    """
    Guest
    """ # noqa: E501
    first_name: Optional[StrictStr] = None
    middle_name: Optional[StrictStr] = None
    last_name: Optional[StrictStr] = None
    gender: Optional[StrictStr] = None
    birthday: Optional[StrictStr] = None
    nationality: Optional[StrictStr] = None
    email: Optional[StrictStr] = None
    phone_number: Optional[StrictStr] = None
    address: Optional[StrictStr] = None
    occupation: Optional[StrictStr] = None
    passport_number: Optional[StrictStr] = None
    id_document: Optional[IDDocument]
    __properties: ClassVar[List[str]] = ["first_name", "middle_name", "last_name", "gender", "birthday", "nationality", "email", "phone_number", "address", "occupation", "passport_number", "id_document"]

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
        """Create an instance of Guest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of id_document
        if self.id_document:
            _dict['id_document'] = self.id_document.to_dict()
        # set to None if id_document (nullable) is None
        # and model_fields_set contains the field
        if self.id_document is None and "id_document" in self.model_fields_set:
            _dict['id_document'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Guest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "first_name": obj.get("first_name"),
            "middle_name": obj.get("middle_name"),
            "last_name": obj.get("last_name"),
            "gender": obj.get("gender"),
            "birthday": obj.get("birthday"),
            "nationality": obj.get("nationality"),
            "email": obj.get("email"),
            "phone_number": obj.get("phone_number"),
            "address": obj.get("address"),
            "occupation": obj.get("occupation"),
            "passport_number": obj.get("passport_number"),
            "id_document": IDDocument.from_dict(obj["id_document"]) if obj.get("id_document") is not None else None
        })
        return _obj


