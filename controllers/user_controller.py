from bottle import request
from models.user import User

class UserController:
    @staticmethod
    def show_registration_form():
        return '''
            <form action="/cadastro" method="post">
                <input type="text" name="username" placeholder="Nome de usuário"><br>
                <input type="password" name="password" placeholder="Senha"><br>
                <input type="submit" value="Cadastrar">
            </form>
        '''

    @staticmethod
    def register():
        username = request.forms.get('username')
        password = request.forms.get('password')
        User.create(username, password)
        return "Usuário cadastrado com sucesso!"
