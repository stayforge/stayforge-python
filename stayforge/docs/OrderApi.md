# stayforge.OrderApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**order_create**](OrderApi.md#order_create) | **POST** /api/v1/order/ | order_create
[**order_delete**](OrderApi.md#order_delete) | **DELETE** /api/v1/order/{id} | order_delete
[**order_get**](OrderApi.md#order_get) | **GET** /api/v1/order/{id} | order_get
[**order_list**](OrderApi.md#order_list) | **GET** /api/v1/order/ | order_list
[**order_update**](OrderApi.md#order_update) | **PUT** /api/v1/order/{id} | order_update


# **order_create**
> object order_create(account, service_account_base)

order_create

order_create operation for order

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import stayforge
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
    api_instance = stayforge.OrderApi(api_client)
    account = 'account_example' # str | 
    service_account_base = stayforge.ServiceAccountBase() # ServiceAccountBase | 

    try:
        # order_create
        api_response = api_instance.order_create(account, service_account_base)
        print("The response of OrderApi->order_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderApi->order_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**|  | 
 **service_account_base** | [**ServiceAccountBase**](ServiceAccountBase.md)|  | 

### Return type

**object**

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

# **order_delete**
> object order_delete(id, account)

order_delete

order_delete operation for order

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import stayforge
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
    api_instance = stayforge.OrderApi(api_client)
    id = 'id_example' # str | 
    account = 'account_example' # str | 

    try:
        # order_delete
        api_response = api_instance.order_delete(id, account)
        print("The response of OrderApi->order_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderApi->order_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **account** | **str**|  | 

### Return type

**object**

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

# **order_get**
> List[Optional[object]] order_get(id, account)

order_get

order_get operation for order

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import stayforge
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
    api_instance = stayforge.OrderApi(api_client)
    id = 'id_example' # str | 
    account = 'account_example' # str | 

    try:
        # order_get
        api_response = api_instance.order_get(id, account)
        print("The response of OrderApi->order_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderApi->order_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **account** | **str**|  | 

### Return type

**List[Optional[object]]**

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

# **order_list**
> List[Optional[object]] order_list(account)

order_list

order_list operation for order

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import stayforge
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
    api_instance = stayforge.OrderApi(api_client)
    account = 'account_example' # str | 

    try:
        # order_list
        api_response = api_instance.order_list(account)
        print("The response of OrderApi->order_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderApi->order_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**|  | 

### Return type

**List[Optional[object]]**

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

# **order_update**
> object order_update(id, account, service_account_base)

order_update

order_update operation for order

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import stayforge
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
    api_instance = stayforge.OrderApi(api_client)
    id = 'id_example' # str | 
    account = 'account_example' # str | 
    service_account_base = stayforge.ServiceAccountBase() # ServiceAccountBase | 

    try:
        # order_update
        api_response = api_instance.order_update(id, account, service_account_base)
        print("The response of OrderApi->order_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderApi->order_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **account** | **str**|  | 
 **service_account_base** | [**ServiceAccountBase**](ServiceAccountBase.md)|  | 

### Return type

**object**

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

