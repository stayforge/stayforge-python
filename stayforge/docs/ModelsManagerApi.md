# stayforge.ModelsManagerApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_models_profile_api_models_post**](ModelsManagerApi.md#create_models_profile_api_models_post) | **POST** /api/models/ | Create Models Profile
[**delete_models_profile_api_models_id_delete**](ModelsManagerApi.md#delete_models_profile_api_models_id_delete) | **DELETE** /api/models/{id} | Delete Models Profile
[**get_models_profile_api_models_get**](ModelsManagerApi.md#get_models_profile_api_models_get) | **GET** /api/models/ | Get Models Profile
[**get_models_profile_api_models_id_get**](ModelsManagerApi.md#get_models_profile_api_models_id_get) | **GET** /api/models/{id} | Get Models Profile
[**put_models_profile_api_models_id_put**](ModelsManagerApi.md#put_models_profile_api_models_id_put) | **PUT** /api/models/{id} | Put Models Profile


# **create_models_profile_api_models_post**
> ModelsManagerResponses create_models_profile_api_models_post(models_manager_input)

Create Models Profile

### Example


```python
import stayforge
from stayforge.models.models_manager_input import ModelsManagerInput
from stayforge.models.models_manager_responses import ModelsManagerResponses
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
    api_instance = stayforge.ModelsManagerApi(api_client)
    models_manager_input = stayforge.ModelsManagerInput() # ModelsManagerInput | 

    try:
        # Create Models Profile
        api_response = api_instance.create_models_profile_api_models_post(models_manager_input)
        print("The response of ModelsManagerApi->create_models_profile_api_models_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModelsManagerApi->create_models_profile_api_models_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **models_manager_input** | [**ModelsManagerInput**](ModelsManagerInput.md)|  | 

### Return type

[**ModelsManagerResponses**](ModelsManagerResponses.md)

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

# **delete_models_profile_api_models_id_delete**
> ModelsManagerResponses delete_models_profile_api_models_id_delete(id)

Delete Models Profile

### Example


```python
import stayforge
from stayforge.models.models_manager_responses import ModelsManagerResponses
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
    api_instance = stayforge.ModelsManagerApi(api_client)
    id = 'id_example' # str | 

    try:
        # Delete Models Profile
        api_response = api_instance.delete_models_profile_api_models_id_delete(id)
        print("The response of ModelsManagerApi->delete_models_profile_api_models_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModelsManagerApi->delete_models_profile_api_models_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ModelsManagerResponses**](ModelsManagerResponses.md)

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

# **get_models_profile_api_models_get**
> ModelsManagerResponses get_models_profile_api_models_get(model_name=model_name, endpoint=endpoint, catch_path=catch_path, catch_method=catch_method, catch_status=catch_status)

Get Models Profile

### Example


```python
import stayforge
from stayforge.models.models_manager_responses import ModelsManagerResponses
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
    api_instance = stayforge.ModelsManagerApi(api_client)
    model_name = 'model_name_example' # str | A friendly name you can remember. (optional)
    endpoint = 'endpoint_example' # str | The URL endpoint where the model is to be sent, e.g., `https://youapplocation/model/endpoint`. (optional)
    catch_path = 'catch_path_example' # str | This refers to the API within Stayforage, the path part of its URL e.g., `/api/order/`. (optional)
    catch_method = 'catch_method_example' # str | Only configured HTTP methods (e.g., `POST`) that the request will capture. (optional)
    catch_status = 56 # int | Only configured HTTP status code (e.g., `200`) that the request will capture. (optional)

    try:
        # Get Models Profile
        api_response = api_instance.get_models_profile_api_models_get(model_name=model_name, endpoint=endpoint, catch_path=catch_path, catch_method=catch_method, catch_status=catch_status)
        print("The response of ModelsManagerApi->get_models_profile_api_models_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModelsManagerApi->get_models_profile_api_models_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model_name** | **str**| A friendly name you can remember. | [optional] 
 **endpoint** | **str**| The URL endpoint where the model is to be sent, e.g., &#x60;https://youapplocation/model/endpoint&#x60;. | [optional] 
 **catch_path** | **str**| This refers to the API within Stayforage, the path part of its URL e.g., &#x60;/api/order/&#x60;. | [optional] 
 **catch_method** | **str**| Only configured HTTP methods (e.g., &#x60;POST&#x60;) that the request will capture. | [optional] 
 **catch_status** | **int**| Only configured HTTP status code (e.g., &#x60;200&#x60;) that the request will capture. | [optional] 

### Return type

[**ModelsManagerResponses**](ModelsManagerResponses.md)

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

# **get_models_profile_api_models_id_get**
> ModelsManagerResponses get_models_profile_api_models_id_get(id)

Get Models Profile

### Example


```python
import stayforge
from stayforge.models.models_manager_responses import ModelsManagerResponses
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
    api_instance = stayforge.ModelsManagerApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get Models Profile
        api_response = api_instance.get_models_profile_api_models_id_get(id)
        print("The response of ModelsManagerApi->get_models_profile_api_models_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModelsManagerApi->get_models_profile_api_models_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ModelsManagerResponses**](ModelsManagerResponses.md)

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

# **put_models_profile_api_models_id_put**
> ModelsManagerResponses put_models_profile_api_models_id_put(id, models_manager_input)

Put Models Profile

### Example


```python
import stayforge
from stayforge.models.models_manager_input import ModelsManagerInput
from stayforge.models.models_manager_responses import ModelsManagerResponses
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
    api_instance = stayforge.ModelsManagerApi(api_client)
    id = 'id_example' # str | 
    models_manager_input = stayforge.ModelsManagerInput() # ModelsManagerInput | 

    try:
        # Put Models Profile
        api_response = api_instance.put_models_profile_api_models_id_put(id, models_manager_input)
        print("The response of ModelsManagerApi->put_models_profile_api_models_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModelsManagerApi->put_models_profile_api_models_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **models_manager_input** | [**ModelsManagerInput**](ModelsManagerInput.md)|  | 

### Return type

[**ModelsManagerResponses**](ModelsManagerResponses.md)

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

