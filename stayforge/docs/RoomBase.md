# RoomBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**room_type_id** | **str** | Reference ID of the RoomType. | 
**branch_id** | **str** | Reference ID of the Branch. | 
**number** | **str** | The number of rooms, e.g., 203. | 
**priority** | **int** | Stayforge will prioritize rooms with high priority numbers to guests. When the priority is the same, it is randomly selected according to certain rules. | [optional] [default to 0]

## Example

```python
from stayforge.models.room_base import RoomBase

# TODO update the JSON string below
json = "{}"
# create an instance of RoomBase from a JSON string
room_base_instance = RoomBase.from_json(json)
# print the JSON string representation of the object
print(RoomBase.to_json())

# convert the object into a dict
room_base_dict = room_base_instance.to_dict()
# create an instance of RoomBase from a dict
room_base_from_dict = RoomBase.from_dict(room_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


