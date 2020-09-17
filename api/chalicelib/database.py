import sqlite3


def iniciar_db():
    conn = sqlite3.connect('./db/atados.db')
    cursor = conn.cursor()
    try:
        # criando a tabela (schema)
        cursor.execute(
            f'CREATE TABLE voluntarios ( '
            f'id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, '
            f'nome TEXT NOT NULL, '
            f'sobrenome TEXT NOT NULL, '
            f'bairro TEXT NOT NULL, '
            f'cidade TEXT NOT NULL);'
        )
        # criando a tabela (schema)
        cursor.execute(
            f'CREATE TABLE acoes ( '
            f'id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, '
            f'nome TEXT NOT NULL, '
            f'instituicao TEXT NOT NULL, '
            f'local TEXT NOT NULL, '
            f'descricao TEXT NOT NULL);'
        )
    except sqlite3.OperationalError:
        print('tables already exists')
    # desconectando...
    conn.close()


def connect():
    conn = sqlite3.connect('./db/atados.db')
    cursor = conn.cursor()
    return cursor, conn


def insert_volunteer(body):
    p_name = body.get('name')
    p_sname = body.get('midname')
    p_neighbor = body.get('neighbor')
    p_city = body.get('city')

    try:
        cursor, conn = connect()
        cursor.execute("""
                        INSERT INTO voluntarios (nome, sobrenome, bairro, cidade)
                        VALUES (?,?,?,?)
                        """, (p_name, p_sname, p_neighbor, p_city)
                       )
        conn.commit()
        return True
    except (sqlite3.OperationalError, sqlite3.IntegrityError):
        pass
    return None


def insert_actions(body):
    p_name = body.get('name')
    p_institution = body.get('institution')
    p_location = body.get('location')
    p_description = body.get('description')

    try:
        cursor, conn = connect()
        cursor.execute("""
                        INSERT INTO acoes (nome, instituicao, local, descricao)
                        VALUES (?,?,?,?)
                        """, (p_name, p_institution, p_location, p_description)
                       )
        conn.commit()
        return True
    except (sqlite3.OperationalError, sqlite3.IntegrityError):
        pass
    return None

iniciar_db()