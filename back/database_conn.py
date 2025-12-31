from conn import Session, User, SessionCode, Address, Product, ProductVariant, Order, OrderItem


def verify_on_database(email: str, senha: str):
    """Verifies if the user and password are correct by connecting to the database"""

    print("database_conn.py verify_on_database() being called")

    with Session() as session:
        try:
            consulta = session.query(User.user_email, User.user_senha).where(User.user_email == email).first()
            if consulta is None:
                print("o email recebido n foi encontrado no database\n")
                return False
        except Exception as e:
            print("houve uma exception inesperada\n"
                  "exception abaixo\n")
            print(e)
            return False

    email_on_database = consulta.user_email
    senha_on_database = consulta.user_senha

    if email == email_on_database and senha == senha_on_database:
        print("email e senha iguais aos do database\n")
        return True
    elif email != email_on_database or senha != senha_on_database:
        print("email ou senha diferente do cadastrado no database\n")
        return False


#verify_on_database(email="celso@hotmail.com", senha="celso_senha")
