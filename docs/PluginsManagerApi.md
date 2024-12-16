# stayforge.PluginsManagerApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_plugins_profile_api_plugins_manager_post**](PluginsManagerApi.md#create_plugins_profile_api_plugins_manager_post) | **POST** /api/plugins_manager/ | Create Plugins Profile
[**delete_plugins_profile_api_plugins_manager_id_delete**](PluginsManagerApi.md#delete_plugins_profile_api_plugins_manager_id_delete) | **DELETE** /api/plugins_manager/&lt;id&gt; | Delete Plugins Profile
[**get_plugins_profile_api_plugins_manager_get**](PluginsManagerApi.md#get_plugins_profile_api_plugins_manager_get) | **GET** /api/plugins_manager/ | Get Plugins Profile
[**get_plugins_profile_api_plugins_manager_id_get**](PluginsManagerApi.md#get_plugins_profile_api_plugins_manager_id_get) | **GET** /api/plugins_manager/&lt;id&gt; | Get Plugins Profile
[**put_plugins_profile_api_plugins_manager_id_put**](PluginsManagerApi.md#put_plugins_profile_api_plugins_manager_id_put) | **PUT** /api/plugins_manager/&lt;id&gt; | Put Plugins Profile


# **create_plugins_profile_api_plugins_manager_post**
> PluginsManagerResponses create_plugins_profile_api_plugins_manager_post(plugins_manager_input)

Create Plugins Profile

### Example


```python
import stayforge
from stayforge.models.plugins_manager_input import PluginsManagerInput
from stayforge.models.plugins_manager_responses import PluginsManagerResponses
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
    api_instance = stayforge.PluginsManagerApi(api_client)
    plugins_manager_input = stayforge.PluginsManagerInput() # PluginsManagerInput | 

    try:
        # Create Plugins Profile
        api_response = api_instance.create_plugins_profile_api_plugins_manager_post(plugins_manager_input)
        print("The response of PluginsManagerApi->create_plugins_profile_api_plugins_manager_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PluginsManagerApi->create_plugins_profile_api_plugins_manager_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plugins_manager_input** | [**PluginsManagerInput**](PluginsManagerInput.md)|  | 

### Return type

[**PluginsManagerResponses**](PluginsManagerResponses.md)

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

# **delete_plugins_profile_api_plugins_manager_id_delete**
> PluginsManagerResponses delete_plugins_profile_api_plugins_manager_id_delete(id)

Delete Plugins Profile

### Example


```python
import stayforge
from stayforge.models.plugins_manager_responses import PluginsManagerResponses
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
    api_instance = stayforge.PluginsManagerApi(api_client)
    id = 'id_example' # str | 

    try:
        # Delete Plugins Profile
        api_response = api_instance.delete_plugins_profile_api_plugins_manager_id_delete(id)
        print("The response of PluginsManagerApi->delete_plugins_profile_api_plugins_manager_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PluginsManagerApi->delete_plugins_profile_api_plugins_manager_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**PluginsManagerResponses**](PluginsManagerResponses.md)

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

# **get_plugins_profile_api_plugins_manager_get**
> PluginsManagerResponses get_plugins_profile_api_plugins_manager_get(plugin_name=plugin_name, endpoint=endpoint, catch_path=catch_path, catch_method=catch_method, catch_status=catch_status)

Get Plugins Profile

### Example


```python
import stayforge
from stayforge.models.plugins_manager_responses import PluginsManagerResponses
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
    api_instance = stayforge.PluginsManagerApi(api_client)
    plugin_name = 'plugin_name_example' # str | A friendly name you can remember. (optional)
    endpoint = 'endpoint_example' # str | The URL endpoint where the plugin is to be sent, e.g., `https://youapplocation/plugin/endpoint`. (optional)
    catch_path = 'catch_path_example' # str | This refers to the API within Stayforage, the path part of its URL e.g., `/api/order/`. (optional)
    catch_method = 'catch_method_example' # str | Only configured HTTP methods (e.g., `POST`) that the request will capture. (optional)
    catch_status = 56 # int | Only configured HTTP status code (e.g., `200`) that the request will capture. (optional)

    try:
        # Get Plugins Profile
        api_response = api_instance.get_plugins_profile_api_plugins_manager_get(plugin_name=plugin_name, endpoint=endpoint, catch_path=catch_path, catch_method=catch_method, catch_status=catch_status)
        print("The response of PluginsManagerApi->get_plugins_profile_api_plugins_manager_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PluginsManagerApi->get_plugins_profile_api_plugins_manager_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plugin_name** | **str**| A friendly name you can remember. | [optional] 
 **endpoint** | **str**| The URL endpoint where the plugin is to be sent, e.g., &#x60;https://youapplocation/plugin/endpoint&#x60;. | [optional] 
 **catch_path** | **str**| This refers to the API within Stayforage, the path part of its URL e.g., &#x60;/api/order/&#x60;. | [optional] 
 **catch_method** | **str**| Only configured HTTP methods (e.g., &#x60;POST&#x60;) that the request will capture. | [optional] 
 **catch_status** | **int**| Only configured HTTP status code (e.g., &#x60;200&#x60;) that the request will capture. | [optional] 

### Return type

[**PluginsManagerResponses**](PluginsManagerResponses.md)

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

# **get_plugins_profile_api_plugins_manager_id_get**
> PluginsManagerResponses get_plugins_profile_api_plugins_manager_id_get(id)

Get Plugins Profile

### Example


```python
import stayforge
from stayforge.models.plugins_manager_responses import PluginsManagerResponses
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
    api_instance = stayforge.PluginsManagerApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get Plugins Profile
        api_response = api_instance.get_plugins_profile_api_plugins_manager_id_get(id)
        print("The response of PluginsManagerApi->get_plugins_profile_api_plugins_manager_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PluginsManagerApi->get_plugins_profile_api_plugins_manager_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**PluginsManagerResponses**](PluginsManagerResponses.md)

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

# **put_plugins_profile_api_plugins_manager_id_put**
> PluginsManagerResponses put_plugins_profile_api_plugins_manager_id_put(id, plugins_manager_input)

Put Plugins Profile

### Example


```python
import stayforge
from stayforge.models.plugins_manager_input import PluginsManagerInput
from stayforge.models.plugins_manager_responses import PluginsManagerResponses
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
    api_instance = stayforge.PluginsManagerApi(api_client)
    id = 'id_example' # str | 
    plugins_manager_input = stayforge.PluginsManagerInput() # PluginsManagerInput | 

    try:
        # Put Plugins Profile
        api_response = api_instance.put_plugins_profile_api_plugins_manager_id_put(id, plugins_manager_input)
        print("The response of PluginsManagerApi->put_plugins_profile_api_plugins_manager_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PluginsManagerApi->put_plugins_profile_api_plugins_manager_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **plugins_manager_input** | [**PluginsManagerInput**](PluginsManagerInput.md)|  | 

### Return type

[**PluginsManagerResponses**](PluginsManagerResponses.md)

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

