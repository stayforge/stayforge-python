# stayforge.BranchApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**branch_create**](BranchApi.md#branch_create) | **POST** /api/v1/branch/ | branch_create
[**branch_delete**](BranchApi.md#branch_delete) | **DELETE** /api/v1/branch/{id} | branch_delete
[**branch_get**](BranchApi.md#branch_get) | **GET** /api/v1/branch/{id} | branch_get
[**branch_list**](BranchApi.md#branch_list) | **GET** /api/v1/branch/ | branch_list
[**branch_update**](BranchApi.md#branch_update) | **PUT** /api/v1/branch/{id} | branch_update


# **branch_create**
> BranchBase branch_create(branch_base)

branch_create

branch_create operation for branch

### Example


```python
import stayforge
from stayforge.models.branch_base import BranchBase
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
    api_instance = stayforge.BranchApi(api_client)
    branch_base = stayforge.BranchBase() # BranchBase | 

    try:
        # branch_create
        api_response = api_instance.branch_create(branch_base)
        print("The response of BranchApi->branch_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BranchApi->branch_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **branch_base** | [**BranchBase**](BranchBase.md)|  | 

### Return type

[**BranchBase**](BranchBase.md)

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

# **branch_delete**
> BranchBase branch_delete(id)

branch_delete

branch_delete operation for branch

### Example


```python
import stayforge
from stayforge.models.branch_base import BranchBase
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
    api_instance = stayforge.BranchApi(api_client)
    id = 'id_example' # str | 

    try:
        # branch_delete
        api_response = api_instance.branch_delete(id)
        print("The response of BranchApi->branch_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BranchApi->branch_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**BranchBase**](BranchBase.md)

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

# **branch_get**
> List[BranchBase] branch_get(id)

branch_get

branch_get operation for branch

### Example


```python
import stayforge
from stayforge.models.branch_base import BranchBase
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
    api_instance = stayforge.BranchApi(api_client)
    id = 'id_example' # str | 

    try:
        # branch_get
        api_response = api_instance.branch_get(id)
        print("The response of BranchApi->branch_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BranchApi->branch_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**List[BranchBase]**](BranchBase.md)

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

# **branch_list**
> List[BranchBase] branch_list()

branch_list

branch_list operation for branch

### Example


```python
import stayforge
from stayforge.models.branch_base import BranchBase
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
    api_instance = stayforge.BranchApi(api_client)

    try:
        # branch_list
        api_response = api_instance.branch_list()
        print("The response of BranchApi->branch_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BranchApi->branch_list: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[BranchBase]**](BranchBase.md)

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

# **branch_update**
> BranchBase branch_update(id, branch_base)

branch_update

branch_update operation for branch

### Example


```python
import stayforge
from stayforge.models.branch_base import BranchBase
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
    api_instance = stayforge.BranchApi(api_client)
    id = 'id_example' # str | 
    branch_base = stayforge.BranchBase() # BranchBase | 

    try:
        # branch_update
        api_response = api_instance.branch_update(id, branch_base)
        print("The response of BranchApi->branch_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BranchApi->branch_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **branch_base** | [**BranchBase**](BranchBase.md)|  | 

### Return type

[**BranchBase**](BranchBase.md)

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

