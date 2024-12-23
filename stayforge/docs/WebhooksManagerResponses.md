# WebhooksManagerResponses


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[WebhooksManager]**](WebhooksManager.md) |  | 
**detail** | **str** |  | [optional] [default to 'Successfully.']
**status** | **int** |  | [optional] [default to 200]
**used_time** | **float** |  | [optional] 
**stayforge** | [**Stayforge**](Stayforge.md) |  | [optional] 

## Example

```python
from stayforge.models.webhooks_manager_responses import WebhooksManagerResponses

# TODO update the JSON string below
json = "{}"
# create an instance of WebhooksManagerResponses from a JSON string
webhooks_manager_responses_instance = WebhooksManagerResponses.from_json(json)
# print the JSON string representation of the object
print(WebhooksManagerResponses.to_json())

# convert the object into a dict
webhooks_manager_responses_dict = webhooks_manager_responses_instance.to_dict()
# create an instance of WebhooksManagerResponses from a dict
webhooks_manager_responses_from_dict = WebhooksManagerResponses.from_dict(webhooks_manager_responses_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


