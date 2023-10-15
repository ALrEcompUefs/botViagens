# botViagens

Répositorio para o projeto do web crwaler e bot no twiter

## Requisitos

* Python 3.11
* BeautifulSoup
* Requests
* Json
* pymongo
* python-dotenv

## Como executar

* Para rodar o projeto execute o arquivo main
* O programa vai executar o web crawler e exibir no terminal a saida com os dados extraidos.
* Após executar o crawler o programa faz inserção no banco de dados e exibe no terminal os resultados

## MongoDb

Para o projeto é utilizado o mongoDb como banco de dados

* Trabalhamos com uma unica coleção ***viagens***
* Para acessar o banco de dados o arquivo .env deve ser configurado com as credenciais para o acesso ao banco de dados.

Para acessar o banco de dados é implementada a classe ***Database** *no arquivo database.py que possui os seguintes métodos

* connect: conecta-se ao banco de dados se possivel e retorna a coleção  ***viagens*** ou lança a exceção que ocorreu
* close: fecha a conexão com o banco de dados
* dB_insert_viagens: recebe uma lista com viagens e insere no banco as que não existem ou informa erros caso ocorram
* dB_find_by_id: faz a busca de uma viagem pelo o id e a retorna caso encontre ou informa que não existe
* dB_find_by_titulo: faz a busca de uma viagem pelo o titulo e a retorna caso encontre ou informa que não existe
* dB_find_by_ano: faz a busca de uma viagem pelo o ano e a retorna caso encontre ou informa que não existe

A coleção ***viagens***  é estruturada do seguinte modo:

```
{
viagens[
	{
		'id'
		'titulo'
		'pontifice'
		'ano'
		'destino'
		'url'
	}
}
```
