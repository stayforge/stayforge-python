# Room


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Reference ID of the key. | [optional] [default to '67681b2e3f420d6e59c168b8']
**create_at** | **datetime** |  | 
**update_at** | **datetime** |  | [optional] 
**key_id** | **str** | Reference ID of the key. | [optional] [default to '67681b2e3f420d6e59c168ba']
**room_type_id** | **str** | Reference ID of the RoomType. | [optional] [default to '67681b2e3f420d6e59c168bb']
**number** | **str** | The number of rooms, e.g., 203. | 
**priority** | **int** | The OTA system will give priority to rooms with a higher value to guests. If the priorities are the same, then it is random. | 

## Example

```python
from stayforge.models.room import Room

# TODO update the JSON string below
json = "{}"
# create an instance of Room from a JSON string
room_instance = Room.from_json(json)
# print the JSON string representation of the object
print(Room.to_json())

# convert the object into a dict
room_dict = room_instance.to_dict()
# create an instance of Room from a dict
room_from_dict = Room.from_dict(room_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


