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


class Terms(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        Terms - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'currency': 'str',
            'single_payment': 'TermsSinglePayment',
            'multi_payment': 'TermsMultiPayment',
            'effective': 'str',
            'expires': 'str'
        }

        self.attribute_map = {
            'currency': 'currency',
            'single_payment': 'singlePayment',
            'multi_payment': 'multiPayment',
            'effective': 'effective',
            'expires': 'expires'
        }

        self._currency = None
        self._single_payment = None
        self._multi_payment = None
        self._effective = None
        self._expires = None

    @property
    def currency(self):
        """
        Gets the currency of this Terms.


        :return: The currency of this Terms.
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """
        Sets the currency of this Terms.


        :param currency: The currency of this Terms.
        :type: str
        """
        self._currency = currency

    @property
    def single_payment(self):
        """
        Gets the single_payment of this Terms.


        :return: The single_payment of this Terms.
        :rtype: TermsSinglePayment
        """
        return self._single_payment

    @single_payment.setter
    def single_payment(self, single_payment):
        """
        Sets the single_payment of this Terms.


        :param single_payment: The single_payment of this Terms.
        :type: TermsSinglePayment
        """
        self._single_payment = single_payment

    @property
    def multi_payment(self):
        """
        Gets the multi_payment of this Terms.


        :return: The multi_payment of this Terms.
        :rtype: TermsMultiPayment
        """
        return self._multi_payment

    @multi_payment.setter
    def multi_payment(self, multi_payment):
        """
        Sets the multi_payment of this Terms.


        :param multi_payment: The multi_payment of this Terms.
        :type: TermsMultiPayment
        """
        self._multi_payment = multi_payment

    @property
    def effective(self):
        """
        Gets the effective of this Terms.


        :return: The effective of this Terms.
        :rtype: str
        """
        return self._effective

    @effective.setter
    def effective(self, effective):
        """
        Sets the effective of this Terms.


        :param effective: The effective of this Terms.
        :type: str
        """
        self._effective = effective

    @property
    def expires(self):
        """
        Gets the expires of this Terms.


        :return: The expires of this Terms.
        :rtype: str
        """
        return self._expires

    @expires.setter
    def expires(self, expires):
        """
        Sets the expires of this Terms.


        :param expires: The expires of this Terms.
        :type: str
        """
        self._expires = expires

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

