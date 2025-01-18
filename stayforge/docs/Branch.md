# Branch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Reference ID of the key. | [optional] [default to '678b9e3638df7c91598cf548']
**create_at** | **datetime** |  | 
**update_at** | **datetime** |  | [optional] 
**name** | **str** | The name of the hotel branch. By default, it combines a base name with a random town. | 
**postcode** | **str** | The postal code of the branch location. | [optional] [default to '000-0000']
**address** | **str** | The full effective of the branch, including administrative unit, city, town, and detailed location. | [optional] [default to '000-0000']
**telephone** | **str** | The contact telephone number for the branch. | 

## Example

```python
from stayforge.models.branch import Branch

# TODO update the JSON string below
json = "{}"
# create an instance of Branch from a JSON string
branch_instance = Branch.from_json(json)
# print the JSON string representation of the object
print(Branch.to_json())

# convert the object into a dict
branch_dict = branch_instance.to_dict()
# create an instance of Branch from a dict
branch_from_dict = Branch.from_dict(branch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


