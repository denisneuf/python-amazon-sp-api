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


class ProductAdsPaymentEvent(object):
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
        'transaction_type': 'str',
        'invoice_id': 'str',
        'base_value': 'Currency',
        'tax_value': 'Currency',
        'transaction_value': 'Currency'
    }

    attribute_map = {
        'posted_date': 'postedDate',
        'transaction_type': 'transactionType',
        'invoice_id': 'invoiceId',
        'base_value': 'baseValue',
        'tax_value': 'taxValue',
        'transaction_value': 'transactionValue'
    }

    def __init__(self, posted_date=None, transaction_type=None, invoice_id=None, base_value=None, tax_value=None, transaction_value=None):  # noqa: E501
        """ProductAdsPaymentEvent - a model defined in Swagger"""  # noqa: E501
        self._posted_date = None
        self._transaction_type = None
        self._invoice_id = None
        self._base_value = None
        self._tax_value = None
        self._transaction_value = None
        self.discriminator = None
        if posted_date is not None:
            self.posted_date = posted_date
        if transaction_type is not None:
            self.transaction_type = transaction_type
        if invoice_id is not None:
            self.invoice_id = invoice_id
        if base_value is not None:
            self.base_value = base_value
        if tax_value is not None:
            self.tax_value = tax_value
        if transaction_value is not None:
            self.transaction_value = transaction_value

    @property
    def posted_date(self):
        """Gets the posted_date of this ProductAdsPaymentEvent.  # noqa: E501


        :return: The posted_date of this ProductAdsPaymentEvent.  # noqa: E501
        :rtype: ModelDate
        """
        return self._posted_date

    @posted_date.setter
    def posted_date(self, posted_date):
        """Sets the posted_date of this ProductAdsPaymentEvent.


        :param posted_date: The posted_date of this ProductAdsPaymentEvent.  # noqa: E501
        :type: ModelDate
        """

        self._posted_date = posted_date

    @property
    def transaction_type(self):
        """Gets the transaction_type of this ProductAdsPaymentEvent.  # noqa: E501

        Indicates if the transaction is for a charge or a refund.  Possible values:  * charge - Charge  * refund - Refund  # noqa: E501

        :return: The transaction_type of this ProductAdsPaymentEvent.  # noqa: E501
        :rtype: str
        """
        return self._transaction_type

    @transaction_type.setter
    def transaction_type(self, transaction_type):
        """Sets the transaction_type of this ProductAdsPaymentEvent.

        Indicates if the transaction is for a charge or a refund.  Possible values:  * charge - Charge  * refund - Refund  # noqa: E501

        :param transaction_type: The transaction_type of this ProductAdsPaymentEvent.  # noqa: E501
        :type: str
        """

        self._transaction_type = transaction_type

    @property
    def invoice_id(self):
        """Gets the invoice_id of this ProductAdsPaymentEvent.  # noqa: E501

        Identifier for the invoice that the transaction appears in.  # noqa: E501

        :return: The invoice_id of this ProductAdsPaymentEvent.  # noqa: E501
        :rtype: str
        """
        return self._invoice_id

    @invoice_id.setter
    def invoice_id(self, invoice_id):
        """Sets the invoice_id of this ProductAdsPaymentEvent.

        Identifier for the invoice that the transaction appears in.  # noqa: E501

        :param invoice_id: The invoice_id of this ProductAdsPaymentEvent.  # noqa: E501
        :type: str
        """

        self._invoice_id = invoice_id

    @property
    def base_value(self):
        """Gets the base_value of this ProductAdsPaymentEvent.  # noqa: E501


        :return: The base_value of this ProductAdsPaymentEvent.  # noqa: E501
        :rtype: Currency
        """
        return self._base_value

    @base_value.setter
    def base_value(self, base_value):
        """Sets the base_value of this ProductAdsPaymentEvent.


        :param base_value: The base_value of this ProductAdsPaymentEvent.  # noqa: E501
        :type: Currency
        """

        self._base_value = base_value

    @property
    def tax_value(self):
        """Gets the tax_value of this ProductAdsPaymentEvent.  # noqa: E501


        :return: The tax_value of this ProductAdsPaymentEvent.  # noqa: E501
        :rtype: Currency
        """
        return self._tax_value

    @tax_value.setter
    def tax_value(self, tax_value):
        """Sets the tax_value of this ProductAdsPaymentEvent.


        :param tax_value: The tax_value of this ProductAdsPaymentEvent.  # noqa: E501
        :type: Currency
        """

        self._tax_value = tax_value

    @property
    def transaction_value(self):
        """Gets the transaction_value of this ProductAdsPaymentEvent.  # noqa: E501


        :return: The transaction_value of this ProductAdsPaymentEvent.  # noqa: E501
        :rtype: Currency
        """
        return self._transaction_value

    @transaction_value.setter
    def transaction_value(self, transaction_value):
        """Sets the transaction_value of this ProductAdsPaymentEvent.


        :param transaction_value: The transaction_value of this ProductAdsPaymentEvent.  # noqa: E501
        :type: Currency
        """

        self._transaction_value = transaction_value

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
        if issubclass(ProductAdsPaymentEvent, dict):
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
        if not isinstance(other, ProductAdsPaymentEvent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
