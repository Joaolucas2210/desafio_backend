# Desafio Backend OMNI!

API para consulta de filmes, inserção nos favoritos e listagem dos favoritos.


# Como utilizar:
**Utilizando Docker**:

1.  Construa a imagem do Docker:


    **`docker build -t <definir-nome-da-imagem> .`**

2.  Execute o contêiner Docker em segundo plano e mapeie a porta 8080:

    **`docker run -d -p 8080:8080 <nome-pre-definido-anteriormente>`**


**Rodando local:**

1.  Certifique-se de que o arquivo `init.sh` tenha as permissões necessárias para execução:


    `chmod +x init.sh`

2.  Execute o comando `./init.sh` para iniciar a aplicação localmente.

## **Endpoints:**

-   GET /title: Busca um filme por nome e insere os dados em `request_storage.json`.

-   GET /title/string:id: Busca um título por ID dentro do `request_storage.json` e, se existir, insere em `local_storage`.

-   GET /favorites: Retorna uma listagem geral de todos os itens favoritados pelo usuário.

-   GET /favorites/string:title: Retorna o item referente ao ID específico. Se não existir, retorna o erro 404.

## **Bibliotecas utilizadas:**
-   Httpx:
-  A biblioteca Httpx foi adaptada em uma classe e seu método "GET" é utilizado para fazer requisições HTTP.

-   Dynaconf:
- De autoria de Bruno Rocha, esta biblioteca foi adaptada para obter variáveis de ambiente, facilitando a configuração da aplicação.

-   Quart:
-  É um framework similar ao Flask, mas assíncrono, permitindo um melhor desempenho em operações de I/O.

## **Observações:**

-   `request_storage.json`: Tem a responsabilidade de armazenar os dados que vêm da API OMDB.

-   `local_storage.json`: Tem a responsabilidade de armazenar os títulos favoritos selecionados pelo usuário.