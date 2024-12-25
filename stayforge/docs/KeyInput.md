# KeyInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The name of the hotel key. By default, it combines a base name with a random town. | 
**num** | **str** | Order number | [optional] [default to '']
**effective_at** | **str** | Effective at | [optional] [default to '2024-12-25T10:42:56.038547Z']
**ineffective_at** | **str** | Ineffective at | [optional] [default to '2024-12-26T10:42:56.038575Z']

## Example

```python
from stayforge.models.key_input import KeyInput

# TODO update the JSON string below
json = "{}"
# create an instance of KeyInput from a JSON string
key_input_instance = KeyInput.from_json(json)
# print the JSON string representation of the object
print(KeyInput.to_json())

# convert the object into a dict
key_input_dict = key_input_instance.to_dict()
# create an instance of KeyInput from a dict
key_input_from_dict = KeyInput.from_dict(key_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


