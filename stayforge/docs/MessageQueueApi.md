# stayforge.MessageQueueApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**enqueue_api_mq_stream_post**](MessageQueueApi.md#enqueue_api_mq_stream_post) | **POST** /api/mq/{stream} | Enqueue
[**messages_api_mq_messages_stream_get**](MessageQueueApi.md#messages_api_mq_messages_stream_get) | **GET** /api/mq/messages/{stream} | Messages
[**sized_api_mq_sized_stream_get**](MessageQueueApi.md#sized_api_mq_sized_stream_get) | **GET** /api/mq/sized/{stream} | Sized
[**streams_api_mq_streams_get**](MessageQueueApi.md#streams_api_mq_streams_get) | **GET** /api/mq/streams | Streams


# **enqueue_api_mq_stream_post**
> object enqueue_api_mq_stream_post(stream, mq_enqueue, ttl=ttl)

Enqueue

### Example


```python
import stayforge
from stayforge.models.mq_enqueue import MQEnqueue
from stayforge.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = stayforge.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with stayforge.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = stayforge.MessageQueueApi(api_client)
    stream = 'stream_example' # str | 
    mq_enqueue = stayforge.MQEnqueue() # MQEnqueue | 
    ttl = -1 # int |  (optional) (default to -1)

    try:
        # Enqueue
        api_response = api_instance.enqueue_api_mq_stream_post(stream, mq_enqueue, ttl=ttl)
        print("The response of MessageQueueApi->enqueue_api_mq_stream_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessageQueueApi->enqueue_api_mq_stream_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stream** | **str**|  | 
 **mq_enqueue** | [**MQEnqueue**](MQEnqueue.md)|  | 
 **ttl** | **int**|  | [optional] [default to -1]

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **messages_api_mq_messages_stream_get**
> object messages_api_mq_messages_stream_get(stream)

Messages

### Example


```python
import stayforge
from stayforge.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = stayforge.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with stayforge.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = stayforge.MessageQueueApi(api_client)
    stream = 'stream_example' # str | 

    try:
        # Messages
        api_response = api_instance.messages_api_mq_messages_stream_get(stream)
        print("The response of MessageQueueApi->messages_api_mq_messages_stream_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessageQueueApi->messages_api_mq_messages_stream_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stream** | **str**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sized_api_mq_sized_stream_get**
> object sized_api_mq_sized_stream_get(stream)

Sized

### Example


```python
import stayforge
from stayforge.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = stayforge.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with stayforge.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = stayforge.MessageQueueApi(api_client)
    stream = 'stream_example' # str | 

    try:
        # Sized
        api_response = api_instance.sized_api_mq_sized_stream_get(stream)
        print("The response of MessageQueueApi->sized_api_mq_sized_stream_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessageQueueApi->sized_api_mq_sized_stream_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stream** | **str**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **streams_api_mq_streams_get**
> object streams_api_mq_streams_get()

Streams

### Example


```python
import stayforge
from stayforge.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = stayforge.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with stayforge.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = stayforge.MessageQueueApi(api_client)

    try:
        # Streams
        api_response = api_instance.streams_api_mq_streams_get()
        print("The response of MessageQueueApi->streams_api_mq_streams_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessageQueueApi->streams_api_mq_streams_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

