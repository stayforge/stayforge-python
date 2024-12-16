# PluginsManagerResponses


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[PluginsManager]**](PluginsManager.md) |  | 
**detail** | **str** |  | [optional] [default to 'Successfully.']
**status** | **int** |  | [optional] [default to 200]
**used_time** | **float** |  | [optional] 
**stayforge** | [**Stayforge**](Stayforge.md) |  | [optional] 

## Example

```python
from stayforge.models.plugins_manager_responses import PluginsManagerResponses

# TODO update the JSON string below
json = "{}"
# create an instance of PluginsManagerResponses from a JSON string
plugins_manager_responses_instance = PluginsManagerResponses.from_json(json)
# print the JSON string representation of the object
print(PluginsManagerResponses.to_json())

# convert the object into a dict
plugins_manager_responses_dict = plugins_manager_responses_instance.to_dict()
# create an instance of PluginsManagerResponses from a dict
plugins_manager_responses_from_dict = PluginsManagerResponses.from_dict(plugins_manager_responses_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


