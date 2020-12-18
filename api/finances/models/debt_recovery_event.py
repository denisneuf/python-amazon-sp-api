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


class DebtRecoveryEvent(object):
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
        'debt_recovery_type': 'str',
        'recovery_amount': 'Currency',
        'over_payment_credit': 'Currency',
        'debt_recovery_item_list': 'DebtRecoveryItemList',
        'charge_instrument_list': 'ChargeInstrumentList'
    }

    attribute_map = {
        'debt_recovery_type': 'DebtRecoveryType',
        'recovery_amount': 'RecoveryAmount',
        'over_payment_credit': 'OverPaymentCredit',
        'debt_recovery_item_list': 'DebtRecoveryItemList',
        'charge_instrument_list': 'ChargeInstrumentList'
    }

    def __init__(self, debt_recovery_type=None, recovery_amount=None, over_payment_credit=None, debt_recovery_item_list=None, charge_instrument_list=None):  # noqa: E501
        """DebtRecoveryEvent - a model defined in Swagger"""  # noqa: E501
        self._debt_recovery_type = None
        self._recovery_amount = None
        self._over_payment_credit = None
        self._debt_recovery_item_list = None
        self._charge_instrument_list = None
        self.discriminator = None
        if debt_recovery_type is not None:
            self.debt_recovery_type = debt_recovery_type
        if recovery_amount is not None:
            self.recovery_amount = recovery_amount
        if over_payment_credit is not None:
            self.over_payment_credit = over_payment_credit
        if debt_recovery_item_list is not None:
            self.debt_recovery_item_list = debt_recovery_item_list
        if charge_instrument_list is not None:
            self.charge_instrument_list = charge_instrument_list

    @property
    def debt_recovery_type(self):
        """Gets the debt_recovery_type of this DebtRecoveryEvent.  # noqa: E501

        The debt recovery type.  Possible values:  * DebtPayment  * DebtPaymentFailure  *DebtAdjustment  # noqa: E501

        :return: The debt_recovery_type of this DebtRecoveryEvent.  # noqa: E501
        :rtype: str
        """
        return self._debt_recovery_type

    @debt_recovery_type.setter
    def debt_recovery_type(self, debt_recovery_type):
        """Sets the debt_recovery_type of this DebtRecoveryEvent.

        The debt recovery type.  Possible values:  * DebtPayment  * DebtPaymentFailure  *DebtAdjustment  # noqa: E501

        :param debt_recovery_type: The debt_recovery_type of this DebtRecoveryEvent.  # noqa: E501
        :type: str
        """

        self._debt_recovery_type = debt_recovery_type

    @property
    def recovery_amount(self):
        """Gets the recovery_amount of this DebtRecoveryEvent.  # noqa: E501


        :return: The recovery_amount of this DebtRecoveryEvent.  # noqa: E501
        :rtype: Currency
        """
        return self._recovery_amount

    @recovery_amount.setter
    def recovery_amount(self, recovery_amount):
        """Sets the recovery_amount of this DebtRecoveryEvent.


        :param recovery_amount: The recovery_amount of this DebtRecoveryEvent.  # noqa: E501
        :type: Currency
        """

        self._recovery_amount = recovery_amount

    @property
    def over_payment_credit(self):
        """Gets the over_payment_credit of this DebtRecoveryEvent.  # noqa: E501


        :return: The over_payment_credit of this DebtRecoveryEvent.  # noqa: E501
        :rtype: Currency
        """
        return self._over_payment_credit

    @over_payment_credit.setter
    def over_payment_credit(self, over_payment_credit):
        """Sets the over_payment_credit of this DebtRecoveryEvent.


        :param over_payment_credit: The over_payment_credit of this DebtRecoveryEvent.  # noqa: E501
        :type: Currency
        """

        self._over_payment_credit = over_payment_credit

    @property
    def debt_recovery_item_list(self):
        """Gets the debt_recovery_item_list of this DebtRecoveryEvent.  # noqa: E501


        :return: The debt_recovery_item_list of this DebtRecoveryEvent.  # noqa: E501
        :rtype: DebtRecoveryItemList
        """
        return self._debt_recovery_item_list

    @debt_recovery_item_list.setter
    def debt_recovery_item_list(self, debt_recovery_item_list):
        """Sets the debt_recovery_item_list of this DebtRecoveryEvent.


        :param debt_recovery_item_list: The debt_recovery_item_list of this DebtRecoveryEvent.  # noqa: E501
        :type: DebtRecoveryItemList
        """

        self._debt_recovery_item_list = debt_recovery_item_list

    @property
    def charge_instrument_list(self):
        """Gets the charge_instrument_list of this DebtRecoveryEvent.  # noqa: E501


        :return: The charge_instrument_list of this DebtRecoveryEvent.  # noqa: E501
        :rtype: ChargeInstrumentList
        """
        return self._charge_instrument_list

    @charge_instrument_list.setter
    def charge_instrument_list(self, charge_instrument_list):
        """Sets the charge_instrument_list of this DebtRecoveryEvent.


        :param charge_instrument_list: The charge_instrument_list of this DebtRecoveryEvent.  # noqa: E501
        :type: ChargeInstrumentList
        """

        self._charge_instrument_list = charge_instrument_list

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
        if issubclass(DebtRecoveryEvent, dict):
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
        if not isinstance(other, DebtRecoveryEvent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
