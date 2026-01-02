import sqlalchemy.exc
from conn import Session, User, SessionCode, Address, Product, ProductVariant, Order, OrderItem


def verify_on_database(email: str, senha: str):
    """Verifies if the user and password are correct by connecting to the database"""

    print("database_conn.py verify_on_database() being called\n")

    with Session() as session:
        try:
            consulta = session.query(User.user_email, User.user_senha).where(User.user_email == email).first()
            if consulta is None:
                print("email received was not found on database\n")
                return False
        except Exception as e:
            print("houve uma exception inesperada\n"
                  "exception right bellow\n")
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


def add_to_database(email: str, senha: str, name: str):
    print("database_conn.py add_to_database() being called\n")

    with Session() as session:
        import sqlalchemy

        new_user = User(user_email=email, user_senha=senha, name=name)
        session.add(new_user)

        try:
            session.commit()
            print("user cadastrado c sucesso\n")
            message: dict = {"response": "user added successfully"}
            return message

        except sqlalchemy.exc.IntegrityError as e:
            error = str(e).split()[0]
            print("-->", error)

            if error == "(psycopg2.errors.UniqueViolation)":
                print("esse email ja existe\n")
                message: dict = {"response": "this email already exists on database"}
                return message

            elif error == "(psycopg2.errors.NotNullViolation)":
                print("faltando alguma coluna")
                print("n era pra acontecer este error\n")
                message: dict = {"error": "some column is missing on the commit to the database"}
                return message

        except Exception as e:
            print("some unknown Exception occurred\n")
            message: dict = {"error": "some interanl error occurred // try again"}
            return message


def reset_password_on_database(email: str, new_password: str):
    print("database_conn.py reset_password_on_database() being called\n")

    with Session() as session:

        from sqlalchemy import update

        user = session.query(User).where(User.user_email == email).first()
        if user is None:
            print("email received was not found on database\n")
            return False

        consulta = update(User).where(User.user_email == email).values(user_senha=new_password)
        session.execute(consulta)

        try:
            session.commit()
            print("senha alterada c sucesso\n")
            message: dict = {"response": "password changed successfully"}
            return message

        except Exception as e:
            print("some Exception was raised\n"
                  "Exception bellow\n")
            print(e)
            message: dict = {"error": "some error have occurred on our server, try to change the password again"}
            return message


def write_sessioncode_on_database(session_code: str, email: str):
    print("database_conn.py write_sessioncode_on_database() being called\n")

    with Session() as session:
        consulta = session.query(User).where(User.user_email == email).first()
        if consulta is None:
            print("this email isnt written on the database\n")
            message: dict = {"error": "this email isnt on our database"}
            return message
        id_usuario = consulta.user_id

    write_sessioncode = SessionCode(sessioncode=session_code, user_id=id_usuario)
    session.add(write_sessioncode)

    import sqlalchemy

    try:
        session.commit()
        print("sessioncode escrito no database\n")
        message: dict = {"response": "sessioncode writtend down on database"}
        return True, message
    except sqlalchemy.exc.IntegrityError as e:
        print("acho q esse sessioncode ja existe no dataabase\n"
              "Exception abaixo\n")
        print(e)
        message: dict = {"error": "this sessioncode is already written on database"}
        return False, message
    except sqlalchemy.exc.OperationalError as e:
        print("acho q foi error de conexao com o database\n")
        print("error -->", e)                                                           #im returning the same error as above to facilitate the handling
        message: dict = {"error": "this sessioncode is already written on database"}    #but this error, i think is like the error on the line right bellow
        return False, message                                                           #sqlalchemy.exc.OperationalError: (psycopg2.OperationalError) SSL connection has been closed unexpectedly


def lookfor_sessioncode_on_database(received_sessioncode: str):
    print("databaase_conn.py lookfor_sessioncode_on_database() being called\n")

    print(received_sessioncode)

    with Session() as session:
        # colocar um try aq
        look_sessioncode = session.query(SessionCode).where(SessionCode.sessioncode == received_sessioncode).first()
        if look_sessioncode is None:
            print("o sessioncode recebido n tem no database")
            return False

        print("look_sessioncode -->", look_sessioncode)
        print("look_sessioncode type -->", type(look_sessioncode))
        print("look_sessioncode.sessioncode -->", look_sessioncode.sessioncode)

        if look_sessioncode.sessioncode == received_sessioncode:
            print("o sessioncode recebido corresponde no dtabase\n")
            return True


lookfor_sessioncode_on_database(received_sessioncode="this the session code")
