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


class TermsMultiPaymentTotal(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        TermsMultiPaymentTotal - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'amount': 'int',
            'maximum_count': 'int'
        }

        self.attribute_map = {
            'amount': 'amount',
            'maximum_count': 'maximumCount'
        }

        self._amount = None
        self._maximum_count = None

    @property
    def amount(self):
        """
        Gets the amount of this TermsMultiPaymentTotal.


        :return: The amount of this TermsMultiPaymentTotal.
        :rtype: int
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """
        Sets the amount of this TermsMultiPaymentTotal.


        :param amount: The amount of this TermsMultiPaymentTotal.
        :type: int
        """
        self._amount = amount

    @property
    def maximum_count(self):
        """
        Gets the maximum_count of this TermsMultiPaymentTotal.


        :return: The maximum_count of this TermsMultiPaymentTotal.
        :rtype: int
        """
        return self._maximum_count

    @maximum_count.setter
    def maximum_count(self, maximum_count):
        """
        Sets the maximum_count of this TermsMultiPaymentTotal.


        :param maximum_count: The maximum_count of this TermsMultiPaymentTotal.
        :type: int
        """
        self._maximum_count = maximum_count

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

