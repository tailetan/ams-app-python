# coding: utf-8

"""
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

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from pprint import pformat
from six import iteritems


class CreateTokenRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        CreateTokenRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'payer': 'CreateTokenRequestPayer',
            'payee': 'CreateTokenRequestPayee',
            'description': 'str',
            'terms': 'Terms'
        }

        self.attribute_map = {
            'payer': 'payer',
            'payee': 'payee',
            'description': 'description',
            'terms': 'terms'
        }

        self._payer = None
        self._payee = None
        self._description = None
        self._terms = None

    @property
    def payer(self):
        """
        Gets the payer of this CreateTokenRequest.


        :return: The payer of this CreateTokenRequest.
        :rtype: CreateTokenRequestPayer
        """
        return self._payer

    @payer.setter
    def payer(self, payer):
        """
        Sets the payer of this CreateTokenRequest.


        :param payer: The payer of this CreateTokenRequest.
        :type: CreateTokenRequestPayer
        """
        self._payer = payer

    @property
    def payee(self):
        """
        Gets the payee of this CreateTokenRequest.


        :return: The payee of this CreateTokenRequest.
        :rtype: CreateTokenRequestPayee
        """
        return self._payee

    @payee.setter
    def payee(self, payee):
        """
        Sets the payee of this CreateTokenRequest.


        :param payee: The payee of this CreateTokenRequest.
        :type: CreateTokenRequestPayee
        """
        self._payee = payee

    @property
    def description(self):
        """
        Gets the description of this CreateTokenRequest.


        :return: The description of this CreateTokenRequest.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateTokenRequest.


        :param description: The description of this CreateTokenRequest.
        :type: str
        """
        self._description = description

    @property
    def terms(self):
        """
        Gets the terms of this CreateTokenRequest.


        :return: The terms of this CreateTokenRequest.
        :rtype: Terms
        """
        return self._terms

    @terms.setter
    def terms(self, terms):
        """
        Sets the terms of this CreateTokenRequest.


        :param terms: The terms of this CreateTokenRequest.
        :type: Terms
        """
        self._terms = terms

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

