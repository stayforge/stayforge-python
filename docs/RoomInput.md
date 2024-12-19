# RoomInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key_id** | **str** | Reference ID of the key. | [optional] [default to '676429c0e0101c91bb881c36']
**room_type_id** | **str** | Reference ID of the RoomType. | [optional] [default to '676429c0e0101c91bb881c37']
**number** | **str** | The number of rooms, e.g., 203. | 
**priority** | **int** | The OTA system will give priority to rooms with a higher value to guests. If the priorities are the same, then it is random. | 

## Example

```python
from stayforge.models.room_input import RoomInput

# TODO update the JSON string below
json = "{}"
# create an instance of RoomInput from a JSON string
room_input_instance = RoomInput.from_json(json)
# print the JSON string representation of the object
print(RoomInput.to_json())

# convert the object into a dict
room_input_dict = room_input_instance.to_dict()
# create an instance of RoomInput from a dict
room_input_from_dict = RoomInput.from_dict(room_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


