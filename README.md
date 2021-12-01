# Projeto Shipay
## Algumas ressalvas
Como alguns exercícios exigiam escrita separada da estrutura da API, as respostas para exercícios específicos estão na pasta `shipay/exs/`. O código referente a API está no pacote `shipay` no diretório raiz.

Foi adicionada uma rota `/api/v1/role` para fazer a adição de uma `role`, já que para testar a rota de adição de usuário, será necessário uma `role` pré-cadastrada, e também uma rota `/api/v1/roles` para listar as roles cadastradas.

## Executando

### Executando os testes
Para executar todos os testes, a partir do diretório raiz, execute: `docker build -t tests --target tests .`, ou então `poetry run pytest` caso possua o `poetry` instalado localmente (será necessário rodar `poetry install` para instalar as dependências antes).

### Localmente
Entre no diretório raiz do projeto shipay e execute `docker-compose up` e a aplicação estará escutando na porta 5000.

### Em deploy
Para dar deploy seria necessário ainda configurar o projeto com um WSGI de produção, como o gunicorn ou uwsgi, além de atualizar as variáveis de ambiente para retirar o status de development da aplicação e, caso a API seja fechada, gerar uma chave secreta de acesso.

## Info
**Schemes**: http://
**Base URL**: localhost:5000/api/v1

## Endpoints
### /user_role/<user_id>
#### GET
Resumo: Pega a `role_id` de um usuário a partir do `user_id`

### /roles
#### GET
Resumo: Retorna todas as roles cadastradas

### /user
#### POST
Resumo: Cria um usuário a partir da informação passada pelo `json`
Campos obrigatórios:
    `name`, `email`, `role`

### /role
#### POST
Resumo: Cria uma role a partir da informação passada pelo `json`
Campos obrigatórios:
    `description`
