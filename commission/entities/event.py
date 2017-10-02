from entities.db import DataBase


class Event(object):
    _user = None
    _id_event = None

    def set_user(self, user):
        self._user = user

    def get_commission(self):
        return self._commision

    def get_payment(self):
        return self._payment
