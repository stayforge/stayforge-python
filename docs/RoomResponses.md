# RoomResponses


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Room]**](Room.md) |  | 
**detail** | **str** |  | [optional] [default to 'Successfully.']
**status** | **int** |  | [optional] [default to 200]
**used_time** | **float** |  | [optional] 
**stayforge** | [**Stayforge**](Stayforge.md) |  | [optional] 

## Example

```python
from openapi_client.models.room_responses import RoomResponses

# TODO update the JSON string below
json = "{}"
# create an instance of RoomResponses from a JSON string
room_responses_instance = RoomResponses.from_json(json)
# print the JSON string representation of the object
print(RoomResponses.to_json())

# convert the object into a dict
room_responses_dict = room_responses_instance.to_dict()
# create an instance of RoomResponses from a dict
room_responses_from_dict = RoomResponses.from_dict(room_responses_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


