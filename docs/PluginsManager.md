# PluginsManager


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Reference ID of the key. | [optional] [default to '67681042212ceae96ac67828']
**create_at** | **datetime** |  | 
**update_at** | **datetime** |  | [optional] 
**plugin** | **str** | The host URL of the plugin. This is used to generate webhook URLs and other plugin-related paths. | 
**plugin_version** | **str** | The version of the plugin. This helps in tracking updates and ensuring compatibility. | [optional] [default to 'latest']
**local_name** | **str** |  | [optional] 
**permissions** | **object** |  | [optional] 

## Example

```python
from stayforge.models.plugins_manager import PluginsManager

# TODO update the JSON string below
json = "{}"
# create an instance of PluginsManager from a JSON string
plugins_manager_instance = PluginsManager.from_json(json)
# print the JSON string representation of the object
print(PluginsManager.to_json())

# convert the object into a dict
plugins_manager_dict = plugins_manager_instance.to_dict()
# create an instance of PluginsManager from a dict
plugins_manager_from_dict = PluginsManager.from_dict(plugins_manager_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


