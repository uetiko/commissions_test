import abc


class Commission(abc.ABC):
    @abc.abstractmethod
    def get_commission(self):
        """
        :return: float
        """
        pass

    @abc.abstractmethod
    def set_commission(self, commission):
        pass

    @abc.abstractmethod
    def commision_calculation(self, reservacion):
        pass
