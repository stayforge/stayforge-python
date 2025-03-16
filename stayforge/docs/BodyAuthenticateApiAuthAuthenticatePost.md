# BodyAuthenticateApiAuthAuthenticatePost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | **str** | Service Account Username (Must be an email address) | 
**secret** | **str** | Service Account API Key (Or password for human user) | 

## Example

```python
from stayforge.models.body_authenticate_api_auth_authenticate_post import BodyAuthenticateApiAuthAuthenticatePost

# TODO update the JSON string below
json = "{}"
# create an instance of BodyAuthenticateApiAuthAuthenticatePost from a JSON string
body_authenticate_api_auth_authenticate_post_instance = BodyAuthenticateApiAuthAuthenticatePost.from_json(json)
# print the JSON string representation of the object
print(BodyAuthenticateApiAuthAuthenticatePost.to_json())

# convert the object into a dict
body_authenticate_api_auth_authenticate_post_dict = body_authenticate_api_auth_authenticate_post_instance.to_dict()
# create an instance of BodyAuthenticateApiAuthAuthenticatePost from a dict
body_authenticate_api_auth_authenticate_post_from_dict = BodyAuthenticateApiAuthAuthenticatePost.from_dict(body_authenticate_api_auth_authenticate_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


