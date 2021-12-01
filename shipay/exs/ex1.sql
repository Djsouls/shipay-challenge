-- Primeiro exercício
-- Para evitar a repetição de dados, a melhor opção seria
-- realizar duas consultas, entretanto como o desafio falava
-- sobre realizar uma consulta, optou-se por essa solução.

SELECT
    users.id,
    users.email,
    users.password,
    claims.decription, -- A tabela claims tem a coluna decription e não deScription 
    roles.description
FROM
    users
INNER JOIN user_claims as uc
    ON uc.user_id = users.id
INNER JOIN claims
    ON uc.claim_id = claims.id
INNER JOIN roles
    ON roles.id = users.role_id
WHERE users.id = 1 -- Aqui será o id do usuário o qual você gostaria de buscar

