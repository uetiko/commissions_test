from sqlalchemy import create_engine, BoundMetaData, Table
from sqlalchemy import mapper, create_session
import os
from sales.commision import UserCommission as User
from sales.commision import EventCommission as Event
from sales.commision import PaymentCommission as Payment


class DataBase(object):
    __event = None
    __user = None
    __payment = None
    _session = None

    def __init__(self):
        self._db = create_engine(os.getenv('DB_DRIVER'))
        self._metadata = BoundMetaData(self.__db)
        self.__user = mapper(
            User, Table(
                os.getenv('USER_TABLE'), self._metadata, autoload=True
            )
        )
        self.__event = mapper(
            Event, Table(
                os.getenv('EVENT_TABLE'), self._metadata, autoload=True
            )
        )
        self.__payment = mapper(
            Payment, Table(
                os.getenv('PAYMENT_TABLE'), self._metadata, autoload=True
            )
        )
        self._session = create_session()

    def get_event(self, id_event):
        return self._session.query(self._event).filter_by(id=id_event)

    def get_user(self, id_user):
        return self._session.query(self._user).filter_by(id=id_user)

    def get_payment(self, id_payment):
        return self._session.query(self._payment).filter_by(id=id_payment)
