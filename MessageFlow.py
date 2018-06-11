class MessageFlow:

    def __init__(self, _from, to, message):
        self._from, self.to, self.message = _from, to, message

    def __eq__(self, other): 
        return self.__dict__ == other.__dict__