from bottle import Bottle, request, redirect

app = Bottle()

# Dados dos usuários
usuarios = []

# Rota inicial (home)
@app.route('/')
def home():
    return "Bem-vindo à página inicial!"

# Rota de cadastro de usuário
@app.route('/cadastro', method='GET')
def exibir_formulario_cadastro():
    return '''
        <form action="/cadastro" method="post">
            <input type="text" name="username" placeholder="Nome de usuário"><br>
            <input type="password" name="password" placeholder="Senha"><br>
            <input type="submit" value="Cadastrar">
        </form>
    '''

@app.route('/cadastro', method='POST')
def cadastrar_usuario():
    username = request.forms.get('username')
    password = request.forms.get('password')
    usuarios.append({'username': username, 'password': password})
    return "Usuário cadastrado com sucesso!"

# Rota de login
@app.route('/login', method='GET')
def exibir_formulario_login():
    return '''
        <form action="/login" method="post">
            <input type="text" name="username" placeholder="Nome de usuário"><br>
            <input type="password" name="password" placeholder="Senha"><br>
            <input type="submit" value="Login">
        </form>
    '''

@app.route('/login', method='POST')
def realizar_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    for usuario in usuarios:
        if usuario['username'] == username and usuario['password'] == password:
            return f"Bem-vindo, {username}! Login realizado com sucesso."
    return "Usuário ou senha incorretos."

if __name__ == '__main__':
    app.run(host='localhost', port=8080)

