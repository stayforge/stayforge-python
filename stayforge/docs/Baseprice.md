# Baseprice

Base price. If you set a price strategy, the price will automatically increase according to the strategy.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from stayforge.models.baseprice import Baseprice

# TODO update the JSON string below
json = "{}"
# create an instance of Baseprice from a JSON string
baseprice_instance = Baseprice.from_json(json)
# print the JSON string representation of the object
print(Baseprice.to_json())

# convert the object into a dict
baseprice_dict = baseprice_instance.to_dict()
# create an instance of Baseprice from a dict
baseprice_from_dict = Baseprice.from_dict(baseprice_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


