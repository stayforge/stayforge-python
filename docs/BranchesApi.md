# openapi_client.BranchesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_key_api_branch_post**](BranchesApi.md#create_key_api_branch_post) | **POST** /api/branch/ | Create Key
[**delete_key_api_branch_id_delete**](BranchesApi.md#delete_key_api_branch_id_delete) | **DELETE** /api/branch/&lt;id&gt; | Delete Key
[**get_key_api_branch_id_get**](BranchesApi.md#get_key_api_branch_id_get) | **GET** /api/branch/&lt;id&gt; | Get Key
[**get_keys_api_branch_get**](BranchesApi.md#get_keys_api_branch_get) | **GET** /api/branch/ | Get Keys
[**put_key_api_branch_id_put**](BranchesApi.md#put_key_api_branch_id_put) | **PUT** /api/branch/&lt;id&gt; | Put Key


# **create_key_api_branch_post**
> ApiBranchViewKeyResponses create_key_api_branch_post(api_branch_models_key_input)

Create Key

### Example


```python
import openapi_client
from openapi_client.models.api_branch_models_key_input import ApiBranchModelsKeyInput
from openapi_client.models.api_branch_view_key_responses import ApiBranchViewKeyResponses
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.BranchesApi(api_client)
    api_branch_models_key_input = openapi_client.ApiBranchModelsKeyInput() # ApiBranchModelsKeyInput | 

    try:
        # Create Key
        api_response = api_instance.create_key_api_branch_post(api_branch_models_key_input)
        print("The response of BranchesApi->create_key_api_branch_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BranchesApi->create_key_api_branch_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_branch_models_key_input** | [**ApiBranchModelsKeyInput**](ApiBranchModelsKeyInput.md)|  | 

### Return type

[**ApiBranchViewKeyResponses**](ApiBranchViewKeyResponses.md)

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

# **delete_key_api_branch_id_delete**
> ApiBranchViewKeyResponses delete_key_api_branch_id_delete(id)

Delete Key

### Example


```python
import openapi_client
from openapi_client.models.api_branch_view_key_responses import ApiBranchViewKeyResponses
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.BranchesApi(api_client)
    id = 'id_example' # str | 

    try:
        # Delete Key
        api_response = api_instance.delete_key_api_branch_id_delete(id)
        print("The response of BranchesApi->delete_key_api_branch_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BranchesApi->delete_key_api_branch_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ApiBranchViewKeyResponses**](ApiBranchViewKeyResponses.md)

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

# **get_key_api_branch_id_get**
> ApiBranchViewKeyResponses get_key_api_branch_id_get(id)

Get Key

### Example


```python
import openapi_client
from openapi_client.models.api_branch_view_key_responses import ApiBranchViewKeyResponses
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.BranchesApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get Key
        api_response = api_instance.get_key_api_branch_id_get(id)
        print("The response of BranchesApi->get_key_api_branch_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BranchesApi->get_key_api_branch_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ApiBranchViewKeyResponses**](ApiBranchViewKeyResponses.md)

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

# **get_keys_api_branch_get**
> ApiBranchViewKeyResponses get_keys_api_branch_get(name=name, address=address, telephone=telephone)

Get Keys

### Example


```python
import openapi_client
from openapi_client.models.api_branch_view_key_responses import ApiBranchViewKeyResponses
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.BranchesApi(api_client)
    name = 'name_example' # str |  (optional)
    address = 'address_example' # str |  (optional)
    telephone = 'telephone_example' # str |  (optional)

    try:
        # Get Keys
        api_response = api_instance.get_keys_api_branch_get(name=name, address=address, telephone=telephone)
        print("The response of BranchesApi->get_keys_api_branch_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BranchesApi->get_keys_api_branch_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 
 **address** | **str**|  | [optional] 
 **telephone** | **str**|  | [optional] 

### Return type

[**ApiBranchViewKeyResponses**](ApiBranchViewKeyResponses.md)

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

# **put_key_api_branch_id_put**
> ApiBranchViewKeyResponses put_key_api_branch_id_put(id, api_branch_models_key_input)

Put Key

### Example


```python
import openapi_client
from openapi_client.models.api_branch_models_key_input import ApiBranchModelsKeyInput
from openapi_client.models.api_branch_view_key_responses import ApiBranchViewKeyResponses
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.BranchesApi(api_client)
    id = 'id_example' # str | 
    api_branch_models_key_input = openapi_client.ApiBranchModelsKeyInput() # ApiBranchModelsKeyInput | 

    try:
        # Put Key
        api_response = api_instance.put_key_api_branch_id_put(id, api_branch_models_key_input)
        print("The response of BranchesApi->put_key_api_branch_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BranchesApi->put_key_api_branch_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **api_branch_models_key_input** | [**ApiBranchModelsKeyInput**](ApiBranchModelsKeyInput.md)|  | 

### Return type

[**ApiBranchViewKeyResponses**](ApiBranchViewKeyResponses.md)

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

