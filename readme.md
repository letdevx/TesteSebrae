# Teste Dev Python SEBRAE

## 📚 Introdução
Este projeto disponibiliza uma aplicação capaz de:
- realizar o download de um arquivo zip à partir do site do INEP contendo uma planilha com as Taxas de Transição Escolar por Município e Dependência Administrativa;
- descompactar o arquivo baixado;
- realizar a leitura e interpretação da planilha;
- persistir os dados em um banco NoSQL (MongoDB);
- consultar dados de uma cidade específica (ex.: Ariquemes);
- gerar uma planilha contendo os dados de Taxa de Transição para Ariquemes contendo um gráfico de barras;

## 🔧 Primeiros Passos
Para poder rodar a aplicação, se faz necessário instalar as dependências. Elas podem ser instaladas executando o seguinte comando:

```bash
pip install -r requirements.txt
```

Obs.: recomenda-se criar um [ambiente virtual](https://docs.python.org/pt-br/3/library/venv.html) antes de realizar a instalação.

### Configuração
Para facilitar a configuração da aplicação, como trocar a url do arquivo a ser baixado ou mesmo a *connection string* do banco, foi criado um arquivo `config.ini` contendo essas e outras opções.

### Banco de Dados
Como banco de dados, foi escolhido o MongoDB. Para evitar a necessidade de provisionar um banco de dados na nuvem ou realizar a instalação do mesmo localmente, foi feito um arquivo `docker-compose.yml` para subir o MongoDB em um container já com o Mongo-Express para realizar consultas.

Antes de iniciar a aplicação, se faz necessário subir os containers, pois a aplicação já se encontra previamente configurada para fazer uso deles. Para subir os containers, basta executar o seguinte comando (desde que o [docker](https://www.docker.com) esteja instalado):

```bash
docker compose up -d
```

Caso queira acessar o Mongo Express o `usuário` e `senha` são `admin` e `admin` respectivamente.

### Execução
Para rodar a aplicação, basta executar o arquivo `main.py`. Por comodidade, foi adicionado no repositório um arquivo `launch.json` para uso com o Visual Studio Code.