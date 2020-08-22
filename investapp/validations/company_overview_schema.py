from marshmallow import Schema, fields, validate


class CompanyOverviewRequestSchema(Schema):
    """
    Classe responsável por validar os parâmetros passados na query de visão geral por empresa
    """

    symbol = fields.Str(required=True, validate=validate.Length(min=1))
