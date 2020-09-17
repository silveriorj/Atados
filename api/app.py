import json
from chalice import Chalice, Response, CORSConfig
try:
    from api.chalicelib import database
except ModuleNotFoundError:
    from chalicelib import database

app = Chalice(app_name='api')

request_headers = {'Content-Type': 'application/json'}

cors_config = CORSConfig(
    allow_origin='*'
)


@app.route('/', methods=['POST'], content_types=['application/json'], cors=cors_config)
def index():
    return {'hello': 'world'}


@app.route('/voluntario/add', methods=['POST'], content_types=['application/json'], cors=cors_config)
def add_volunteer():
    request = app.current_request
    body = request.json_body
    flag = database.insert_volunteer(body)
    if flag:
        return Response(
            status_code=200,
            body={
                'message': f'Voluntario \"{body["name"]} {body["midname"]}\" inserido com sucesso!'
            }
        )
    return Response(
            status_code=400,
            body={
                'message': f'Nao foi possivel inserir o usuario no sistema!\n'
                           f'Verifique se as informacoes foram passadas corretamente'
            }
        )


@app.route('/acao/add', methods=['POST'], content_types=['application/json'], cors=cors_config)
def add_action():
    request = app.current_request
    body = request.json_body
    flag = database.insert_actions(body)
    if flag:
        return Response(
            status_code=200,
            body={
                'message': f'Acao \"{body["name"]} - {body["institution"]}\" inserida com sucesso!'
            }
        )
    return Response(
        status_code=400,
        body={
            'message': f'Nao foi possivel inserir a acao no sistema!\n'
                       f'Verifique se as informacoes foram passadas corretamente'
        }
    )
