from conn import Session, User, SessionCode, Address, Product, ProductVariant, Order, OrderItem


def verify_on_database(email: str, senha: str):
    """Verifies if the user and password are correct by connecting to the database"""
    print("database_conn.py verify_on_database() being called\n")

    with Session() as session:
        try:
            consulta = session.query(User.user_email, User.user_senha).where(User.user_email == email).first()
            if consulta is None:
                print("email received was not found on database\n")
                message: dict = {"error": "email received was not found on database"}
                return message
        except Exception as e:
            print("houve uma exception inesperada\n"
                  "exception right bellow\n")
            print(e)
            message: dict = {"error": f"{e}"}
            return message

    email_on_database = consulta.user_email
    senha_on_database = consulta.user_senha

    if email == email_on_database and senha == senha_on_database:
        print("email e senha iguais aos do database\n")
        #message: dict = {"response": "email and senha match with those in the database"}
        message: dict = {"response": True}
        return message
    elif email != email_on_database or senha != senha_on_database:
        print("email ou senha diferente do cadastrado no database\n")
        #message: dict = {"error": "email or senha different from the ones in the database"}
        message: dict = {"response": False}
        return message


def add_to_database(email: str, senha: str, name: str):
    """Tries to write down the user received to the database"""
    print("\ndatabase_conn.py add_to_database() being called\n")

    with Session() as session:      #using the Session from conn.py
        import sqlalchemy.exc

        new_user = User(user_email=email, user_senha=senha, name=name)      #we define the user to be added with User from conn.py
        session.add(new_user)

        try:
            session.commit()                        #and try to commit him
            print("user cadastrado c sucesso\n")
            #message: dict = {"response": "user added successfully"}
            message: dict = {"response": True}
            return message      #returns this message if everything goes all alright

        except sqlalchemy.exc.IntegrityError as e:      #if this Exception is raised
            error = str(e).split()[0]                   #we put the Exception into a variable

            if error == "(psycopg2.errors.UniqueViolation)":        #and check the variable to respond the request the better way
                print("esse email ja existe\n")
                message: dict = {"response": "this email already exists on database"}
                return message
            elif error == "(psycopg2.errors.NotNullViolation)":
                print("faltando alguma coluna")
                print("n era pra acontecer este error\n")
                message: dict = {"error": "some column is missing on the commit to the database"}
                return message

        except Exception as e:
            print("some unknown Exception occurred\n"
                  "Exception bellow"
                  f"{e}\n")
            message: dict = {"error": f"{e}"}
            return message


def reset_password_on_database(email: str, new_password: str):
    """Tries to change the password directly into the database"""
    print("\ndatabase_conn.py reset_password_on_database() being called\n")

    with Session() as session:
        from sqlalchemy import update

        user = session.query(User).where(User.user_email == email).first()  #checking if the email received exists in the database
        if user is None:                                                    #if the email isnt written in the database
            print("email received was not found on database\n")
            message: dict = {"error": "email received was not found on database"}
            return message                                                  #we return this message

        mudar_senha = update(User).where(User.user_email == email).values(user_senha=new_password)     #if the email exists
        session.execute(mudar_senha)            #we write the sql query to change the password

        try:
            session.commit()                    #and try to commit it
            print("senha alterada c sucesso\n")
            #message: dict = {"response": "password changed successfully"}   #if it is successful
            message: dict = {"response": True}   #if it is successful
            return message                                                  #the function returns this message

        except Exception as e:                      #if some Exception is raised
            print("some Exception was raised\n"
                  "Exception bellow\n")
            print(e)
            message: dict = {"error": f"{e}"}
            return message                  #the function returns this message


def write_sessioncode_on_database(session_code: str, email: str):
    print("\ndatabase_conn.py write_sessioncode_on_database() being called\n")

    with Session() as session:
        consulta = session.query(User).where(User.user_email == email).first()
        if consulta is None:
            print("this email isnt written on the database\n")
            message: dict = {"error": "this email isnt on our database"}
            return False, message
        id_usuario = consulta.user_id

    write_sessioncode = SessionCode(sessioncode=session_code, user_id=id_usuario)
    session.add(write_sessioncode)

    import sqlalchemy.exc

    try:
        session.commit()
        print("sessioncode escrito no database\n")
        message: dict = {"response": "sessioncode written down on database"}
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


def write_sessioncode_on_database_2(session_code: str):
    print("\ndatabase_conn.py write_sessioncode_on_database() being called\n")

    print("seila sessioncode --> ", session_code)
    session = Session()
    write_sessioncode = SessionCode(sessioncode=session_code)
    session.add(write_sessioncode)

    import sqlalchemy.exc

    try:
        session.commit()
        print("sessioncode escrito no database\n")
        message: dict = {"response": "sessioncode written down on database"}
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
        return False, message


def lookfor_sessioncode_on_database(received_sessioncode: str):
    print("\ndatabase_conn.py lookfor_sessioncode_on_database() being called\n")    #need just 1 argumento --> received_sessioncode

    with Session() as session:      #Session imported from conn.py
        try:
            look_sessioncode = session.query(SessionCode).where(SessionCode.sessioncode == received_sessioncode).first()
        except Exception as e:
            print("deu ruim aq, some Exception raised\n"
                  "Exception bellow\n")
            print(e)
            message: dict = {"error": f"{e}"}
            return False, message

        if look_sessioncode is None:
            print("o sessioncode recebido n tem no database\n")
            message: dict = {"error": "the sessioncode received dont exist in the database"}
            #message: dict = {"response": False}
            return False, message

        if look_sessioncode.sessioncode == received_sessioncode:
            print("o sessioncode recebido corresponde no database\n")
            #message: dict = {"response": "the sessioncode received corresponds to the written on database"}
            message: dict = {"response": True}
            return True, message
        elif look_sessioncode.sessioncode != received_sessioncode:
            print("o sessioncode recebido n corresponde ao escrito no database\n")
            message: dict = {"error": "the sessioncode received didnt match on database"}
            #message: dict = {"error": False}
            return False, message
