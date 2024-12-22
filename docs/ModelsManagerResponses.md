# ModelsManagerResponses


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ModelsManager]**](ModelsManager.md) |  | 
**detail** | **str** |  | [optional] [default to 'Successfully.']
**status** | **int** |  | [optional] [default to 200]
**used_time** | **float** |  | [optional] 
**stayforge** | [**Stayforge**](Stayforge.md) |  | [optional] 

## Example

```python
from stayforge.models.models_manager_responses import ModelsManagerResponses

# TODO update the JSON string below
json = "{}"
# create an instance of ModelsManagerResponses from a JSON string
models_manager_responses_instance = ModelsManagerResponses.from_json(json)
# print the JSON string representation of the object
print(ModelsManagerResponses.to_json())

# convert the object into a dict
models_manager_responses_dict = models_manager_responses_instance.to_dict()
# create an instance of ModelsManagerResponses from a dict
models_manager_responses_from_dict = ModelsManagerResponses.from_dict(models_manager_responses_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


