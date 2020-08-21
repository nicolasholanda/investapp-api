from http.client import TOO_MANY_REQUESTS, OK, BAD_REQUEST
from time import sleep

from flask import Response
from flask.testing import FlaskClient

from investapp.utils.constants import AV_SYMBOL_SEARCH_KEYS

ROUTE_PREFIX = '/stock_exchange'


def test_should_return_company_by_symbol(client: FlaskClient):
    """
    Testa se a API retorna a empresa pelo símbolo.
    :param client: API cliente para testes.
    :return:
    """
    company_symbol = 'XIACF'
    response: Response = search_by_keywords(client, keywords=company_symbol)
    first_result: dict = response.json.get('items')[0]

    assert response.status_code == OK
    assert first_result.get('symbol') == company_symbol
    for key in AV_SYMBOL_SEARCH_KEYS.keys():
        assert first_result.get(key) is not None


def test_should_return_company_by_name(client: FlaskClient):
    """
    Testa se a API retorna a empresa pelo nome.
    :param client: API cliente para testes.
    :return:
    """
    company_name = 'Xiaomi'
    response: Response = search_by_keywords(client, keywords=company_name)
    first_result: dict = response.json.get('items')[0]

    assert response.status_code == OK
    assert company_name in first_result.get('name')
    for key in AV_SYMBOL_SEARCH_KEYS.keys():
        assert first_result.get(key) is not None


def test_should_fail_when_keywords_is_empty(client: FlaskClient):
    """
    Testa se a API retorna um erro quando a palavra-chave está vazia.
    :param client: API cliente para testes.
    :return:
    """
    response: Response = search_by_keywords(client, keywords='')

    assert response.status_code == BAD_REQUEST
    assert 'minimum length' in response.json.get('description')


def test_should_fail_when_keywords_is_missing(client: FlaskClient):
    """
    Testa se a API retorna um erro quando a palavra-chave não é enviada.
    :param client: API cliente para testes.
    :return:
    """
    response: Response = search_by_keywords(client)

    assert response.status_code == BAD_REQUEST
    assert 'Missing data' in response.json.get('description')


def test_should_fail_when_many_requests_are_made(client: FlaskClient):
    """
    Testa se a API retorna um erro quando mais do ques 5 requisições são feitas dentro de 1 minuto.
    :param client: API cliente para testes.
    :return:
    """
    while True:
        response = client.get(f'{ROUTE_PREFIX}/search/', query_string= {'keywords': 'XIACF'})
        if response.status_code != OK:
            break

    assert response.json.get('code') == TOO_MANY_REQUESTS
    assert 'Muitas requisições' in response.json.get('description')


def search_by_keywords(client: FlaskClient, **kwargs) -> Response:
    """
    Retorna a busca de empresas por palavra-chave e garante que o servidor não retorne uma exceção
    do tipo TooManyRequests.
    :param client: API cliente para testes.
    :key keywords: Palavra-chave da busca.
    :return: Objeto Response, contendo a resposta do servidor.
    """
    while True:
        response: Response = client.get(f'{ROUTE_PREFIX}/search/', query_string=kwargs)

        if response.status_code == TOO_MANY_REQUESTS:
            sleep(60)
        else:
            break

    return response
