# stayforge.RoomTypeApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**room_type_create**](RoomTypeApi.md#room_type_create) | **POST** /api/v1/room_type/ | room_type_create
[**room_type_delete**](RoomTypeApi.md#room_type_delete) | **DELETE** /api/v1/room_type/{id} | room_type_delete
[**room_type_get**](RoomTypeApi.md#room_type_get) | **GET** /api/v1/room_type/{id} | room_type_get
[**room_type_list**](RoomTypeApi.md#room_type_list) | **GET** /api/v1/room_type/ | room_type_list
[**room_type_update**](RoomTypeApi.md#room_type_update) | **PUT** /api/v1/room_type/{id} | room_type_update


# **room_type_create**
> RoomTypeBase room_type_create(account, service_account_base)

room_type_create

room_type_create operation for room_type

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import stayforge
from stayforge.models.room_type_base import RoomTypeBase
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
    api_instance = stayforge.RoomTypeApi(api_client)
    account = 'account_example' # str | 
    service_account_base = stayforge.ServiceAccountBase() # ServiceAccountBase | 

    try:
        # room_type_create
        api_response = api_instance.room_type_create(account, service_account_base)
        print("The response of RoomTypeApi->room_type_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoomTypeApi->room_type_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**|  | 
 **service_account_base** | [**ServiceAccountBase**](ServiceAccountBase.md)|  | 

### Return type

[**RoomTypeBase**](RoomTypeBase.md)

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

# **room_type_delete**
> RoomTypeBase room_type_delete(id, account)

room_type_delete

room_type_delete operation for room_type

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import stayforge
from stayforge.models.room_type_base import RoomTypeBase
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
    api_instance = stayforge.RoomTypeApi(api_client)
    id = 'id_example' # str | 
    account = 'account_example' # str | 

    try:
        # room_type_delete
        api_response = api_instance.room_type_delete(id, account)
        print("The response of RoomTypeApi->room_type_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoomTypeApi->room_type_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **account** | **str**|  | 

### Return type

[**RoomTypeBase**](RoomTypeBase.md)

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

# **room_type_get**
> List[RoomTypeBase] room_type_get(id, account)

room_type_get

room_type_get operation for room_type

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import stayforge
from stayforge.models.room_type_base import RoomTypeBase
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
    api_instance = stayforge.RoomTypeApi(api_client)
    id = 'id_example' # str | 
    account = 'account_example' # str | 

    try:
        # room_type_get
        api_response = api_instance.room_type_get(id, account)
        print("The response of RoomTypeApi->room_type_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoomTypeApi->room_type_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **account** | **str**|  | 

### Return type

[**List[RoomTypeBase]**](RoomTypeBase.md)

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

# **room_type_list**
> List[RoomTypeBase] room_type_list(account)

room_type_list

room_type_list operation for room_type

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import stayforge
from stayforge.models.room_type_base import RoomTypeBase
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
    api_instance = stayforge.RoomTypeApi(api_client)
    account = 'account_example' # str | 

    try:
        # room_type_list
        api_response = api_instance.room_type_list(account)
        print("The response of RoomTypeApi->room_type_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoomTypeApi->room_type_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**|  | 

### Return type

[**List[RoomTypeBase]**](RoomTypeBase.md)

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

# **room_type_update**
> RoomTypeBase room_type_update(id, account, service_account_base)

room_type_update

room_type_update operation for room_type

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import stayforge
from stayforge.models.room_type_base import RoomTypeBase
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
    api_instance = stayforge.RoomTypeApi(api_client)
    id = 'id_example' # str | 
    account = 'account_example' # str | 
    service_account_base = stayforge.ServiceAccountBase() # ServiceAccountBase | 

    try:
        # room_type_update
        api_response = api_instance.room_type_update(id, account, service_account_base)
        print("The response of RoomTypeApi->room_type_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoomTypeApi->room_type_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **account** | **str**|  | 
 **service_account_base** | [**ServiceAccountBase**](ServiceAccountBase.md)|  | 

### Return type

[**RoomTypeBase**](RoomTypeBase.md)

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

