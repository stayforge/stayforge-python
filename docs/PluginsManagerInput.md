# PluginsManagerInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plugin** | **str** | The host URL of the plugin. This is used to generate webhook URLs and other plugin-related paths. | 
**plugin_version** | **str** | The version of the plugin. This helps in tracking updates and ensuring compatibility. | [optional] [default to 'latest']
**local_name** | **str** |  | [optional] 
**permissions** | **object** |  | [optional] 

## Example

```python
from stayforge.models.plugins_manager_input import PluginsManagerInput

# TODO update the JSON string below
json = "{}"
# create an instance of PluginsManagerInput from a JSON string
plugins_manager_input_instance = PluginsManagerInput.from_json(json)
# print the JSON string representation of the object
print(PluginsManagerInput.to_json())

# convert the object into a dict
plugins_manager_input_dict = plugins_manager_input_instance.to_dict()
# create an instance of PluginsManagerInput from a dict
plugins_manager_input_from_dict = PluginsManagerInput.from_dict(plugins_manager_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


