# coding: utf-8

"""
    Selling Partner API for Finances

    The Selling Partner API for Finances helps you obtain financial information relevant to a seller's business. You can obtain financial events for a given order, financial event group, or date range without having to wait until a statement period closes. You can also obtain financial event groups for a given date range.  # noqa: E501

    OpenAPI spec version: v0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class Promotion(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'promotion_type': 'str',
        'promotion_id': 'str',
        'promotion_amount': 'Currency'
    }

    attribute_map = {
        'promotion_type': 'PromotionType',
        'promotion_id': 'PromotionId',
        'promotion_amount': 'PromotionAmount'
    }

    def __init__(self, promotion_type=None, promotion_id=None, promotion_amount=None):  # noqa: E501
        """Promotion - a model defined in Swagger"""  # noqa: E501
        self._promotion_type = None
        self._promotion_id = None
        self._promotion_amount = None
        self.discriminator = None
        if promotion_type is not None:
            self.promotion_type = promotion_type
        if promotion_id is not None:
            self.promotion_id = promotion_id
        if promotion_amount is not None:
            self.promotion_amount = promotion_amount

    @property
    def promotion_type(self):
        """Gets the promotion_type of this Promotion.  # noqa: E501

        The type of promotion.  # noqa: E501

        :return: The promotion_type of this Promotion.  # noqa: E501
        :rtype: str
        """
        return self._promotion_type

    @promotion_type.setter
    def promotion_type(self, promotion_type):
        """Sets the promotion_type of this Promotion.

        The type of promotion.  # noqa: E501

        :param promotion_type: The promotion_type of this Promotion.  # noqa: E501
        :type: str
        """

        self._promotion_type = promotion_type

    @property
    def promotion_id(self):
        """Gets the promotion_id of this Promotion.  # noqa: E501

        The seller-specified identifier for the promotion.  # noqa: E501

        :return: The promotion_id of this Promotion.  # noqa: E501
        :rtype: str
        """
        return self._promotion_id

    @promotion_id.setter
    def promotion_id(self, promotion_id):
        """Sets the promotion_id of this Promotion.

        The seller-specified identifier for the promotion.  # noqa: E501

        :param promotion_id: The promotion_id of this Promotion.  # noqa: E501
        :type: str
        """

        self._promotion_id = promotion_id

    @property
    def promotion_amount(self):
        """Gets the promotion_amount of this Promotion.  # noqa: E501


        :return: The promotion_amount of this Promotion.  # noqa: E501
        :rtype: Currency
        """
        return self._promotion_amount

    @promotion_amount.setter
    def promotion_amount(self, promotion_amount):
        """Sets the promotion_amount of this Promotion.


        :param promotion_amount: The promotion_amount of this Promotion.  # noqa: E501
        :type: Currency
        """

        self._promotion_amount = promotion_amount

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(Promotion, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Promotion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
