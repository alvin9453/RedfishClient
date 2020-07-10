Requirements
 =============
1. Python3.7
2. Other packages
    ```
    pip3 install -r requirements
    ```
Usage
======
1. Import in python scripts
     ```
     from RedfishClient import *
     ```

2. Create a new RedfishClient object
    ```
    redfish_client = RedfishClient(base_url=context.redfish_host, username=admin, password=admin)
    ```

3. Send request with REST method(`GET/POST/DELETE/PATCH/HEAD/PUT`)

    ```
    redfish_client.GET("https://example.com/", auth="basic", headers=None, payload=None)
    redfish_client.POST("https://example.com/", auth="basic", headers=None, payload=None)
    redfish_client.PATCH("https://example.com/", auth="basic", headers=None, payload=None)
    redfish_client.DELETE("https://example.com/", auth="basic", headers=None, payload=None)
    ...
    ```

    The parameters `headers`, `payload`, `auth` can be specified if needed.
    
    ```
    my_payload = {
        'test' : 123
    }
    
    my_headers = {
        "Content-Type" : "application/json"
    }
    
    redfish_client.PATCH("https://example.com/", auth="basic", payload=my_payload, headers=my_headers)
    ```
    
    Note that `auth` now only support Basic Authentication("basic").
