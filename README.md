# Começando uma aplicação web com python e bottle

A instenção é criar uma aplicação web que apartir da index seja retornado um bem-vindo em json.

## Instalação do virtiualenv

* sudo apt install -y python3-venv


## Criação do virtual env

* virtualenv myenv

## ativando o ambiente virtual criado

* source myenv/bin/activate

## Quando precisar pode desativar o ambiente virtual

* deactivate

## Inatalação do micorframework bottle

* pip install bottle
* pip install PyJwt

## Execução da aplicação, ececutando o app.py

* python app.py

Acesse http://localhost:8080 em seu navegador para interagir com a aplicação.

Neste exemplo, temos as seguintes rotas:

    Rota inicial: '/' - Exibe uma mensagem de boas-vindas.
    Rota de cadastro de usuário: '/cadastro' - Exibe um formulário de cadastro de usuário. Quando o formulário é enviado via método POST, o usuário é cadastrado e a mensagem de sucesso é exibida.
    Rota de login: '/login' - Exibe um formulário de login. Quando o formulário é enviado via método POST, verifica-se se o usuário e senha correspondem aos dados cadastrados. Se forem corretos, uma mensagem de boas-vindas é exibida; caso contrário, uma mensagem de erro é exibida.

Primeiro se acessa a tela de cadastro via GET e usuário via POST e enviado e fica salvi no seção.

 
Para melhor organização e gerenciamento do projetos foi feita refatoração seguindo padrão MVC:

- main.py
- controllers/
    - home_controller.py
    - user_controller.py
    - auth_controller.py
- models/
    - user.py


Para testar começaremos a trestar as rotas no postman:


    Cadastro de Usuário:
        Método: POST
        URL: http://localhost:8080/cadastro
        Cabeçalhos:
            Content-Type: application/x-www-form-urlencoded
        Corpo (form data):
            username: [nome_de_usuario]
            password: [senha]

    Login de Usuário:
        Método: POST
        URL: http://localhost:8080/login
        Cabeçalhos:
            Content-Type: application/x-www-form-urlencoded
        Corpo (form data):
            username: [nome_de_usuario]
            password: [senha]
        Resposta: Você receberá um token JWT como resposta no corpo da mensagem.

    Acesso à Rota Home:
        Método: GET
        URL: http://localhost:8080/
        Cabeçalhos:
            Authorization: Bearer [seu_token_jwt]

Inclusive estamos peotegendo a rota index com jwt descrito abaixo.


Substitua [nome_de_usuario] e [senha] pelos valores desejados para o cadastro e login. Para acessar a rota home, substitua [seu_token_jwt] pelo token JWT gerado após o login bem-sucedido.

Certifique-se de ajustar a URL e a porta de acordo com a configuração do seu ambiente.

Usando o Postman, você pode adicionar facilmente os cabeçalhos necessários para cada solicitação. Certifique-se de selecionar o método correto, definir a URL correta e incluir os cabeçalhos apropriados em cada solicitação.

Lembre-se de que, para acessar a rota home, você deve fornecer o token JWT no cabeçalho Authorization, usando o prefixo Bearer.
