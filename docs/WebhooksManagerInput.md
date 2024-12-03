# WebhooksManagerInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**webhook_name** | **str** | The Type of WebhooksManager | 
**endpoint** | **str** | Description of the room type. | 
**catch_path** | **str** | Current price. If you deploy a price controller, this value will be updated automatically. | 
**catch_method** | **str** | HTTP method to be captured. | 
**catch_status** | **int** | HTTP status to be captured. | [optional] [default to 200]

## Example

```python
from openapi_client.models.webhooks_manager_input import WebhooksManagerInput

# TODO update the JSON string below
json = "{}"
# create an instance of WebhooksManagerInput from a JSON string
webhooks_manager_input_instance = WebhooksManagerInput.from_json(json)
# print the JSON string representation of the object
print(WebhooksManagerInput.to_json())

# convert the object into a dict
webhooks_manager_input_dict = webhooks_manager_input_instance.to_dict()
# create an instance of WebhooksManagerInput from a dict
webhooks_manager_input_from_dict = WebhooksManagerInput.from_dict(webhooks_manager_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


