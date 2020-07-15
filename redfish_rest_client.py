#!/usr/bin/python3.7

import requests
import warnings
import base64
import json
from urllib3.exceptions import InsecureRequestWarning
warnings.simplefilter('ignore', InsecureRequestWarning)


class RedfishClient:
    def __init__(self, base_url, username=None, password=None, default_prefix='/redfish/v1/', timeout=3):
        self.__base_url = base_url
        self.__username = username
        self.__password = password
        self.__default_prefix = default_prefix
        self.__timeout = timeout
        self.__default_content_type = "application/json"

    def __get_encode_auth_key_in_base64(self):
        if self.__username and self.__password:
            return base64.b64encode((f"{self.__username}:{self.__password}").encode("utf-8")).decode("utf-8")
        else:
            return None

    # Default using basic auth
    def __restful_request(self, method="GET", url="/redfish/v1/", headers=None, payload=None, auth="basic"):
        target_url = f"{self.__base_url}{url}"

        request_headers = dict()
        if headers:
            request_headers = dict(headers)

        request_body = dict()
        if payload:
            request_body = json.dumps(payload)

        if auth == "basic":
            request_headers["Authorization"] = 'Basic {base64_auth_key}'.format(
                base64_auth_key=self.__get_encode_auth_key_in_base64())

        request_headers["Content-Type"] = self.__default_content_type

        raw_response = requests.request(
            method, target_url, headers=request_headers, verify=False, data=request_body, timeout=self.__timeout)

        response = dict()
        response["status_code"] = raw_response.status_code
        response["headers"] = raw_response.headers
        if len(raw_response.text) > 0:
            response["body"] = json.loads(raw_response.text)
        else:
            response["body"] = ""

        return response

    def GET(self, resource_url, headers=None, payload=None, auth="basic"):
        return self.__restful_request(method="GET", url=resource_url, headers=headers, payload=payload, auth=auth)

    def POST(self, resource_url, headers=None, payload=None, auth="basic"):
        return self.__restful_request(method="POST", url=resource_url, headers=headers, payload=payload, auth=auth)

    def PATCH(self, resource_url, headers=None, payload=None, auth="basic"):
        return self.__restful_request(method="PATCH", url=resource_url, headers=headers, payload=payload, auth=auth)

    def DELETE(self, resource_url, headers=None, payload=None, auth="basic"):
        return self.__restful_request(method="DELETE", url=resource_url, headers=headers, payload=payload, auth=auth)

    def HEAD(self, resource_url, headers=None, payload=None, auth="basic"):
        return self.__restful_request(method="HEAD", url=resource_url, headers=headers, payload=payload, auth=auth)

    def PUT(self, resource_url, headers=None, payload=None, auth="basic"):
        return self.__restful_request(method="PUT", url=resource_url, headers=headers, payload=payload, auth=auth)
