import jwt
from bottle import request, HTTPError

def jwt_auth_middleware(callback):
    def wrapper(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token or not token.startswith('Bearer '):
            return HTTPError(401, 'Token de autenticação não fornecido.')

        token = token.split(' ')[1]  # Remove o prefixo 'Bearer '

        try:
            # Verificar e decodificar o token JWT
            decoded = jwt.decode(token, 'sua_chave_secreta', algorithms=['HS256'])
            # Adicionar informações do usuário ao contexto
            request.user = decoded['user']
        except jwt.ExpiredSignatureError:
            return HTTPError(401, 'Token de autenticação expirado.')
        except (jwt.InvalidTokenError, KeyError):
            return HTTPError(401, 'Token de autenticação inválido.')

        return callback(*args, **kwargs)

    return wrapper
