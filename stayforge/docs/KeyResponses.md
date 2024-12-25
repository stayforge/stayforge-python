# KeyResponses


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Key]**](Key.md) |  | 
**detail** | **str** |  | [optional] [default to 'Successfully.']
**status** | **int** |  | [optional] [default to 200]
**used_time** | **float** |  | [optional] 
**stayforge** | [**Stayforge**](Stayforge.md) |  | [optional] 

## Example

```python
from stayforge.models.key_responses import KeyResponses

# TODO update the JSON string below
json = "{}"
# create an instance of KeyResponses from a JSON string
key_responses_instance = KeyResponses.from_json(json)
# print the JSON string representation of the object
print(KeyResponses.to_json())

# convert the object into a dict
key_responses_dict = key_responses_instance.to_dict()
# create an instance of KeyResponses from a dict
key_responses_from_dict = KeyResponses.from_dict(key_responses_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


