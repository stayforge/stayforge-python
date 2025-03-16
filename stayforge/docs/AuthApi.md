# stayforge.AuthApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authenticate_api_auth_authenticate_post**](AuthApi.md#authenticate_api_auth_authenticate_post) | **POST** /api/auth/authenticate | Authenticate
[**refresh_access_token_api_auth_refresh_access_token_post**](AuthApi.md#refresh_access_token_api_auth_refresh_access_token_post) | **POST** /api/auth/refresh_access_token | Refresh Access Token


# **authenticate_api_auth_authenticate_post**
> TokenResponse authenticate_api_auth_authenticate_post(body_authenticate_api_auth_authenticate_post)

Authenticate

This API gives you a cake(access_token) and a baker(refresh_token). But don’t keep the baker waiting—if you don’t put them to work within 2592000 seconds, they’ll walk out on you. No baker, no cake!

### Example


```python
import stayforge
from stayforge.models.body_authenticate_api_auth_authenticate_post import BodyAuthenticateApiAuthAuthenticatePost
from stayforge.models.token_response import TokenResponse
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
    api_instance = stayforge.AuthApi(api_client)
    body_authenticate_api_auth_authenticate_post = stayforge.BodyAuthenticateApiAuthAuthenticatePost() # BodyAuthenticateApiAuthAuthenticatePost | 

    try:
        # Authenticate
        api_response = api_instance.authenticate_api_auth_authenticate_post(body_authenticate_api_auth_authenticate_post)
        print("The response of AuthApi->authenticate_api_auth_authenticate_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->authenticate_api_auth_authenticate_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body_authenticate_api_auth_authenticate_post** | [**BodyAuthenticateApiAuthAuthenticatePost**](BodyAuthenticateApiAuthAuthenticatePost.md)|  | 

### Return type

[**TokenResponse**](TokenResponse.md)

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

# **refresh_access_token_api_auth_refresh_access_token_post**
> TokenResponse refresh_access_token_api_auth_refresh_access_token_post(token_refresh_request)

Refresh Access Token

Think of the `access_token` as the cake, and the Refresh Token as the baker—basically, the one that keeps the cake coming. When you've finished your cake, ask your baker to make your bread!

### Example


```python
import stayforge
from stayforge.models.token_refresh_request import TokenRefreshRequest
from stayforge.models.token_response import TokenResponse
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
    api_instance = stayforge.AuthApi(api_client)
    token_refresh_request = stayforge.TokenRefreshRequest() # TokenRefreshRequest | 

    try:
        # Refresh Access Token
        api_response = api_instance.refresh_access_token_api_auth_refresh_access_token_post(token_refresh_request)
        print("The response of AuthApi->refresh_access_token_api_auth_refresh_access_token_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->refresh_access_token_api_auth_refresh_access_token_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_refresh_request** | [**TokenRefreshRequest**](TokenRefreshRequest.md)|  | 

### Return type

[**TokenResponse**](TokenResponse.md)

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

