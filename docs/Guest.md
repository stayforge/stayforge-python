# Guest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** |  | [optional] 
**middle_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**gender** | **str** |  | [optional] 
**birthday** | **str** |  | [optional] 
**nationality** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**phone_number** | **str** |  | [optional] 
**address** | **str** |  | [optional] 
**occupation** | **str** |  | [optional] 
**passport_number** | **str** |  | [optional] 
**id_document** | [**IDDocument**](IDDocument.md) |  | 

## Example

```python
from openapi_client.models.guest import Guest

# TODO update the JSON string below
json = "{}"
# create an instance of Guest from a JSON string
guest_instance = Guest.from_json(json)
# print the JSON string representation of the object
print(Guest.to_json())

# convert the object into a dict
guest_dict = guest_instance.to_dict()
# create an instance of Guest from a dict
guest_from_dict = Guest.from_dict(guest_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


