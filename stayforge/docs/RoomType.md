# RoomType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Reference ID of the key. | [optional] [default to '678b99563ba2fc9a277480f3']
**create_at** | **datetime** |  | 
**update_at** | **datetime** |  | [optional] 
**name** | **str** | The Type of RoomType | 
**description** | **str** | Description of the room type. | [optional] 
**price** | **str** | Current price. If you deploy a price controller, this value will be updated automatically. | 
**price_policy** | **str** | The price controller will modify the corresponding price field based on the price policy ID. | [optional] 
**price_max** | **str** | The max of price. | [optional] 
**price_min** | **str** | The min of price. | 

## Example

```python
from stayforge.models.room_type import RoomType

# TODO update the JSON string below
json = "{}"
# create an instance of RoomType from a JSON string
room_type_instance = RoomType.from_json(json)
# print the JSON string representation of the object
print(RoomType.to_json())

# convert the object into a dict
room_type_dict = room_type_instance.to_dict()
# create an instance of RoomType from a dict
room_type_from_dict = RoomType.from_dict(room_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


