# BranchResponses


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Branch]**](Branch.md) |  | 
**detail** | **str** |  | [optional] [default to 'Successfully.']
**status** | **int** |  | [optional] [default to 200]
**used_time** | **float** |  | [optional] 
**stayforge** | [**Stayforge**](Stayforge.md) |  | [optional] 

## Example

```python
from stayforge.models.branch_responses import BranchResponses

# TODO update the JSON string below
json = "{}"
# create an instance of BranchResponses from a JSON string
branch_responses_instance = BranchResponses.from_json(json)
# print the JSON string representation of the object
print(BranchResponses.to_json())

# convert the object into a dict
branch_responses_dict = branch_responses_instance.to_dict()
# create an instance of BranchResponses from a dict
branch_responses_from_dict = BranchResponses.from_dict(branch_responses_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


