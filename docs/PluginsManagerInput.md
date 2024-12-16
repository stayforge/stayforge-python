# PluginsManagerInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plugin** | **str** | The host URL of the plugin. This is used to generate webhook URLs and other plugin-related paths. | 
**plugin_version** | **str** | The version of the plugin. This helps in tracking updates and ensuring compatibility. | 
**permissions** | **object** | ### Example  &#x60;String &#39;auto&#39;&#x60; or &#x60;JSON Started dict&#x60;.  When the value is auto, the content in the plug-in configuration &#x60;permissions.json&#x60; is used.  Stayforge APIs that can be called by the plugin, starting with &#x60;_&#x60; are method names.  &#x60;&#x60;&#x60;json {   \&quot;room\&quot;: {     \&quot;_methods\&quot;: {       \&quot;_post\&quot;: {         \&quot;_allow\&quot;: true,         \&quot;_webhook\&quot;: true,         \&quot;_webhook_path\&quot;: \&quot;/webhook/room\&quot;       }     }   } } &#x60;&#x60;&#x60;  ### Key Elements  1. **API Name** (&#x60;&lt;API Name&gt;&#x60;):     - Represents the name of the API the plugin interacts with (e.g., &#x60;\&quot;room\&quot;&#x60;).  2. **_methods**:     - Defines the HTTP methods (e.g., &#x60;_post&#x60;, &#x60;_get&#x60;, &#x60;_put&#x60;, &#x60;_delete&#x60;) that the API supports.  3. **HTTP Method Configuration**:     - &#x60;_allow&#x60; (Required):         - A boolean indicating whether the method is allowed for plugins. If &#x60;False&#x60;, the plugin cannot use this method.     - &#x60;_webhook&#x60; (Optional):         - A boolean indicating whether webhook functionality is enabled for this method. If &#x60;True&#x60;, a &#x60;_webhook_path&#x60;           must be specified.     - &#x60;_webhook_path&#x60; (Required if &#x60;_webhook&#x60; is &#x60;True&#x60;):         - A string representing the webhook submission URL path. The full URL is constructed by concatenating the           &#x60;plugin_host&#x60; with &#x60;_webhook_path&#x60;.  | [optional] 

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


