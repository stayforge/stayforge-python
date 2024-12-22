# ModelsManagerInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model** | **str** | The host URL of the model. This is used to generate webhook URLs and other model-related paths. | 
**model_version** | **str** | The version of the model. This helps in tracking updates and ensuring compatibility. | [optional] [default to 'latest']
**local_name** | **str** |  | [optional] 
**permissions** | **object** |  | [optional] 

## Example

```python
from stayforge.models.models_manager_input import ModelsManagerInput

# TODO update the JSON string below
json = "{}"
# create an instance of ModelsManagerInput from a JSON string
models_manager_input_instance = ModelsManagerInput.from_json(json)
# print the JSON string representation of the object
print(ModelsManagerInput.to_json())

# convert the object into a dict
models_manager_input_dict = models_manager_input_instance.to_dict()
# create an instance of ModelsManagerInput from a dict
models_manager_input_from_dict = ModelsManagerInput.from_dict(models_manager_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


