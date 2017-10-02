from entities import Payment
from entities import Invoice
from entities.db import DataBase


class Order(object):
    __items = None
    __payment = None
    __invoice = None
    _billing_address = None
    _subtotal = None
    _grant_total = None
    _commision = None
    _db = None
    _id_event = None
    _id_user = None
    _id_payment = None

    def __init__(self):
        self.__items = list()
        self.__payment = Payment()
        self.__invoice = Invoice()
        self._db = DataBase()

    def set_id_event(self, id_event):
        self._id_event = id_event

    def set_id_user(self, id_user):
        self._id_user = id_user

    def set_id_payment(self, id_payment):
        self.set_id_payment = id_payment

    def get_payment(self):
        return self.__payment

    def set_payment(self, payment):
        self.__payment = payment

    def get_billing_address(self):
        return self._billing_address

    def set_billing_address(self, address):
        self._billing_address = address

    def get_shipping_address(self):
        return self._shipping_address

    def set_shipping_address(self, address):
        self._shipping_address = address

    def get_all_items(self):
        self.__items

    def get_sub_total(self):
        return self._subtotal

    def get_commission(self):
        if self._db.get_event(self._id_event).count() > 0:
            self.__event = self._db.get_event().all()
            self._commision = self.__event.commision

        elif self._db.get_user(self._id_user).count > 0:
            self._user = self._db.get_user(self._id_user).all()
            self._commision = self._user.commision
        else:
            self.__payment = self._db.get_payment(self._id_payment).all()
            self._commision = self._payment.commision

        return self._commision

    def get_grant_total(self):
        return self._grant_total

    def get_commission_by_order(self):
        return self._commision_total

    def set_type_commission(self, commission):
        self._commision = commission

    def get_event(self):
        return self._event

    def commision_calculation(self):
        self._commision_total = round(self._subtotal * self._commision, 2)
        self._grant_total = round((self._subtotal + self._commision_total), 2)
