# WebhooksManager


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Reference ID of the key. | [optional] [default to '675d7c54524f6cd129efea6e']
**create_at** | **datetime** |  | 
**update_at** | **datetime** |  | [optional] 
**webhook_name** | **str** | The Type of WebhooksManager | 
**endpoint** | **str** | Description of the room type. | 
**catch_path** | **str** | Current price. If you deploy a price controller, this value will be updated automatically. | 
**catch_method** | **str** | HTTP method to be captured. | 
**catch_status** | **int** | HTTP status to be captured. | [optional] [default to 200]

## Example

```python
from stayforge.models.webhooks_manager import WebhooksManager

# TODO update the JSON string below
json = "{}"
# create an instance of WebhooksManager from a JSON string
webhooks_manager_instance = WebhooksManager.from_json(json)
# print the JSON string representation of the object
print(WebhooksManager.to_json())

# convert the object into a dict
webhooks_manager_dict = webhooks_manager_instance.to_dict()
# create an instance of WebhooksManager from a dict
webhooks_manager_from_dict = WebhooksManager.from_dict(webhooks_manager_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


