# ApiKeyManagerViewKeyResponses


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ApiKeyManagerModelsKey]**](ApiKeyManagerModelsKey.md) |  | 
**detail** | **str** |  | [optional] [default to 'Successfully.']
**status** | **int** |  | [optional] [default to 200]
**used_time** | **float** |  | [optional] 
**stayforge** | [**Stayforge**](Stayforge.md) |  | [optional] 

## Example

```python
from openapi_client.models.api_key_manager_view_key_responses import ApiKeyManagerViewKeyResponses

# TODO update the JSON string below
json = "{}"
# create an instance of ApiKeyManagerViewKeyResponses from a JSON string
api_key_manager_view_key_responses_instance = ApiKeyManagerViewKeyResponses.from_json(json)
# print the JSON string representation of the object
print(ApiKeyManagerViewKeyResponses.to_json())

# convert the object into a dict
api_key_manager_view_key_responses_dict = api_key_manager_view_key_responses_instance.to_dict()
# create an instance of ApiKeyManagerViewKeyResponses from a dict
api_key_manager_view_key_responses_from_dict = ApiKeyManagerViewKeyResponses.from_dict(api_key_manager_view_key_responses_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


