# stayforge.RoomsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_room_api_room_post**](RoomsApi.md#create_room_api_room_post) | **POST** /api/room/ | Create Room
[**delete_room_api_room_id_delete**](RoomsApi.md#delete_room_api_room_id_delete) | **DELETE** /api/room/&lt;id&gt; | Delete Room
[**get_room_api_room_id_get**](RoomsApi.md#get_room_api_room_id_get) | **GET** /api/room/&lt;id&gt; | Get Room
[**get_rooms_api_room_get**](RoomsApi.md#get_rooms_api_room_get) | **GET** /api/room/ | Get Rooms
[**put_room_api_room_id_put**](RoomsApi.md#put_room_api_room_id_put) | **PUT** /api/room/&lt;id&gt; | Put Room


# **create_room_api_room_post**
> RoomResponses create_room_api_room_post(room_input)

Create Room

### Example


```python
import stayforge
from stayforge.models.room_input import RoomInput
from stayforge.models.room_responses import RoomResponses
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
    api_instance = stayforge.RoomsApi(api_client)
    room_input = stayforge.RoomInput() # RoomInput | 

    try:
        # Create Room
        api_response = api_instance.create_room_api_room_post(room_input)
        print("The response of RoomsApi->create_room_api_room_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoomsApi->create_room_api_room_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **room_input** | [**RoomInput**](RoomInput.md)|  | 

### Return type

[**RoomResponses**](RoomResponses.md)

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

# **delete_room_api_room_id_delete**
> RoomResponses delete_room_api_room_id_delete(id)

Delete Room

### Example


```python
import stayforge
from stayforge.models.room_responses import RoomResponses
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
    api_instance = stayforge.RoomsApi(api_client)
    id = 'id_example' # str | 

    try:
        # Delete Room
        api_response = api_instance.delete_room_api_room_id_delete(id)
        print("The response of RoomsApi->delete_room_api_room_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoomsApi->delete_room_api_room_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**RoomResponses**](RoomResponses.md)

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

# **get_room_api_room_id_get**
> RoomResponses get_room_api_room_id_get(id)

Get Room

### Example


```python
import stayforge
from stayforge.models.room_responses import RoomResponses
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
    api_instance = stayforge.RoomsApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get Room
        api_response = api_instance.get_room_api_room_id_get(id)
        print("The response of RoomsApi->get_room_api_room_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoomsApi->get_room_api_room_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**RoomResponses**](RoomResponses.md)

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

# **get_rooms_api_room_get**
> RoomResponses get_rooms_api_room_get(name=name, address=address, telephone=telephone)

Get Rooms

### Example


```python
import stayforge
from stayforge.models.room_responses import RoomResponses
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
    api_instance = stayforge.RoomsApi(api_client)
    name = 'name_example' # str |  (optional)
    address = 'address_example' # str |  (optional)
    telephone = 'telephone_example' # str |  (optional)

    try:
        # Get Rooms
        api_response = api_instance.get_rooms_api_room_get(name=name, address=address, telephone=telephone)
        print("The response of RoomsApi->get_rooms_api_room_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoomsApi->get_rooms_api_room_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 
 **address** | **str**|  | [optional] 
 **telephone** | **str**|  | [optional] 

### Return type

[**RoomResponses**](RoomResponses.md)

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

# **put_room_api_room_id_put**
> RoomResponses put_room_api_room_id_put(id, room_input)

Put Room

### Example


```python
import stayforge
from stayforge.models.room_input import RoomInput
from stayforge.models.room_responses import RoomResponses
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
    api_instance = stayforge.RoomsApi(api_client)
    id = 'id_example' # str | 
    room_input = stayforge.RoomInput() # RoomInput | 

    try:
        # Put Room
        api_response = api_instance.put_room_api_room_id_put(id, room_input)
        print("The response of RoomsApi->put_room_api_room_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoomsApi->put_room_api_room_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **room_input** | [**RoomInput**](RoomInput.md)|  | 

### Return type

[**RoomResponses**](RoomResponses.md)

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

