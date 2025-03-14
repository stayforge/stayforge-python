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
> RoomTypeBase room_type_create(branch_base)

room_type_create

room_type_create operation for room_type

### Example


```python
import stayforge
from stayforge.models.branch_base import BranchBase
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
    api_instance = stayforge.RoomTypeApi(api_client)
    branch_base = stayforge.BranchBase() # BranchBase | 

    try:
        # room_type_create
        api_response = api_instance.room_type_create(branch_base)
        print("The response of RoomTypeApi->room_type_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoomTypeApi->room_type_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **branch_base** | [**BranchBase**](BranchBase.md)|  | 

### Return type

[**RoomTypeBase**](RoomTypeBase.md)

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

# **room_type_delete**
> RoomTypeBase room_type_delete(id)

room_type_delete

room_type_delete operation for room_type

### Example


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


# Enter a context with an instance of the API client
with stayforge.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = stayforge.RoomTypeApi(api_client)
    id = 'id_example' # str | 

    try:
        # room_type_delete
        api_response = api_instance.room_type_delete(id)
        print("The response of RoomTypeApi->room_type_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoomTypeApi->room_type_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**RoomTypeBase**](RoomTypeBase.md)

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

# **room_type_get**
> List[RoomTypeBase] room_type_get(id)

room_type_get

room_type_get operation for room_type

### Example


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


# Enter a context with an instance of the API client
with stayforge.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = stayforge.RoomTypeApi(api_client)
    id = 'id_example' # str | 

    try:
        # room_type_get
        api_response = api_instance.room_type_get(id)
        print("The response of RoomTypeApi->room_type_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoomTypeApi->room_type_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**List[RoomTypeBase]**](RoomTypeBase.md)

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

# **room_type_list**
> List[RoomTypeBase] room_type_list()

room_type_list

room_type_list operation for room_type

### Example


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


# Enter a context with an instance of the API client
with stayforge.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = stayforge.RoomTypeApi(api_client)

    try:
        # room_type_list
        api_response = api_instance.room_type_list()
        print("The response of RoomTypeApi->room_type_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoomTypeApi->room_type_list: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[RoomTypeBase]**](RoomTypeBase.md)

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

# **room_type_update**
> RoomTypeBase room_type_update(id, branch_base)

room_type_update

room_type_update operation for room_type

### Example


```python
import stayforge
from stayforge.models.branch_base import BranchBase
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
    api_instance = stayforge.RoomTypeApi(api_client)
    id = 'id_example' # str | 
    branch_base = stayforge.BranchBase() # BranchBase | 

    try:
        # room_type_update
        api_response = api_instance.room_type_update(id, branch_base)
        print("The response of RoomTypeApi->room_type_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoomTypeApi->room_type_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **branch_base** | [**BranchBase**](BranchBase.md)|  | 

### Return type

[**RoomTypeBase**](RoomTypeBase.md)

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

