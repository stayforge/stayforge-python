# Key


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Reference ID of the key. | [optional] [default to '676c2799cabb04bdf96759f9']
**create_at** | **datetime** |  | 
**update_at** | **datetime** |  | [optional] 
**url** | **str** | The name of the hotel key. By default, it combines a base name with a random town. | 
**num** | **str** | Order number | [optional] [default to '']
**effective_at** | **str** | Effective at | [optional] [default to '2024-12-25T15:41:13.178342Z']
**ineffective_at** | **str** | Ineffective at | [optional] [default to '2024-12-26T15:41:13.178398Z']

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


