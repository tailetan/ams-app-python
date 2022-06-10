# coding: utf-8

"""
MembersApi.py
Copyright 2016 SmartBear Software

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

from __future__ import absolute_import

import sys
import os

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class MembersApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def create_device_route(self, member_id, request, **kwargs):
        """
        Create device
        Create unverified device.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_device_route(member_id, request, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str member_id: Unique id for a member. (required)
        :param CreateDeviceRequest request:  (required)
        :return: CreateDeviceResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['member_id', 'request']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_device_route" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'member_id' is set
        if ('member_id' not in params) or (params['member_id'] is None):
            raise ValueError("Missing the required parameter `member_id` when calling `create_device_route`")
        # verify the required parameter 'request' is set
        if ('request' not in params) or (params['request'] is None):
            raise ValueError("Missing the required parameter `request` when calling `create_device_route`")

        resource_path = '/members/{memberId}/devices'.replace('{format}', 'json')
        path_params = {}
        if 'member_id' in params:
            path_params['memberId'] = params['member_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'request' in params:
            body_params = params['request']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept([])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='CreateDeviceResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def create_member_route(self, request, **kwargs):
        """
        Create member
        Create a member and its first device

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_member_route(request, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param CreateMemberRequest request:  (required)
        :return: CreateMemberResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['request']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_member_route" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'request' is set
        if ('request' not in params) or (params['request'] is None):
            raise ValueError("Missing the required parameter `request` when calling `create_member_route`")

        resource_path = '/members'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'request' in params:
            body_params = params['request']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept([])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='CreateMemberResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response