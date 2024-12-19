# Order


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Reference ID of the key. | [optional] [default to '67642a9def9125ab1e5084ec']
**create_at** | **datetime** |  | 
**update_at** | **datetime** |  | [optional] 
**num** | **str** | Order number | [optional] 
**room_id** | **str** | Room ID | [optional] 
**guest** | [**Guest**](Guest.md) | Guest information | [optional] 
**type** | **str** | OrderType | 
**scheduled_checkin_at** | **datetime** | Creation timestamp | [optional] 
**scheduled_checkout_at** | **datetime** | Creation timestamp | [optional] 

## Example

```python
from stayforge.models.order import Order

# TODO update the JSON string below
json = "{}"
# create an instance of Order from a JSON string
order_instance = Order.from_json(json)
# print the JSON string representation of the object
print(Order.to_json())

# convert the object into a dict
order_dict = order_instance.to_dict()
# create an instance of Order from a dict
order_from_dict = Order.from_dict(order_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


