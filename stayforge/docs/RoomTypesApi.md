# stayforge.RoomTypesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_room_type_api_room_type_rooms_post**](RoomTypesApi.md#create_room_type_api_room_type_rooms_post) | **POST** /api/room_type/rooms/ | Create Room Type
[**delete_room_type_api_room_type_room_types_room_type_id_delete**](RoomTypesApi.md#delete_room_type_api_room_type_room_types_room_type_id_delete) | **DELETE** /api/room_type/room_types/{room_type_id} | Delete Room Type
[**get_room_type_api_room_type_room_types_room_type_id_get**](RoomTypesApi.md#get_room_type_api_room_type_room_types_room_type_id_get) | **GET** /api/room_type/room_types/{room_type_id} | Get Room Type
[**get_room_types_api_room_type_rooms_get**](RoomTypesApi.md#get_room_types_api_room_type_rooms_get) | **GET** /api/room_type/rooms/ | Get Room Types
[**update_room_type_api_room_type_room_types_room_type_id_put**](RoomTypesApi.md#update_room_type_api_room_type_room_types_room_type_id_put) | **PUT** /api/room_type/room_types/{room_type_id} | Update Room Type


# **create_room_type_api_room_type_rooms_post**
> RoomType create_room_type_api_room_type_rooms_post(room_type_base)

Create Room Type

### Example


```python
import stayforge
from stayforge.models.room_type import RoomType
from stayforge.models.room_type_base import RoomTypeBase
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
    api_instance = stayforge.RoomTypesApi(api_client)
    room_type_base = stayforge.RoomTypeBase() # RoomTypeBase | 

    try:
        # Create Room Type
        api_response = api_instance.create_room_type_api_room_type_rooms_post(room_type_base)
        print("The response of RoomTypesApi->create_room_type_api_room_type_rooms_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoomTypesApi->create_room_type_api_room_type_rooms_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **room_type_base** | [**RoomTypeBase**](RoomTypeBase.md)|  | 

### Return type

[**RoomType**](RoomType.md)

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

# **delete_room_type_api_room_type_room_types_room_type_id_delete**
> object delete_room_type_api_room_type_room_types_room_type_id_delete(room_type_id)

Delete Room Type

### Example


```python
import stayforge
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
    api_instance = stayforge.RoomTypesApi(api_client)
    room_type_id = 'room_type_id_example' # str | 

    try:
        # Delete Room Type
        api_response = api_instance.delete_room_type_api_room_type_room_types_room_type_id_delete(room_type_id)
        print("The response of RoomTypesApi->delete_room_type_api_room_type_room_types_room_type_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoomTypesApi->delete_room_type_api_room_type_room_types_room_type_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **room_type_id** | **str**|  | 

### Return type

**object**

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

# **get_room_type_api_room_type_room_types_room_type_id_get**
> RoomType get_room_type_api_room_type_room_types_room_type_id_get(room_type_id)

Get Room Type

### Example


```python
import stayforge
from stayforge.models.room_type import RoomType
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
    api_instance = stayforge.RoomTypesApi(api_client)
    room_type_id = 'room_type_id_example' # str | 

    try:
        # Get Room Type
        api_response = api_instance.get_room_type_api_room_type_room_types_room_type_id_get(room_type_id)
        print("The response of RoomTypesApi->get_room_type_api_room_type_room_types_room_type_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoomTypesApi->get_room_type_api_room_type_room_types_room_type_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **room_type_id** | **str**|  | 

### Return type

[**RoomType**](RoomType.md)

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

# **get_room_types_api_room_type_rooms_get**
> List[RoomType] get_room_types_api_room_type_rooms_get()

Get Room Types

### Example


```python
import stayforge
from stayforge.models.room_type import RoomType
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
    api_instance = stayforge.RoomTypesApi(api_client)

    try:
        # Get Room Types
        api_response = api_instance.get_room_types_api_room_type_rooms_get()
        print("The response of RoomTypesApi->get_room_types_api_room_type_rooms_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoomTypesApi->get_room_types_api_room_type_rooms_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[RoomType]**](RoomType.md)

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

# **update_room_type_api_room_type_room_types_room_type_id_put**
> RoomType update_room_type_api_room_type_room_types_room_type_id_put(room_type_id, room_type_base)

Update Room Type

### Example


```python
import stayforge
from stayforge.models.room_type import RoomType
from stayforge.models.room_type_base import RoomTypeBase
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
    api_instance = stayforge.RoomTypesApi(api_client)
    room_type_id = 'room_type_id_example' # str | 
    room_type_base = stayforge.RoomTypeBase() # RoomTypeBase | 

    try:
        # Update Room Type
        api_response = api_instance.update_room_type_api_room_type_room_types_room_type_id_put(room_type_id, room_type_base)
        print("The response of RoomTypesApi->update_room_type_api_room_type_room_types_room_type_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoomTypesApi->update_room_type_api_room_type_room_types_room_type_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **room_type_id** | **str**|  | 
 **room_type_base** | [**RoomTypeBase**](RoomTypeBase.md)|  | 

### Return type

[**RoomType**](RoomType.md)

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

