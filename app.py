from bottle import Bottle, redirect, run
from controllers.home_controller import HomeController
from controllers.user_controller import UserController
from controllers.auth_controller import AuthController
from middleware import jwt_auth_middleware

app = Bottle()

# Rotas
app.route('/', method='GET', callback=jwt_auth_middleware(HomeController.index))

app.route('/cadastro', method='GET', callback=UserController.show_registration_form)
app.route('/cadastro', method='POST', callback=UserController.register)

app.route('/login', method='GET', callback=AuthController.show_login_form)
app.route('/login', method='POST', callback=AuthController.login)

if __name__ == '__main__':
    run(app, host='localhost', port=8080)