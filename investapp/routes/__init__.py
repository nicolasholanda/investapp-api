from flask import Flask

from investapp.routes import stock_exchange


def init_app(app: Flask):
    """
    Função responsável por inicializar o módulo routes, registrando os blueprints no app.
    :param app: Aplicação Flask principal
    :return:
    """

    app.register_blueprint(stock_exchange.bp)
