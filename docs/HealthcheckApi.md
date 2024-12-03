# openapi_client.HealthcheckApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**info_api_healthcheck_info_get**](HealthcheckApi.md#info_api_healthcheck_info_get) | **GET** /api/healthcheck/info | Info
[**ping_api_healthcheck_get**](HealthcheckApi.md#ping_api_healthcheck_get) | **GET** /api/healthcheck/ | Ping


# **info_api_healthcheck_info_get**
> Stayforge info_api_healthcheck_info_get()

Info

Stayforge API Info

### Example


```python
import openapi_client
from openapi_client.models.stayforge import Stayforge
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
    api_instance = openapi_client.HealthcheckApi(api_client)

    try:
        # Info
        api_response = api_instance.info_api_healthcheck_info_get()
        print("The response of HealthcheckApi->info_api_healthcheck_info_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HealthcheckApi->info_api_healthcheck_info_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**Stayforge**](Stayforge.md)

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

# **ping_api_healthcheck_get**
> object ping_api_healthcheck_get()

Ping

ping! pong! ping!ping!ping!......pong?

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
    api_instance = openapi_client.HealthcheckApi(api_client)

    try:
        # Ping
        api_response = api_instance.ping_api_healthcheck_get()
        print("The response of HealthcheckApi->ping_api_healthcheck_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HealthcheckApi->ping_api_healthcheck_get: %s\n" % e)
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
**200** | pong |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

