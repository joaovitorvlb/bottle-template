from bottle import request
from models.user import User

class AuthController:
    @staticmethod
    def show_login_form():
        return '''
            <form action="/login" method="post">
                <input type="text" name="username" placeholder="Nome de usuário"><br>
                <input type="password" name="password" placeholder="Senha"><br>
                <input type="submit" value="Login">
            </form>
        '''

    @staticmethod
    def login():
        username = request.forms.get('username')
        password = request.forms.get('password')
        if User.authenticate(username, password):
            return f"Bem-vindo, {username}! Login realizado com sucesso."
        return "Usuário ou senha incorretos."
