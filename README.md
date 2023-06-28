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
