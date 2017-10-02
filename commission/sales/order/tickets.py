class Ticket(object):
    __ticket_type_id = None
    __ticket_type_name = None
    __assigned = None

    def __init__(self):
        self.__assigned = False
        self.__ticket_type_id = int
        self.__ticket_type_name = str

    def set_ticket_type_name(self, ticket_type_name):
        self.__ticket_type_name = ticket_type_name

    def get_ticket_type_name(self):
        return self.__ticket_type_name

    def set_ticket_type_id(self, ticket_type_id):
        self.__ticket_type_id = ticket_type_id

    def get_ticket_type_id(self):
        return self.__ticket_type_id

    def set_assigned(self, assigned):
        self.__assigned = assigned
