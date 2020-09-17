import json
import unittest

from chalice.config import Config
from chalice.local import LocalGateway

from api.app import app


class UnitTests(unittest.TestCase):
    def setUp(self):
        self.lg = LocalGateway(app, Config())

    def test_insert_volunteer(self):
        request = {'body': {'name': 'Raul', 'midname': 'Silverio', 'neighbor': 'Jurere', 'city': 'Florianopolis'}}
        request_body = request['body']
        response = self.lg.handle_request(method='POST',
                                          path='/voluntario/add',
                                          headers={
                                              'Content-Type': 'application/json'
                                          },
                                          body=json.dumps(request_body))

        assert response['statusCode'] == 200

    def test_insert_action(self):
        request = {'body': {"name": "Ambiental", "institution": "IBAMA", "location": "Amazonas",
                            "description": "Organizacao nacional responsavel pela protecao ambiental"}}
        request_body = request['body']
        response = self.lg.handle_request(method='POST',
                                          path='/voluntario/add',
                                          headers={
                                              'Content-Type': 'application/json'
                                          },
                                          body=json.dumps(request_body))

        assert response['statusCode'] == 200
