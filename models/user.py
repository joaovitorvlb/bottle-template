class User:
    usuarios = []

    @classmethod
    def create(cls, username, password):
        cls.usuarios.append({'username': username, 'password': password})

    @classmethod
    def authenticate(cls, username, password):
        for usuario in cls.usuarios:
            if usuario['username'] == username and usuario['password'] == password:
                return True
        return False
