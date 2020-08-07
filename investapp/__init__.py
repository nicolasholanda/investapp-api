import os

from flask import Flask


def create_app(test_config: dict = None):
    """
    Método factory para criar e configurar o app Flask.

    :param test_config: Configurações de testes, para sobreescreverem a configuração normal do app.
    :return: Objeto Flask, que representa a aplicação.
    """

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev'
    )

    # Carregando configuração de teste, caso tenha sido passada como argumento
    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    # Criando a pasta instance do Flask
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/')
    def hello():
        return 'Welcome to Investapp API! Read the docs.'

    return app
