# openapi_client.RoomTypesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_room_type_api_room_type_post**](RoomTypesApi.md#create_room_type_api_room_type_post) | **POST** /api/room_type/ | Create Room Type
[**delete_room_type_api_room_type_id_delete**](RoomTypesApi.md#delete_room_type_api_room_type_id_delete) | **DELETE** /api/room_type/&lt;id&gt; | Delete Room Type
[**get_room_type_api_room_type_id_get**](RoomTypesApi.md#get_room_type_api_room_type_id_get) | **GET** /api/room_type/&lt;id&gt; | Get Room Type
[**get_room_types_api_room_type_get**](RoomTypesApi.md#get_room_types_api_room_type_get) | **GET** /api/room_type/ | Get Room Types
[**put_room_type_api_room_type_id_put**](RoomTypesApi.md#put_room_type_api_room_type_id_put) | **PUT** /api/room_type/&lt;id&gt; | Put Room Type


# **create_room_type_api_room_type_post**
> RoomTypeResponses create_room_type_api_room_type_post(room_type_input)

Create Room Type

### Example


```python
import openapi_client
from openapi_client.models.room_type_input import RoomTypeInput
from openapi_client.models.room_type_responses import RoomTypeResponses
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
    api_instance = openapi_client.RoomTypesApi(api_client)
    room_type_input = openapi_client.RoomTypeInput() # RoomTypeInput | 

    try:
        # Create Room Type
        api_response = api_instance.create_room_type_api_room_type_post(room_type_input)
        print("The response of RoomTypesApi->create_room_type_api_room_type_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoomTypesApi->create_room_type_api_room_type_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **room_type_input** | [**RoomTypeInput**](RoomTypeInput.md)|  | 

### Return type

[**RoomTypeResponses**](RoomTypeResponses.md)

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

# **delete_room_type_api_room_type_id_delete**
> RoomTypeResponses delete_room_type_api_room_type_id_delete(id)

Delete Room Type

### Example


```python
import openapi_client
from openapi_client.models.room_type_responses import RoomTypeResponses
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
    api_instance = openapi_client.RoomTypesApi(api_client)
    id = 'id_example' # str | 

    try:
        # Delete Room Type
        api_response = api_instance.delete_room_type_api_room_type_id_delete(id)
        print("The response of RoomTypesApi->delete_room_type_api_room_type_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoomTypesApi->delete_room_type_api_room_type_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**RoomTypeResponses**](RoomTypeResponses.md)

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

# **get_room_type_api_room_type_id_get**
> RoomTypeResponses get_room_type_api_room_type_id_get(id)

Get Room Type

### Example


```python
import openapi_client
from openapi_client.models.room_type_responses import RoomTypeResponses
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
    api_instance = openapi_client.RoomTypesApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get Room Type
        api_response = api_instance.get_room_type_api_room_type_id_get(id)
        print("The response of RoomTypesApi->get_room_type_api_room_type_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoomTypesApi->get_room_type_api_room_type_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**RoomTypeResponses**](RoomTypeResponses.md)

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

# **get_room_types_api_room_type_get**
> RoomTypeResponses get_room_types_api_room_type_get(name, price, price_min, description=description, price_policy=price_policy, price_max=price_max)

Get Room Types

### Example


```python
import openapi_client
from openapi_client.models.room_type_responses import RoomTypeResponses
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
    api_instance = openapi_client.RoomTypesApi(api_client)
    name = 'name_example' # str | The Type of RoomTypeType
    price = 56 # int | Current price. If you deploy a price controller, this value will be updated automatically.
    price_min = 56 # int | The min of price.
    description = 'description_example' # str | Description of the room_type type (optional)
    price_policy = 'price_policy_example' # str | The price controller will modify the corresponding price field based on the price policy ID. (optional)
    price_max = 56 # int | The max of price. (optional)

    try:
        # Get Room Types
        api_response = api_instance.get_room_types_api_room_type_get(name, price, price_min, description=description, price_policy=price_policy, price_max=price_max)
        print("The response of RoomTypesApi->get_room_types_api_room_type_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoomTypesApi->get_room_types_api_room_type_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The Type of RoomTypeType | 
 **price** | **int**| Current price. If you deploy a price controller, this value will be updated automatically. | 
 **price_min** | **int**| The min of price. | 
 **description** | **str**| Description of the room_type type | [optional] 
 **price_policy** | **str**| The price controller will modify the corresponding price field based on the price policy ID. | [optional] 
 **price_max** | **int**| The max of price. | [optional] 

### Return type

[**RoomTypeResponses**](RoomTypeResponses.md)

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

# **put_room_type_api_room_type_id_put**
> RoomTypeResponses put_room_type_api_room_type_id_put(id, room_type_input)

Put Room Type

### Example


```python
import openapi_client
from openapi_client.models.room_type_input import RoomTypeInput
from openapi_client.models.room_type_responses import RoomTypeResponses
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
    api_instance = openapi_client.RoomTypesApi(api_client)
    id = 'id_example' # str | 
    room_type_input = openapi_client.RoomTypeInput() # RoomTypeInput | 

    try:
        # Put Room Type
        api_response = api_instance.put_room_type_api_room_type_id_put(id, room_type_input)
        print("The response of RoomTypesApi->put_room_type_api_room_type_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoomTypesApi->put_room_type_api_room_type_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **room_type_input** | [**RoomTypeInput**](RoomTypeInput.md)|  | 

### Return type

[**RoomTypeResponses**](RoomTypeResponses.md)

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

