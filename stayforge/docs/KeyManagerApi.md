# stayforge.KeyManagerApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_key_api_key_post**](KeyManagerApi.md#create_key_api_key_post) | **POST** /api/key/ | Create Key
[**delete_key_api_key_id_delete**](KeyManagerApi.md#delete_key_api_key_id_delete) | **DELETE** /api/key/{id} | Delete Key
[**get_key_api_key_id_get**](KeyManagerApi.md#get_key_api_key_id_get) | **GET** /api/key/{id} | Get Key
[**get_key_by_num_api_key_num_num_get**](KeyManagerApi.md#get_key_by_num_api_key_num_num_get) | **GET** /api/key/num/{num} | Get Key By Num
[**put_key_api_key_id_put**](KeyManagerApi.md#put_key_api_key_id_put) | **PUT** /api/key/{id} | Put Key


# **create_key_api_key_post**
> ApiKeyManagerViewKeyResponses create_key_api_key_post(api_key_manager_models_key_input)

Create Key

### Example


```python
import stayforge
from stayforge.models.api_key_manager_models_key_input import ApiKeyManagerModelsKeyInput
from stayforge.models.api_key_manager_view_key_responses import ApiKeyManagerViewKeyResponses
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
    api_instance = stayforge.KeyManagerApi(api_client)
    api_key_manager_models_key_input = stayforge.ApiKeyManagerModelsKeyInput() # ApiKeyManagerModelsKeyInput | 

    try:
        # Create Key
        api_response = api_instance.create_key_api_key_post(api_key_manager_models_key_input)
        print("The response of KeyManagerApi->create_key_api_key_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KeyManagerApi->create_key_api_key_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key_manager_models_key_input** | [**ApiKeyManagerModelsKeyInput**](ApiKeyManagerModelsKeyInput.md)|  | 

### Return type

[**ApiKeyManagerViewKeyResponses**](ApiKeyManagerViewKeyResponses.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**409** | Resource maybe created. But can&#39;t found it. |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_key_api_key_id_delete**
> ApiKeyManagerViewKeyResponses delete_key_api_key_id_delete(id)

Delete Key

### Example


```python
import stayforge
from stayforge.models.api_key_manager_view_key_responses import ApiKeyManagerViewKeyResponses
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
    api_instance = stayforge.KeyManagerApi(api_client)
    id = 'id_example' # str | 

    try:
        # Delete Key
        api_response = api_instance.delete_key_api_key_id_delete(id)
        print("The response of KeyManagerApi->delete_key_api_key_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KeyManagerApi->delete_key_api_key_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ApiKeyManagerViewKeyResponses**](ApiKeyManagerViewKeyResponses.md)

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

# **get_key_api_key_id_get**
> ApiKeyManagerViewKeyResponses get_key_api_key_id_get(id)

Get Key

### Example


```python
import stayforge
from stayforge.models.api_key_manager_view_key_responses import ApiKeyManagerViewKeyResponses
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
    api_instance = stayforge.KeyManagerApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get Key
        api_response = api_instance.get_key_api_key_id_get(id)
        print("The response of KeyManagerApi->get_key_api_key_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KeyManagerApi->get_key_api_key_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ApiKeyManagerViewKeyResponses**](ApiKeyManagerViewKeyResponses.md)

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

# **get_key_by_num_api_key_num_num_get**
> ApiKeyManagerViewKeyResponses get_key_by_num_api_key_num_num_get(num)

Get Key By Num

### Example


```python
import stayforge
from stayforge.models.api_key_manager_view_key_responses import ApiKeyManagerViewKeyResponses
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
    api_instance = stayforge.KeyManagerApi(api_client)
    num = 'num_example' # str | Order Num

    try:
        # Get Key By Num
        api_response = api_instance.get_key_by_num_api_key_num_num_get(num)
        print("The response of KeyManagerApi->get_key_by_num_api_key_num_num_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KeyManagerApi->get_key_by_num_api_key_num_num_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **num** | **str**| Order Num | 

### Return type

[**ApiKeyManagerViewKeyResponses**](ApiKeyManagerViewKeyResponses.md)

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

# **put_key_api_key_id_put**
> ApiKeyManagerViewKeyResponses put_key_api_key_id_put(id, api_key_manager_models_key_input)

Put Key

### Example


```python
import stayforge
from stayforge.models.api_key_manager_models_key_input import ApiKeyManagerModelsKeyInput
from stayforge.models.api_key_manager_view_key_responses import ApiKeyManagerViewKeyResponses
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
    api_instance = stayforge.KeyManagerApi(api_client)
    id = 'id_example' # str | 
    api_key_manager_models_key_input = stayforge.ApiKeyManagerModelsKeyInput() # ApiKeyManagerModelsKeyInput | 

    try:
        # Put Key
        api_response = api_instance.put_key_api_key_id_put(id, api_key_manager_models_key_input)
        print("The response of KeyManagerApi->put_key_api_key_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KeyManagerApi->put_key_api_key_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **api_key_manager_models_key_input** | [**ApiKeyManagerModelsKeyInput**](ApiKeyManagerModelsKeyInput.md)|  | 

### Return type

[**ApiKeyManagerViewKeyResponses**](ApiKeyManagerViewKeyResponses.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**409** | Resource maybe changed. But can&#39;t found it. |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

