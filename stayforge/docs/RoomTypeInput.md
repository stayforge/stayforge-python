# RoomTypeInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The Type of RoomType | 
**description** | **str** | Description of the room type. | [optional] 
**price** | [**Price**](Price.md) |  | 
**price_policy** | **str** | The price controller will modify the corresponding price field based on the price policy ID. | [optional] 
**price_max** | [**PriceMax**](PriceMax.md) |  | [optional] 
**price_min** | [**PriceMin**](PriceMin.md) |  | 

## Example

```python
from stayforge.models.room_type_input import RoomTypeInput

# TODO update the JSON string below
json = "{}"
# create an instance of RoomTypeInput from a JSON string
room_type_input_instance = RoomTypeInput.from_json(json)
# print the JSON string representation of the object
print(RoomTypeInput.to_json())

# convert the object into a dict
room_type_input_dict = room_type_input_instance.to_dict()
# create an instance of RoomTypeInput from a dict
room_type_input_from_dict = RoomTypeInput.from_dict(room_type_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


