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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class RoomTypeBaseOutput(BaseModel):
    """
    RoomTypeBaseOutput
    """ # noqa: E501
    parent: Optional[StrictStr] = Field(default=None, description="Parent room type’s name. If set to None, it will be considered a top-level room type.")
    name: StrictStr = Field(description="Unique name of RoomType.")
    name_visible: StrictStr = Field(description="A visible name of the room type.", alias="nameVisible")
    description: Optional[StrictStr] = Field(default=None, description="Description of the room type.")
    branch: Optional[List[StrictStr]] = Field(default=None, description="Branch names that this type is available. If None, it will follow the parent settings or allow all branches by default.")
    base_price: StrictStr = Field(description="Base price. If you set a price strategy, the price will automatically increase according to the strategy.", alias="basePrice")
    price_policy: Optional[StrictStr] = Field(default=None, description="The price controller will modify the corresponding price field based on the price policy name.", alias="pricePolicy")
    min_usage: Union[StrictFloat, StrictInt] = Field(description="Minimum usage hours.")
    max_usage: Union[StrictFloat, StrictInt] = Field(description="Maximum usage hours.")
    allow_extension: Optional[StrictBool] = Field(default=None, description="When it True, this type will marked as allowed to extend.", alias="allowExtension")
    __properties: ClassVar[List[str]] = ["parent", "name", "nameVisible", "description", "branch", "basePrice", "pricePolicy", "min_usage", "max_usage", "allowExtension"]

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
        """Create an instance of RoomTypeBaseOutput from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RoomTypeBaseOutput from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "parent": obj.get("parent"),
            "name": obj.get("name"),
            "nameVisible": obj.get("nameVisible"),
            "description": obj.get("description"),
            "branch": obj.get("branch"),
            "basePrice": obj.get("basePrice"),
            "pricePolicy": obj.get("pricePolicy"),
            "min_usage": obj.get("min_usage"),
            "max_usage": obj.get("max_usage"),
            "allowExtension": obj.get("allowExtension")
        })
        return _obj


