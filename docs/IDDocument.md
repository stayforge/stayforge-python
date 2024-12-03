# IDDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mrz** | **str** |  | [optional] 
**photocopy** | [**Photocopy**](Photocopy.md) |  | [optional] 

## Example

```python
from stayforge.models.id_document import IDDocument

# TODO update the JSON string below
json = "{}"
# create an instance of IDDocument from a JSON string
id_document_instance = IDDocument.from_json(json)
# print the JSON string representation of the object
print(IDDocument.to_json())

# convert the object into a dict
id_document_dict = id_document_instance.to_dict()
# create an instance of IDDocument from a dict
id_document_from_dict = IDDocument.from_dict(id_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


