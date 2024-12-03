# coding: utf-8

"""
    Stayforge API

    This is a basic API description.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class RoomType(BaseModel):
    """
    RoomType
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default='674f89f2caad30d1418f12ba', description="Reference ID of the key.")
    create_at: Optional[datetime]
    update_at: Optional[datetime] = None
    name: StrictStr = Field(description="The Type of RoomType")
    description: Optional[StrictStr] = Field(default=None, description="Description of the room type.")
    price: StrictStr = Field(description="Current price. If you deploy a price controller, this value will be updated automatically.")
    price_policy: Optional[StrictStr] = Field(default=None, description="The price controller will modify the corresponding price field based on the price policy ID.")
    price_max: Optional[StrictStr] = Field(default=None, description="The max of price.")
    price_min: StrictStr = Field(description="The min of price.")
    __properties: ClassVar[List[str]] = ["id", "create_at", "update_at", "name", "description", "price", "price_policy", "price_max", "price_min"]

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
        """Create an instance of RoomType from a JSON string"""
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
        # set to None if create_at (nullable) is None
        # and model_fields_set contains the field
        if self.create_at is None and "create_at" in self.model_fields_set:
            _dict['create_at'] = None

        # set to None if update_at (nullable) is None
        # and model_fields_set contains the field
        if self.update_at is None and "update_at" in self.model_fields_set:
            _dict['update_at'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RoomType from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id") if obj.get("id") is not None else '674f89f2caad30d1418f12ba',
            "create_at": obj.get("create_at"),
            "update_at": obj.get("update_at"),
            "name": obj.get("name"),
            "description": obj.get("description"),
            "price": obj.get("price"),
            "price_policy": obj.get("price_policy"),
            "price_max": obj.get("price_max"),
            "price_min": obj.get("price_min")
        })
        return _obj


