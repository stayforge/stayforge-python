# openapi_client.OrdersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_order_api_order_post**](OrdersApi.md#create_order_api_order_post) | **POST** /api/order/ | Create Order
[**delete_order_api_order_delete_id_delete**](OrdersApi.md#delete_order_api_order_delete_id_delete) | **DELETE** /api/order/_delete/&lt;id&gt; | Delete Order
[**get_order_by_id_api_order_id_get**](OrdersApi.md#get_order_by_id_api_order_id_get) | **GET** /api/order/&lt;id&gt; | Get Order By Id
[**get_order_by_num_api_order_num_num_get**](OrdersApi.md#get_order_by_num_api_order_num_num_get) | **GET** /api/order/num/&lt;num&gt; | Get Order By Num
[**get_order_types_api_order_order_types_get**](OrdersApi.md#get_order_types_api_order_order_types_get) | **GET** /api/order/order_types | Get Order Types


# **create_order_api_order_post**
> OrderResponses create_order_api_order_post(order_input)

Create Order

If the order number is None when creating, it will be automatically created and then returned.Please record the order number for subsequent operations.

### Example


```python
import openapi_client
from openapi_client.models.order_input import OrderInput
from openapi_client.models.order_responses import OrderResponses
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
    api_instance = openapi_client.OrdersApi(api_client)
    order_input = openapi_client.OrderInput() # OrderInput | 

    try:
        # Create Order
        api_response = api_instance.create_order_api_order_post(order_input)
        print("The response of OrdersApi->create_order_api_order_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->create_order_api_order_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_input** | [**OrderInput**](OrderInput.md)|  | 

### Return type

[**OrderResponses**](OrderResponses.md)

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

# **delete_order_api_order_delete_id_delete**
> OrderResponses delete_order_api_order_delete_id_delete(id)

Delete Order

**WARING:** Order generally does not need to be deleted. You only need to **create a new one to overwrite it**.

### Example


```python
import openapi_client
from openapi_client.models.order_responses import OrderResponses
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
    api_instance = openapi_client.OrdersApi(api_client)
    id = 'id_example' # str | 

    try:
        # Delete Order
        api_response = api_instance.delete_order_api_order_delete_id_delete(id)
        print("The response of OrdersApi->delete_order_api_order_delete_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->delete_order_api_order_delete_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**OrderResponses**](OrderResponses.md)

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

# **get_order_by_id_api_order_id_get**
> OrderResponses get_order_by_id_api_order_id_get(id)

Get Order By Id

### Example


```python
import openapi_client
from openapi_client.models.order_responses import OrderResponses
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
    api_instance = openapi_client.OrdersApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get Order By Id
        api_response = api_instance.get_order_by_id_api_order_id_get(id)
        print("The response of OrdersApi->get_order_by_id_api_order_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->get_order_by_id_api_order_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**OrderResponses**](OrderResponses.md)

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

# **get_order_by_num_api_order_num_num_get**
> OrderResponses get_order_by_num_api_order_num_num_get(num, get_all=get_all)

Get Order By Num

### Example


```python
import openapi_client
from openapi_client.models.order_responses import OrderResponses
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
    api_instance = openapi_client.OrdersApi(api_client)
    num = 'num_example' # str | 
    get_all = False # bool | Get all orders with the same order number. When it's `true`, This time all Orders are returned, otherwise `false` **only the latest Order will be returned**. (optional) (default to False)

    try:
        # Get Order By Num
        api_response = api_instance.get_order_by_num_api_order_num_num_get(num, get_all=get_all)
        print("The response of OrdersApi->get_order_by_num_api_order_num_num_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->get_order_by_num_api_order_num_num_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **num** | **str**|  | 
 **get_all** | **bool**| Get all orders with the same order number. When it&#39;s &#x60;true&#x60;, This time all Orders are returned, otherwise &#x60;false&#x60; **only the latest Order will be returned**. | [optional] [default to False]

### Return type

[**OrderResponses**](OrderResponses.md)

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

# **get_order_types_api_order_order_types_get**
> object get_order_types_api_order_order_types_get()

Get Order Types

Call this API or Click `Try it out` and `Execute` to see the order types you can use.

### Example


```python
import openapi_client
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
    api_instance = openapi_client.OrdersApi(api_client)

    try:
        # Get Order Types
        api_response = api_instance.get_order_types_api_order_order_types_get()
        print("The response of OrdersApi->get_order_types_api_order_order_types_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->get_order_types_api_order_order_types_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

