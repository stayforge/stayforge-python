# Key


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Reference ID of the key. | [optional] [default to '678b211480076d32a7bb2d32']
**create_at** | **datetime** |  | 
**update_at** | **datetime** |  | [optional] 
**url** | **str** | The name of the hotel key. By default, it combines a base name with a random town. | 
**num** | **str** | Order number | [optional] [default to '']
**effective_at** | **str** | Effective at | [optional] [default to '2025-01-18T03:33:40.305775Z']
**ineffective_at** | **str** | Ineffective at | [optional] [default to '2025-01-19T03:33:40.305803Z']

## Example

```python
from stayforge.models.key import Key

# TODO update the JSON string below
json = "{}"
# create an instance of Key from a JSON string
key_instance = Key.from_json(json)
# print the JSON string representation of the object
print(Key.to_json())

# convert the object into a dict
key_dict = key_instance.to_dict()
# create an instance of Key from a dict
key_from_dict = Key.from_dict(key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


