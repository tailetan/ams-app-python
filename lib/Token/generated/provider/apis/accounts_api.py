# coding: utf-8

"""
AccountsApi.py
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


class AccountsApi(object):
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

    def create_account_route(self, request, **kwargs):
        """
        Create account
        Create an account.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_account_route(request, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param CreateAccountRequest request:  (required)
        :param str authorization: Authorization scheme and credentials.
        :return: CreateAccountResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['request', 'authorization']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_account_route" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'request' is set
        if ('request' not in params) or (params['request'] is None):
            raise ValueError("Missing the required parameter `request` when calling `create_account_route`")

        resource_path = '/accounts'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']

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
                                            response_type='CreateAccountResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def delete_account_route(self, account_id, **kwargs):
        """
        Delete account
        Delete an account.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_account_route(account_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str account_id: Unique id for an account. (required)
        :param str authorization: Authorization scheme and credentials.
        :return: Function1RequestContextBoxedUnit
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_id', 'authorization']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_account_route" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'account_id' is set
        if ('account_id' not in params) or (params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `delete_account_route`")

        resource_path = '/accounts/{accountId}'.replace('{format}', 'json')
        path_params = {}
        if 'account_id' in params:
            path_params['accountId'] = params['account_id']

        query_params = {}

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']

        form_params = []
        local_var_files = {}

        body_params = None

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

        response = self.api_client.call_api(resource_path, 'DELETE',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='Function1RequestContextBoxedUnit',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_account_route(self, account_id, **kwargs):
        """
        Get account
        Retrieve an account.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_account_route(account_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str account_id: Unique id for an account. (required)
        :param str authorization: Authorization scheme and credentials.
        :return: GetAccountResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_id', 'authorization']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_account_route" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'account_id' is set
        if ('account_id' not in params) or (params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `get_account_route`")

        resource_path = '/accounts/{accountId}'.replace('{format}', 'json')
        path_params = {}
        if 'account_id' in params:
            path_params['accountId'] = params['account_id']

        query_params = {}

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']

        form_params = []
        local_var_files = {}

        body_params = None

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

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='GetAccountResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_accounts_route(self, **kwargs):
        """
        Get accounts
        Retrieve a list of accounts.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_accounts_route(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str authorization: Authorization scheme and credentials.
        :return: GetAccountsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['authorization']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_accounts_route" % key
                )
            params[key] = val
        del params['kwargs']


        resource_path = '/accounts'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']

        form_params = []
        local_var_files = {}

        body_params = None

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

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='GetAccountsResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_transactions_route(self, account_id, page_offset, page_limit, **kwargs):
        """
        Get transactions
        Retrieve transactions.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_transactions_route(account_id, page_offset, page_limit, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str account_id: Unique id for an account. (required)
        :param int page_offset: Offset for the page. The number of rows to skip from the selected sequence. (required)
        :param int page_limit: Limit for the page. The maximum number of rows to take from the selected sequence. (required)
        :param str authorization: Authorization scheme and credentials.
        :return: GetTransactionsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_id', 'page_offset', 'page_limit', 'authorization']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_transactions_route" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'account_id' is set
        if ('account_id' not in params) or (params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `get_transactions_route`")
        # verify the required parameter 'page_offset' is set
        if ('page_offset' not in params) or (params['page_offset'] is None):
            raise ValueError("Missing the required parameter `page_offset` when calling `get_transactions_route`")
        # verify the required parameter 'page_limit' is set
        if ('page_limit' not in params) or (params['page_limit'] is None):
            raise ValueError("Missing the required parameter `page_limit` when calling `get_transactions_route`")

        resource_path = '/accounts/{accountId}/transactions'.replace('{format}', 'json')
        path_params = {}
        if 'account_id' in params:
            path_params['accountId'] = params['account_id']

        query_params = {}
        if 'page_offset' in params:
            query_params['pageOffset'] = params['page_offset']
        if 'page_limit' in params:
            query_params['pageLimit'] = params['page_limit']

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']

        form_params = []
        local_var_files = {}

        body_params = None

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

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='GetTransactionsResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response