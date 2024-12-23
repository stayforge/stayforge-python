# stayforge.WebhooksManagerApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_webhooks_profile_api_webhooks_manager_post**](WebhooksManagerApi.md#create_webhooks_profile_api_webhooks_manager_post) | **POST** /api/webhooks_manager/ | Create Webhooks Profile
[**delete_webhooks_profile_api_webhooks_manager_id_delete**](WebhooksManagerApi.md#delete_webhooks_profile_api_webhooks_manager_id_delete) | **DELETE** /api/webhooks_manager/{id} | Delete Webhooks Profile
[**get_webhooks_profile_api_webhooks_manager_get**](WebhooksManagerApi.md#get_webhooks_profile_api_webhooks_manager_get) | **GET** /api/webhooks_manager/ | Get Webhooks Profile
[**get_webhooks_profile_api_webhooks_manager_id_get**](WebhooksManagerApi.md#get_webhooks_profile_api_webhooks_manager_id_get) | **GET** /api/webhooks_manager/{id} | Get Webhooks Profile
[**put_webhooks_profile_api_webhooks_manager_id_put**](WebhooksManagerApi.md#put_webhooks_profile_api_webhooks_manager_id_put) | **PUT** /api/webhooks_manager/{id} | Put Webhooks Profile


# **create_webhooks_profile_api_webhooks_manager_post**
> WebhooksManagerResponses create_webhooks_profile_api_webhooks_manager_post(webhooks_manager_input)

Create Webhooks Profile

### Example


```python
import stayforge
from stayforge.models.webhooks_manager_input import WebhooksManagerInput
from stayforge.models.webhooks_manager_responses import WebhooksManagerResponses
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
    api_instance = stayforge.WebhooksManagerApi(api_client)
    webhooks_manager_input = stayforge.WebhooksManagerInput() # WebhooksManagerInput | 

    try:
        # Create Webhooks Profile
        api_response = api_instance.create_webhooks_profile_api_webhooks_manager_post(webhooks_manager_input)
        print("The response of WebhooksManagerApi->create_webhooks_profile_api_webhooks_manager_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksManagerApi->create_webhooks_profile_api_webhooks_manager_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhooks_manager_input** | [**WebhooksManagerInput**](WebhooksManagerInput.md)|  | 

### Return type

[**WebhooksManagerResponses**](WebhooksManagerResponses.md)

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

# **delete_webhooks_profile_api_webhooks_manager_id_delete**
> WebhooksManagerResponses delete_webhooks_profile_api_webhooks_manager_id_delete(id)

Delete Webhooks Profile

### Example


```python
import stayforge
from stayforge.models.webhooks_manager_responses import WebhooksManagerResponses
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
    api_instance = stayforge.WebhooksManagerApi(api_client)
    id = 'id_example' # str | 

    try:
        # Delete Webhooks Profile
        api_response = api_instance.delete_webhooks_profile_api_webhooks_manager_id_delete(id)
        print("The response of WebhooksManagerApi->delete_webhooks_profile_api_webhooks_manager_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksManagerApi->delete_webhooks_profile_api_webhooks_manager_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**WebhooksManagerResponses**](WebhooksManagerResponses.md)

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

# **get_webhooks_profile_api_webhooks_manager_get**
> WebhooksManagerResponses get_webhooks_profile_api_webhooks_manager_get(webhook_name=webhook_name, endpoint=endpoint, catch_path=catch_path, catch_method=catch_method, catch_status=catch_status)

Get Webhooks Profile

### Example


```python
import stayforge
from stayforge.models.webhooks_manager_responses import WebhooksManagerResponses
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
    api_instance = stayforge.WebhooksManagerApi(api_client)
    webhook_name = 'webhook_name_example' # str | A friendly name you can remember. (optional)
    endpoint = 'endpoint_example' # str | The URL endpoint where the webhook is to be sent, e.g., `https://youapplocation/webhook/endpoint`. (optional)
    catch_path = 'catch_path_example' # str | This refers to the API within Stayforage, the path part of its URL e.g., `/api/order/`. (optional)
    catch_method = 'catch_method_example' # str | Only configured HTTP methods (e.g., `POST`) that the request will capture. (optional)
    catch_status = 56 # int | Only configured HTTP status code (e.g., `200`) that the request will capture. (optional)

    try:
        # Get Webhooks Profile
        api_response = api_instance.get_webhooks_profile_api_webhooks_manager_get(webhook_name=webhook_name, endpoint=endpoint, catch_path=catch_path, catch_method=catch_method, catch_status=catch_status)
        print("The response of WebhooksManagerApi->get_webhooks_profile_api_webhooks_manager_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksManagerApi->get_webhooks_profile_api_webhooks_manager_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_name** | **str**| A friendly name you can remember. | [optional] 
 **endpoint** | **str**| The URL endpoint where the webhook is to be sent, e.g., &#x60;https://youapplocation/webhook/endpoint&#x60;. | [optional] 
 **catch_path** | **str**| This refers to the API within Stayforage, the path part of its URL e.g., &#x60;/api/order/&#x60;. | [optional] 
 **catch_method** | **str**| Only configured HTTP methods (e.g., &#x60;POST&#x60;) that the request will capture. | [optional] 
 **catch_status** | **int**| Only configured HTTP status code (e.g., &#x60;200&#x60;) that the request will capture. | [optional] 

### Return type

[**WebhooksManagerResponses**](WebhooksManagerResponses.md)

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

# **get_webhooks_profile_api_webhooks_manager_id_get**
> WebhooksManagerResponses get_webhooks_profile_api_webhooks_manager_id_get(id)

Get Webhooks Profile

### Example


```python
import stayforge
from stayforge.models.webhooks_manager_responses import WebhooksManagerResponses
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
    api_instance = stayforge.WebhooksManagerApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get Webhooks Profile
        api_response = api_instance.get_webhooks_profile_api_webhooks_manager_id_get(id)
        print("The response of WebhooksManagerApi->get_webhooks_profile_api_webhooks_manager_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksManagerApi->get_webhooks_profile_api_webhooks_manager_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**WebhooksManagerResponses**](WebhooksManagerResponses.md)

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

# **put_webhooks_profile_api_webhooks_manager_id_put**
> WebhooksManagerResponses put_webhooks_profile_api_webhooks_manager_id_put(id, webhooks_manager_input)

Put Webhooks Profile

### Example


```python
import stayforge
from stayforge.models.webhooks_manager_input import WebhooksManagerInput
from stayforge.models.webhooks_manager_responses import WebhooksManagerResponses
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
    api_instance = stayforge.WebhooksManagerApi(api_client)
    id = 'id_example' # str | 
    webhooks_manager_input = stayforge.WebhooksManagerInput() # WebhooksManagerInput | 

    try:
        # Put Webhooks Profile
        api_response = api_instance.put_webhooks_profile_api_webhooks_manager_id_put(id, webhooks_manager_input)
        print("The response of WebhooksManagerApi->put_webhooks_profile_api_webhooks_manager_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksManagerApi->put_webhooks_profile_api_webhooks_manager_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **webhooks_manager_input** | [**WebhooksManagerInput**](WebhooksManagerInput.md)|  | 

### Return type

[**WebhooksManagerResponses**](WebhooksManagerResponses.md)

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

