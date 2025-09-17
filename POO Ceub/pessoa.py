
class Pessoa:
    def __init__(self, id, nome, email):
        self._id = id
        self._nome = nome
        self._email = email

    def get_id(self):
        return self._id

    def get_nome(self):
        return self._nome

    def get_email(self):
        return self._email
