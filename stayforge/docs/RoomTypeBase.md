# RoomTypeBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parent** | **str** | Parent room type’s name. If set to None, it will be considered a top-level room type. | [optional] 
**name** | **str** | Unique name of RoomType. | 
**name_visible** | **str** | A visible name of the room type. | 
**description** | **str** | Description of the room type. | [optional] 
**branch** | **List[str]** | Branch names that this type is available. If None, it will follow the parent settings or allow all branches by default. | [optional] 
**base_price** | **str** | Base price. If you set a price strategy, the price will automatically increase according to the strategy. | 
**price_policy** | **str** | The price controller will modify the corresponding price field based on the price policy name. | [optional] 
**min_usage** | **float** | Minimum usage hours. | 
**max_usage** | **float** | Maximum usage hours. | 
**allow_extension** | **bool** | When it True, this type will marked as allowed to extend. | [optional] 

## Example

```python
from stayforge.models.room_type_base import RoomTypeBase

# TODO update the JSON string below
json = "{}"
# create an instance of RoomTypeBase from a JSON string
room_type_base_instance = RoomTypeBase.from_json(json)
# print the JSON string representation of the object
print(RoomTypeBase.to_json())

# convert the object into a dict
room_type_base_dict = room_type_base_instance.to_dict()
# create an instance of RoomTypeBase from a dict
room_type_base_from_dict = RoomTypeBase.from_dict(room_type_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


