# KeyValueRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | 
**value** | **str** |  | [optional] 

## Example

```python
from stayforge.models.key_value_request import KeyValueRequest

# TODO update the JSON string below
json = "{}"
# create an instance of KeyValueRequest from a JSON string
key_value_request_instance = KeyValueRequest.from_json(json)
# print the JSON string representation of the object
print(KeyValueRequest.to_json())

# convert the object into a dict
key_value_request_dict = key_value_request_instance.to_dict()
# create an instance of KeyValueRequest from a dict
key_value_request_from_dict = KeyValueRequest.from_dict(key_value_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


