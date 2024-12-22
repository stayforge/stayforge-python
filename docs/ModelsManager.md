# ModelsManager


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Reference ID of the key. | [optional] [default to '67683e7808122b7fbc20ff34']
**create_at** | **datetime** |  | 
**update_at** | **datetime** |  | [optional] 
**model** | **str** | The host URL of the model. This is used to generate webhook URLs and other model-related paths. | 
**model_version** | **str** | The version of the model. This helps in tracking updates and ensuring compatibility. | [optional] [default to 'latest']
**local_name** | **str** |  | [optional] 
**permissions** | **object** |  | [optional] 

## Example

```python
from stayforge.models.models_manager import ModelsManager

# TODO update the JSON string below
json = "{}"
# create an instance of ModelsManager from a JSON string
models_manager_instance = ModelsManager.from_json(json)
# print the JSON string representation of the object
print(ModelsManager.to_json())

# convert the object into a dict
models_manager_dict = models_manager_instance.to_dict()
# create an instance of ModelsManager from a dict
models_manager_from_dict = ModelsManager.from_dict(models_manager_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


