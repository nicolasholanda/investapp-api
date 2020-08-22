from http.client import TOO_MANY_REQUESTS, OK, BAD_REQUEST
from time import sleep

from flask import Response
from flask.testing import FlaskClient

from investapp.utils.constants import AV_OVERVIEW_KEYS

ROUTE_PREFIX = '/stock_exchange'


def test_should_return_company_overview_by_symbol(client: FlaskClient):
    """
    Testa se a API retorna a visão geral da empresa pelo símbolo.
    :param client: API cliente para testes.
    :return:
    """
    company_symbol = 'IBM'
    response: Response = get_company_overview(client, symbol=company_symbol)

    assert response.status_code == OK
    assert company_symbol in response.json.get('symbol')
    for key in AV_OVERVIEW_KEYS.keys():
        assert response.json.get(key) is not None


def test_should_fail_when_keywords_is_empty(client: FlaskClient):
    """
    Testa se a API retorna um erro quando o símbolo está vazio.
    :param client: API cliente para testes.
    :return:
    """
    response: Response = get_company_overview(client, symbol='')

    assert response.status_code == BAD_REQUEST
    assert 'minimum length' in response.json.get('description')


def test_should_fail_when_symbol_is_missing(client: FlaskClient):
    """
    Testa se a API retorna um erro quando o símbolo não é enviado.
    :param client: API cliente para testes.
    :return:
    """
    response: Response = get_company_overview(client)

    assert response.status_code == BAD_REQUEST
    assert 'Missing data' in response.json.get('description')


def test_should_fail_when_many_requests_are_made(client: FlaskClient):
    """
    Testa se a API retorna um erro quando mais do ques 5 requisições são feitas dentro de 1 minuto.
    :param client: API cliente para testes.
    :return:
    """
    while True:
        response = client.get(f'{ROUTE_PREFIX}/overview/', query_string={'symbol': 'IBM'})
        if response.status_code != OK:
            break

    assert response.json.get('code') == TOO_MANY_REQUESTS
    assert 'Muitas requisições' in response.json.get('description')


def get_company_overview(client: FlaskClient, **kwargs) -> Response:
    """
    Retorna a visão geral por empresa e garante que o servidor não retorne uma exceção
    do tipo TooManyRequests.
    :param client: API cliente para testes.
    :key symbol: Símbolo da empresa.
    :return: Objeto Response, contendo a resposta do servidor.
    """
    while True:
        response: Response = client.get(f'{ROUTE_PREFIX}/overview/', query_string=kwargs)

        if response.status_code == TOO_MANY_REQUESTS:
            sleep(60)
        else:
            break

    return response
