import abc
from sales.interfaces.base import Commission


class AbstractCommision(Commission):
    commision = None
    __metaclass__ = abc.ABCMeta

    def get_commission(self):
        return self._commision

    def set_commission(self, commission):
        self._commision = commission


class UserCommission(AbstractCommision):
    _id_user = None


class EventCommission(AbstractCommision):
    _id_event = None


class PaymentCommission(AbstractCommision):
    _id_payment = None
