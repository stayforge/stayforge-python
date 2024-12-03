# RoomTypeResponses


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[RoomType]**](RoomType.md) |  | 
**detail** | **str** |  | [optional] [default to 'Successfully.']
**status** | **int** |  | [optional] [default to 200]
**used_time** | **float** |  | [optional] 
**stayforge** | [**Stayforge**](Stayforge.md) |  | [optional] 

## Example

```python
from openapi_client.models.room_type_responses import RoomTypeResponses

# TODO update the JSON string below
json = "{}"
# create an instance of RoomTypeResponses from a JSON string
room_type_responses_instance = RoomTypeResponses.from_json(json)
# print the JSON string representation of the object
print(RoomTypeResponses.to_json())

# convert the object into a dict
room_type_responses_dict = room_type_responses_instance.to_dict()
# create an instance of RoomTypeResponses from a dict
room_type_responses_from_dict = RoomTypeResponses.from_dict(room_type_responses_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


