from marshmallow import Schema, fields, validate

from investapp.utils import constants


class TimeSeriesRequestSchema(Schema):
    """
    Classe responsável por validar os parâmetros passados na query da requisição de séries temporais por
    empresa.
    """

    symbol = fields.Str()
    interval = fields.Str(validate=validate.OneOf(list(constants.IA_INTERVAL.keys())), required=True)
