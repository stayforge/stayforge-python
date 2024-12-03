# ApiBranchModelsKey


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Reference ID of the key. | [optional] [default to '674f7eee58103c1ed7a444eb']
**create_at** | **datetime** |  | 
**update_at** | **datetime** |  | [optional] 
**name** | **str** | The name of the hotel key. By default, it combines a base name with a random town. | 
**postcode** | **str** | The postal code of the key location. | [optional] [default to '000-0000']
**address** | **str** | The full effective of the key, including administrative unit, city, town, and detailed location. | [optional] [default to '000-0000']
**telephone** | **str** | The contact telephone number for the key. | 

## Example

```python
from stayforge.models.api_branch_models_key import ApiBranchModelsKey

# TODO update the JSON string below
json = "{}"
# create an instance of ApiBranchModelsKey from a JSON string
api_branch_models_key_instance = ApiBranchModelsKey.from_json(json)
# print the JSON string representation of the object
print(ApiBranchModelsKey.to_json())

# convert the object into a dict
api_branch_models_key_dict = api_branch_models_key_instance.to_dict()
# create an instance of ApiBranchModelsKey from a dict
api_branch_models_key_from_dict = ApiBranchModelsKey.from_dict(api_branch_models_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


