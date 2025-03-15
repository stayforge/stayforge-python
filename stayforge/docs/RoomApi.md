# stayforge.RoomApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**room_create**](RoomApi.md#room_create) | **POST** /api/v1/room/ | room_create
[**room_delete**](RoomApi.md#room_delete) | **DELETE** /api/v1/room/{id} | room_delete
[**room_get**](RoomApi.md#room_get) | **GET** /api/v1/room/{id} | room_get
[**room_list**](RoomApi.md#room_list) | **GET** /api/v1/room/ | room_list
[**room_update**](RoomApi.md#room_update) | **PUT** /api/v1/room/{id} | room_update


# **room_create**
> RoomBase room_create(room_type_base_input)

room_create

room_create operation for room

### Example


```python
import stayforge
from stayforge.models.room_base import RoomBase
from stayforge.models.room_type_base_input import RoomTypeBaseInput
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
    api_instance = stayforge.RoomApi(api_client)
    room_type_base_input = stayforge.RoomTypeBaseInput() # RoomTypeBaseInput | 

    try:
        # room_create
        api_response = api_instance.room_create(room_type_base_input)
        print("The response of RoomApi->room_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoomApi->room_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **room_type_base_input** | [**RoomTypeBaseInput**](RoomTypeBaseInput.md)|  | 

### Return type

[**RoomBase**](RoomBase.md)

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

# **room_delete**
> RoomBase room_delete(id)

room_delete

room_delete operation for room

### Example


```python
import stayforge
from stayforge.models.room_base import RoomBase
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
    api_instance = stayforge.RoomApi(api_client)
    id = 'id_example' # str | 

    try:
        # room_delete
        api_response = api_instance.room_delete(id)
        print("The response of RoomApi->room_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoomApi->room_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**RoomBase**](RoomBase.md)

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

# **room_get**
> List[RoomBase] room_get(id)

room_get

room_get operation for room

### Example


```python
import stayforge
from stayforge.models.room_base import RoomBase
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
    api_instance = stayforge.RoomApi(api_client)
    id = 'id_example' # str | 

    try:
        # room_get
        api_response = api_instance.room_get(id)
        print("The response of RoomApi->room_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoomApi->room_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**List[RoomBase]**](RoomBase.md)

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

# **room_list**
> List[RoomBase] room_list()

room_list

room_list operation for room

### Example


```python
import stayforge
from stayforge.models.room_base import RoomBase
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
    api_instance = stayforge.RoomApi(api_client)

    try:
        # room_list
        api_response = api_instance.room_list()
        print("The response of RoomApi->room_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoomApi->room_list: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[RoomBase]**](RoomBase.md)

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

# **room_update**
> RoomBase room_update(id, room_type_base_input)

room_update

room_update operation for room

### Example


```python
import stayforge
from stayforge.models.room_base import RoomBase
from stayforge.models.room_type_base_input import RoomTypeBaseInput
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
    api_instance = stayforge.RoomApi(api_client)
    id = 'id_example' # str | 
    room_type_base_input = stayforge.RoomTypeBaseInput() # RoomTypeBaseInput | 

    try:
        # room_update
        api_response = api_instance.room_update(id, room_type_base_input)
        print("The response of RoomApi->room_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoomApi->room_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **room_type_base_input** | [**RoomTypeBaseInput**](RoomTypeBaseInput.md)|  | 

### Return type

[**RoomBase**](RoomBase.md)

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

