# MQEnqueue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | The content of the message to be enqueued. | [optional] 

## Example

```python
from stayforge.models.mq_enqueue import MQEnqueue

# TODO update the JSON string below
json = "{}"
# create an instance of MQEnqueue from a JSON string
mq_enqueue_instance = MQEnqueue.from_json(json)
# print the JSON string representation of the object
print(MQEnqueue.to_json())

# convert the object into a dict
mq_enqueue_dict = mq_enqueue_instance.to_dict()
# create an instance of MQEnqueue from a dict
mq_enqueue_from_dict = MQEnqueue.from_dict(mq_enqueue_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


