

## Exemplos:

- POST: 

- [x] Inserir Voluntario `curl http://127.0.0.1:8000/voluntario/add -d '{"name":"Raul", "midname": "Silverio", "neighbor": "Jurere", "city": "Florianopolis"}' -H "Content-Type: application/json" -X POST`
- [x] Inserir Acoes `curl http://127.0.0.1:8000/acao/add -d '{"name":"Ambiental", "institution": "IBAMA", "location": "Amazonas", "description": "Organizacao nacional responsavel pela protecao ambiental"}' -H "Content-Type: application/json" -X POST`