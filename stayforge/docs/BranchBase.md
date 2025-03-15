# BranchBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the hotel branch. By default, it combines a base name with a random town. | 
**postcode** | **str** | The postal code of the branch location. | [optional] [default to '000-0000']
**address** | **str** | The full effective of the branch, including administrative unit, city, town, and detailed location. | [optional] [default to '000-0000']
**telephone** | **str** | The contact telephone number for the branch. | 

## Example

```python
from stayforge.models.branch_base import BranchBase

# TODO update the JSON string below
json = "{}"
# create an instance of BranchBase from a JSON string
branch_base_instance = BranchBase.from_json(json)
# print the JSON string representation of the object
print(BranchBase.to_json())

# convert the object into a dict
branch_base_dict = branch_base_instance.to_dict()
# create an instance of BranchBase from a dict
branch_base_from_dict = BranchBase.from_dict(branch_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


