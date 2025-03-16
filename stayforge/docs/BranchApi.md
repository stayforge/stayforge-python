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
> BranchBase branch_create(account, service_account_base)

branch_create

branch_create operation for branch

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import stayforge
from stayforge.models.branch_base import BranchBase
from stayforge.models.service_account_base import ServiceAccountBase
from stayforge.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = stayforge.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = stayforge.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with stayforge.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = stayforge.BranchApi(api_client)
    account = 'account_example' # str | 
    service_account_base = stayforge.ServiceAccountBase() # ServiceAccountBase | 

    try:
        # branch_create
        api_response = api_instance.branch_create(account, service_account_base)
        print("The response of BranchApi->branch_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BranchApi->branch_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**|  | 
 **service_account_base** | [**ServiceAccountBase**](ServiceAccountBase.md)|  | 

### Return type

[**BranchBase**](BranchBase.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

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
> BranchBase branch_delete(id, account)

branch_delete

branch_delete operation for branch

### Example

* Bearer (JWT) Authentication (BearerAuth):

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

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = stayforge.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with stayforge.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = stayforge.BranchApi(api_client)
    id = 'id_example' # str | 
    account = 'account_example' # str | 

    try:
        # branch_delete
        api_response = api_instance.branch_delete(id, account)
        print("The response of BranchApi->branch_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BranchApi->branch_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **account** | **str**|  | 

### Return type

[**BranchBase**](BranchBase.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

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
> List[BranchBase] branch_get(id, account)

branch_get

branch_get operation for branch

### Example

* Bearer (JWT) Authentication (BearerAuth):

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

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = stayforge.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with stayforge.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = stayforge.BranchApi(api_client)
    id = 'id_example' # str | 
    account = 'account_example' # str | 

    try:
        # branch_get
        api_response = api_instance.branch_get(id, account)
        print("The response of BranchApi->branch_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BranchApi->branch_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **account** | **str**|  | 

### Return type

[**List[BranchBase]**](BranchBase.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

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
> List[BranchBase] branch_list(account)

branch_list

branch_list operation for branch

### Example

* Bearer (JWT) Authentication (BearerAuth):

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

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = stayforge.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with stayforge.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = stayforge.BranchApi(api_client)
    account = 'account_example' # str | 

    try:
        # branch_list
        api_response = api_instance.branch_list(account)
        print("The response of BranchApi->branch_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BranchApi->branch_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**|  | 

### Return type

[**List[BranchBase]**](BranchBase.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **branch_update**
> BranchBase branch_update(id, account, service_account_base)

branch_update

branch_update operation for branch

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import stayforge
from stayforge.models.branch_base import BranchBase
from stayforge.models.service_account_base import ServiceAccountBase
from stayforge.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = stayforge.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = stayforge.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with stayforge.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = stayforge.BranchApi(api_client)
    id = 'id_example' # str | 
    account = 'account_example' # str | 
    service_account_base = stayforge.ServiceAccountBase() # ServiceAccountBase | 

    try:
        # branch_update
        api_response = api_instance.branch_update(id, account, service_account_base)
        print("The response of BranchApi->branch_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BranchApi->branch_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **account** | **str**|  | 
 **service_account_base** | [**ServiceAccountBase**](ServiceAccountBase.md)|  | 

### Return type

[**BranchBase**](BranchBase.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

