# OrderInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**num** | **str** | Order number | [optional] 
**room_id** | **str** | Room ID | [optional] 
**guest** | [**Guest**](Guest.md) | Guest information | [optional] 
**type** | **str** | OrderType | 
**scheduled_checkin_at** | **datetime** | Creation timestamp | [optional] 
**scheduled_checkout_at** | **datetime** | Creation timestamp | [optional] 

## Example

```python
from stayforge.models.order_input import OrderInput

# TODO update the JSON string below
json = "{}"
# create an instance of OrderInput from a JSON string
order_input_instance = OrderInput.from_json(json)
# print the JSON string representation of the object
print(OrderInput.to_json())

# convert the object into a dict
order_input_dict = order_input_instance.to_dict()
# create an instance of OrderInput from a dict
order_input_from_dict = OrderInput.from_dict(order_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


