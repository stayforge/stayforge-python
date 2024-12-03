# OrderResponses


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Order]**](Order.md) |  | 
**detail** | **str** |  | [optional] [default to 'Successfully.']
**status** | **int** |  | [optional] [default to 200]
**used_time** | **float** |  | [optional] 
**stayforge** | [**Stayforge**](Stayforge.md) |  | [optional] 

## Example

```python
from openapi_client.models.order_responses import OrderResponses

# TODO update the JSON string below
json = "{}"
# create an instance of OrderResponses from a JSON string
order_responses_instance = OrderResponses.from_json(json)
# print the JSON string representation of the object
print(OrderResponses.to_json())

# convert the object into a dict
order_responses_dict = order_responses_instance.to_dict()
# create an instance of OrderResponses from a dict
order_responses_from_dict = OrderResponses.from_dict(order_responses_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


