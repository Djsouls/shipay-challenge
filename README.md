# Projeto Shipay - Desafio
## Escopo do problema
Foi requisitada a criação de uma API RESTful com no mínimo duas rotas: uma para realizar a procura de uma `role_id` dado um `user_id` e outra para cadastrar um usuário, fornecendo os campos do usuário através do payload da requisição, caso o usuário não fornecesse senha, uma deveria ser criada para ele.

## Algumas ressalvas
Foi adicionada uma rota `/api/v1/role` para fazer a adição de uma `role`, já que para testar a rota de adição de usuário, será necessário uma `role` pré-cadastrada, e também uma rota `/api/v1/roles` para listar as roles cadastradas.

PS: Caso esteja com o serviço do postgresql rodando na sua máquina, é possível que haja conflito de portas, execute `systemctl stop postgresql` para parar temporariamente o serviço. Para reativá-lo, execute `systemctl start postgresql`.

## Executando

### Executando os testes
Para executar todos os testes, a partir do diretório raiz, execute: `docker build -t tests --target tests .`, ou então `poetry run pytest` caso possua o `poetry` instalado localmente (será necessário rodar `poetry install` para instalar as dependências antes).

### Localmente
Entre no diretório raiz do projeto shipay e execute `docker-compose up` e a aplicação estará escutando na porta 5000.

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
