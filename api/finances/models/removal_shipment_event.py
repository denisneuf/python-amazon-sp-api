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


class RemovalShipmentEvent(object):
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
        'posted_date': 'ModelDate',
        'order_id': 'str',
        'transaction_type': 'str',
        'removal_shipment_item_list': 'RemovalShipmentItemList'
    }

    attribute_map = {
        'posted_date': 'PostedDate',
        'order_id': 'OrderId',
        'transaction_type': 'TransactionType',
        'removal_shipment_item_list': 'RemovalShipmentItemList'
    }

    def __init__(self, posted_date=None, order_id=None, transaction_type=None, removal_shipment_item_list=None):  # noqa: E501
        """RemovalShipmentEvent - a model defined in Swagger"""  # noqa: E501
        self._posted_date = None
        self._order_id = None
        self._transaction_type = None
        self._removal_shipment_item_list = None
        self.discriminator = None
        if posted_date is not None:
            self.posted_date = posted_date
        if order_id is not None:
            self.order_id = order_id
        if transaction_type is not None:
            self.transaction_type = transaction_type
        if removal_shipment_item_list is not None:
            self.removal_shipment_item_list = removal_shipment_item_list

    @property
    def posted_date(self):
        """Gets the posted_date of this RemovalShipmentEvent.  # noqa: E501


        :return: The posted_date of this RemovalShipmentEvent.  # noqa: E501
        :rtype: ModelDate
        """
        return self._posted_date

    @posted_date.setter
    def posted_date(self, posted_date):
        """Sets the posted_date of this RemovalShipmentEvent.


        :param posted_date: The posted_date of this RemovalShipmentEvent.  # noqa: E501
        :type: ModelDate
        """

        self._posted_date = posted_date

    @property
    def order_id(self):
        """Gets the order_id of this RemovalShipmentEvent.  # noqa: E501

        The identifier for the removal shipment order.  # noqa: E501

        :return: The order_id of this RemovalShipmentEvent.  # noqa: E501
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this RemovalShipmentEvent.

        The identifier for the removal shipment order.  # noqa: E501

        :param order_id: The order_id of this RemovalShipmentEvent.  # noqa: E501
        :type: str
        """

        self._order_id = order_id

    @property
    def transaction_type(self):
        """Gets the transaction_type of this RemovalShipmentEvent.  # noqa: E501

        The type of removal order.  Possible values:  * WHOLESALE_LIQUIDATION  # noqa: E501

        :return: The transaction_type of this RemovalShipmentEvent.  # noqa: E501
        :rtype: str
        """
        return self._transaction_type

    @transaction_type.setter
    def transaction_type(self, transaction_type):
        """Sets the transaction_type of this RemovalShipmentEvent.

        The type of removal order.  Possible values:  * WHOLESALE_LIQUIDATION  # noqa: E501

        :param transaction_type: The transaction_type of this RemovalShipmentEvent.  # noqa: E501
        :type: str
        """

        self._transaction_type = transaction_type

    @property
    def removal_shipment_item_list(self):
        """Gets the removal_shipment_item_list of this RemovalShipmentEvent.  # noqa: E501


        :return: The removal_shipment_item_list of this RemovalShipmentEvent.  # noqa: E501
        :rtype: RemovalShipmentItemList
        """
        return self._removal_shipment_item_list

    @removal_shipment_item_list.setter
    def removal_shipment_item_list(self, removal_shipment_item_list):
        """Sets the removal_shipment_item_list of this RemovalShipmentEvent.


        :param removal_shipment_item_list: The removal_shipment_item_list of this RemovalShipmentEvent.  # noqa: E501
        :type: RemovalShipmentItemList
        """

        self._removal_shipment_item_list = removal_shipment_item_list

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
        if issubclass(RemovalShipmentEvent, dict):
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
        if not isinstance(other, RemovalShipmentEvent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
