# stayforge.ModelsEtcdApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_data_api_models_model_etcd_delete_key_delete**](ModelsEtcdApi.md#delete_data_api_models_model_etcd_delete_key_delete) | **DELETE** /api/models/{model}/etcd/delete/{key} | Delete Data
[**get_data_api_models_model_etcd_get_key_get**](ModelsEtcdApi.md#get_data_api_models_model_etcd_get_key_get) | **GET** /api/models/{model}/etcd/get/{key} | Get Data
[**put_data_api_models_model_etcd_put_post**](ModelsEtcdApi.md#put_data_api_models_model_etcd_put_post) | **POST** /api/models/{model}/etcd/put | Put Data


# **delete_data_api_models_model_etcd_delete_key_delete**
> object delete_data_api_models_model_etcd_delete_key_delete(key, model)

Delete Data

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
    api_instance = stayforge.ModelsEtcdApi(api_client)
    key = 'key_example' # str | 
    model = 'model_example' # str | 

    try:
        # Delete Data
        api_response = api_instance.delete_data_api_models_model_etcd_delete_key_delete(key, model)
        print("The response of ModelsEtcdApi->delete_data_api_models_model_etcd_delete_key_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModelsEtcdApi->delete_data_api_models_model_etcd_delete_key_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**|  | 
 **model** | **str**|  | 

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

# **get_data_api_models_model_etcd_get_key_get**
> object get_data_api_models_model_etcd_get_key_get(key, model)

Get Data

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
    api_instance = stayforge.ModelsEtcdApi(api_client)
    key = 'key_example' # str | 
    model = 'model_example' # str | 

    try:
        # Get Data
        api_response = api_instance.get_data_api_models_model_etcd_get_key_get(key, model)
        print("The response of ModelsEtcdApi->get_data_api_models_model_etcd_get_key_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModelsEtcdApi->get_data_api_models_model_etcd_get_key_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**|  | 
 **model** | **str**|  | 

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

# **put_data_api_models_model_etcd_put_post**
> object put_data_api_models_model_etcd_put_post(model, key_value_request)

Put Data

### Example


```python
import stayforge
from stayforge.models.key_value_request import KeyValueRequest
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
    api_instance = stayforge.ModelsEtcdApi(api_client)
    model = 'model_example' # str | 
    key_value_request = stayforge.KeyValueRequest() # KeyValueRequest | 

    try:
        # Put Data
        api_response = api_instance.put_data_api_models_model_etcd_put_post(model, key_value_request)
        print("The response of ModelsEtcdApi->put_data_api_models_model_etcd_put_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModelsEtcdApi->put_data_api_models_model_etcd_put_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model** | **str**|  | 
 **key_value_request** | [**KeyValueRequest**](KeyValueRequest.md)|  | 

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

