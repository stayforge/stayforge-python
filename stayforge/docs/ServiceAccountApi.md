# stayforge.ServiceAccountApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**service_account_create**](ServiceAccountApi.md#service_account_create) | **POST** /api/v1/service_account/ | service_account_create
[**service_account_delete**](ServiceAccountApi.md#service_account_delete) | **DELETE** /api/v1/service_account/{id} | service_account_delete
[**service_account_get**](ServiceAccountApi.md#service_account_get) | **GET** /api/v1/service_account/{id} | service_account_get
[**service_account_list**](ServiceAccountApi.md#service_account_list) | **GET** /api/v1/service_account/ | service_account_list
[**service_account_update**](ServiceAccountApi.md#service_account_update) | **PUT** /api/v1/service_account/{id} | service_account_update


# **service_account_create**
> ServiceAccount service_account_create(account, service_account)

service_account_create

service_account_create operation for service_account

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import stayforge
from stayforge.models.service_account import ServiceAccount
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
    api_instance = stayforge.ServiceAccountApi(api_client)
    account = 'account_example' # str | 
    service_account = stayforge.ServiceAccount() # ServiceAccount | 

    try:
        # service_account_create
        api_response = api_instance.service_account_create(account, service_account)
        print("The response of ServiceAccountApi->service_account_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceAccountApi->service_account_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**|  | 
 **service_account** | [**ServiceAccount**](ServiceAccount.md)|  | 

### Return type

[**ServiceAccount**](ServiceAccount.md)

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

# **service_account_delete**
> ServiceAccount service_account_delete(id, account)

service_account_delete

service_account_delete operation for service_account

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import stayforge
from stayforge.models.service_account import ServiceAccount
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
    api_instance = stayforge.ServiceAccountApi(api_client)
    id = 'id_example' # str | 
    account = 'account_example' # str | 

    try:
        # service_account_delete
        api_response = api_instance.service_account_delete(id, account)
        print("The response of ServiceAccountApi->service_account_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceAccountApi->service_account_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **account** | **str**|  | 

### Return type

[**ServiceAccount**](ServiceAccount.md)

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

# **service_account_get**
> List[ServiceAccount] service_account_get(id, account)

service_account_get

service_account_get operation for service_account

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import stayforge
from stayforge.models.service_account import ServiceAccount
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
    api_instance = stayforge.ServiceAccountApi(api_client)
    id = 'id_example' # str | 
    account = 'account_example' # str | 

    try:
        # service_account_get
        api_response = api_instance.service_account_get(id, account)
        print("The response of ServiceAccountApi->service_account_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceAccountApi->service_account_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **account** | **str**|  | 

### Return type

[**List[ServiceAccount]**](ServiceAccount.md)

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

# **service_account_list**
> List[ServiceAccount] service_account_list(account)

service_account_list

service_account_list operation for service_account

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import stayforge
from stayforge.models.service_account import ServiceAccount
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
    api_instance = stayforge.ServiceAccountApi(api_client)
    account = 'account_example' # str | 

    try:
        # service_account_list
        api_response = api_instance.service_account_list(account)
        print("The response of ServiceAccountApi->service_account_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceAccountApi->service_account_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**|  | 

### Return type

[**List[ServiceAccount]**](ServiceAccount.md)

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

# **service_account_update**
> ServiceAccount service_account_update(id, account, service_account)

service_account_update

service_account_update operation for service_account

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import stayforge
from stayforge.models.service_account import ServiceAccount
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
    api_instance = stayforge.ServiceAccountApi(api_client)
    id = 'id_example' # str | 
    account = 'account_example' # str | 
    service_account = stayforge.ServiceAccount() # ServiceAccount | 

    try:
        # service_account_update
        api_response = api_instance.service_account_update(id, account, service_account)
        print("The response of ServiceAccountApi->service_account_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceAccountApi->service_account_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **account** | **str**|  | 
 **service_account** | [**ServiceAccount**](ServiceAccount.md)|  | 

### Return type

[**ServiceAccount**](ServiceAccount.md)

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

