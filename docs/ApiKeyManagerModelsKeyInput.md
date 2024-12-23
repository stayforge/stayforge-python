# ApiKeyManagerModelsKeyInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The name of the hotel key. By default, it combines a base name with a random town. | 
**num** | **str** | Order number | [optional] [default to '']
**effective_at** | **str** | Effective at | [optional] [default to '2024-12-23T10:16:33.484030Z']
**ineffective_at** | **str** | Ineffective at | [optional] [default to '2024-12-24T10:16:33.484061Z']

## Example

```python
from stayforge.models.api_key_manager_models_key_input import ApiKeyManagerModelsKeyInput

# TODO update the JSON string below
json = "{}"
# create an instance of ApiKeyManagerModelsKeyInput from a JSON string
api_key_manager_models_key_input_instance = ApiKeyManagerModelsKeyInput.from_json(json)
# print the JSON string representation of the object
print(ApiKeyManagerModelsKeyInput.to_json())

# convert the object into a dict
api_key_manager_models_key_input_dict = api_key_manager_models_key_input_instance.to_dict()
# create an instance of ApiKeyManagerModelsKeyInput from a dict
api_key_manager_models_key_input_from_dict = ApiKeyManagerModelsKeyInput.from_dict(api_key_manager_models_key_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


