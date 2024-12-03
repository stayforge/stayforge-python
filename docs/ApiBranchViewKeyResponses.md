# ApiBranchViewKeyResponses


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ApiBranchModelsKey]**](ApiBranchModelsKey.md) |  | 
**detail** | **str** |  | [optional] [default to 'Successfully.']
**status** | **int** |  | [optional] [default to 200]
**used_time** | **float** |  | [optional] 
**stayforge** | [**Stayforge**](Stayforge.md) |  | [optional] 

## Example

```python
from stayforge.models.api_branch_view_key_responses import ApiBranchViewKeyResponses

# TODO update the JSON string below
json = "{}"
# create an instance of ApiBranchViewKeyResponses from a JSON string
api_branch_view_key_responses_instance = ApiBranchViewKeyResponses.from_json(json)
# print the JSON string representation of the object
print(ApiBranchViewKeyResponses.to_json())

# convert the object into a dict
api_branch_view_key_responses_dict = api_branch_view_key_responses_instance.to_dict()
# create an instance of ApiBranchViewKeyResponses from a dict
api_branch_view_key_responses_from_dict = ApiBranchViewKeyResponses.from_dict(api_branch_view_key_responses_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


