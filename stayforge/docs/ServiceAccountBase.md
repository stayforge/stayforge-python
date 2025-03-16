# ServiceAccountBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | [**Account**](Account.md) |  | 

## Example

```python
from stayforge.models.service_account_base import ServiceAccountBase

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceAccountBase from a JSON string
service_account_base_instance = ServiceAccountBase.from_json(json)
# print the JSON string representation of the object
print(ServiceAccountBase.to_json())

# convert the object into a dict
service_account_base_dict = service_account_base_instance.to_dict()
# create an instance of ServiceAccountBase from a dict
service_account_base_from_dict = ServiceAccountBase.from_dict(service_account_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


