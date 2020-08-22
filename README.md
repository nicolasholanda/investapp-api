# Documentação
A documentação descreve todos os endpoints disponibilizados na API e pode ser acessada através deste [link](https://app.swaggerhub.com/apis-docs/nicolasholanda/investapp-api/1.0.0).

# Descrição
Investapp API se trata do backend da aplicação Investapp. A aplicação tem por objetivo comunicar-se com a API da 
Alpha Vantage, para buscar dados reais de valores de ações de empresas, bem como os valores da Bovespa e disponibilizar os
dados para que sejam consumidos através de uma aplicação cliente em VueJS. O projeto faz parte do desafio da seleção da
empresa PontoTel.

# Tecnologias utilizadas
- Python 3.7
- Flask
- Requests
- Marshmallow
- Pytest
- Coverage

# Rodando a aplicação
- Linux
```
$ pip install virtualenv
$ virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ export FLASK_APP=__init__.py
$ flask run
```

- Windows
```
C:\path\to\investapp>virtualenv venv
C:\path\to\investapp>venv/Scripts/activate
C:\path\to\investapp>pip install -r requirements.txt
C:\path\to\investapp>set FLASK_APP=__init__.py
C:\path\to\investapp>flask run
```

# Testes

```
$ coverage run -m pytest
```