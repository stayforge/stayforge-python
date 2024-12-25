# stayforge.BranchesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_branch_api_branch_post**](BranchesApi.md#create_branch_api_branch_post) | **POST** /api/branch/ | Create Branch
[**delete_branch_api_branch_id_delete**](BranchesApi.md#delete_branch_api_branch_id_delete) | **DELETE** /api/branch/{id} | Delete Branch
[**get_branch_api_branch_id_get**](BranchesApi.md#get_branch_api_branch_id_get) | **GET** /api/branch/{id} | Get Branch
[**get_branches_api_branch_get**](BranchesApi.md#get_branches_api_branch_get) | **GET** /api/branch/ | Get Branches
[**put_branch_api_branch_id_put**](BranchesApi.md#put_branch_api_branch_id_put) | **PUT** /api/branch/{id} | Put Branch


# **create_branch_api_branch_post**
> BranchResponses create_branch_api_branch_post(branch_input)

Create Branch

### Example


```python
import stayforge
from stayforge.models.branch_input import BranchInput
from stayforge.models.branch_responses import BranchResponses
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
    api_instance = stayforge.BranchesApi(api_client)
    branch_input = stayforge.BranchInput() # BranchInput | 

    try:
        # Create Branch
        api_response = api_instance.create_branch_api_branch_post(branch_input)
        print("The response of BranchesApi->create_branch_api_branch_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BranchesApi->create_branch_api_branch_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **branch_input** | [**BranchInput**](BranchInput.md)|  | 

### Return type

[**BranchResponses**](BranchResponses.md)

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

# **delete_branch_api_branch_id_delete**
> BranchResponses delete_branch_api_branch_id_delete(id)

Delete Branch

### Example


```python
import stayforge
from stayforge.models.branch_responses import BranchResponses
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
    api_instance = stayforge.BranchesApi(api_client)
    id = 'id_example' # str | 

    try:
        # Delete Branch
        api_response = api_instance.delete_branch_api_branch_id_delete(id)
        print("The response of BranchesApi->delete_branch_api_branch_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BranchesApi->delete_branch_api_branch_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**BranchResponses**](BranchResponses.md)

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

# **get_branch_api_branch_id_get**
> BranchResponses get_branch_api_branch_id_get(id)

Get Branch

### Example


```python
import stayforge
from stayforge.models.branch_responses import BranchResponses
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
    api_instance = stayforge.BranchesApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get Branch
        api_response = api_instance.get_branch_api_branch_id_get(id)
        print("The response of BranchesApi->get_branch_api_branch_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BranchesApi->get_branch_api_branch_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**BranchResponses**](BranchResponses.md)

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

# **get_branches_api_branch_get**
> BranchResponses get_branches_api_branch_get(name=name, address=address, telephone=telephone)

Get Branches

### Example


```python
import stayforge
from stayforge.models.branch_responses import BranchResponses
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
    api_instance = stayforge.BranchesApi(api_client)
    name = 'name_example' # str |  (optional)
    address = 'address_example' # str |  (optional)
    telephone = 'telephone_example' # str |  (optional)

    try:
        # Get Branches
        api_response = api_instance.get_branches_api_branch_get(name=name, address=address, telephone=telephone)
        print("The response of BranchesApi->get_branches_api_branch_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BranchesApi->get_branches_api_branch_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 
 **address** | **str**|  | [optional] 
 **telephone** | **str**|  | [optional] 

### Return type

[**BranchResponses**](BranchResponses.md)

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

# **put_branch_api_branch_id_put**
> BranchResponses put_branch_api_branch_id_put(id, branch_input)

Put Branch

### Example


```python
import stayforge
from stayforge.models.branch_input import BranchInput
from stayforge.models.branch_responses import BranchResponses
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
    api_instance = stayforge.BranchesApi(api_client)
    id = 'id_example' # str | 
    branch_input = stayforge.BranchInput() # BranchInput | 

    try:
        # Put Branch
        api_response = api_instance.put_branch_api_branch_id_put(id, branch_input)
        print("The response of BranchesApi->put_branch_api_branch_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BranchesApi->put_branch_api_branch_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **branch_input** | [**BranchInput**](BranchInput.md)|  | 

### Return type

[**BranchResponses**](BranchResponses.md)

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

