# WebhooksManager


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Reference ID of the key. | [optional] [default to '67d35f43c210cb550f8e32ed']
**create_at** | **datetime** |  | 
**update_at** | **datetime** |  | [optional] 
**webhook_name** | **str** | The name of the webhook configuration. | 
**endpoint** | **str** | The URL where webhook events will be sent. | 
**catch_path** | **str** | The path to monitor for webhook events. | 
**catch_method** | **str** | HTTP method to be captured. | 
**catch_status** | **int** |  | [optional] 
**retry_status_code** | **List[str]** |  | [optional] 
**retry_times** | [**RetryTimes**](RetryTimes.md) |  | [optional] 

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


