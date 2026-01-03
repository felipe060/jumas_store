def verify_header(**kwargs):
    content_type = kwargs["content_type"]       #recebi o content-type atraves do kwargs com type string

    if content_type.strip() == "":                                  #verifies if the content-type is indeed in the request
        message = {"error": "missing //content-type// header"}      #if not, returns a json
        return message

    elif content_type != "application/json":                                    #verifies if the header id content-type=application/json
        message = {"error": "//content-type// must be application/json"}        #if not, return a json
        return message

    elif content_type == "application/json":
        return True


def verifies_user(**kwargs):
    """Verifies if the user and password are correct"""

    print("sidetasks.py verifies_user() being called\n")

    json_data = kwargs["json_data"]             #receives the json from the app.py and put it into a variable

    json_data_keys = json_data.keys()           #put the json keys on a variable
    lista: list = []
    for item in json_data_keys:                 #put the keys on a list
        lista.append(item)

    len_lista = len(lista)                      #checks the length of the list with json keys

    if len_lista != 2:                                                          #if the list has something different from 2 items, its over pro betinha
        print("o json recebido tem um numero de campos diferente de 2\n")       #eu so preciso de 2 itens //email// e //senha//
        message: dict = {"error": "the json file received has a number of fields different from 2"}
        return message

    elif len_lista == 2:            #if the json received has exactly 2 items
        for item in lista:
            if item != "email" and item != "senha":                                     #we check if these items are //email// and //senha//
                print("o json tem algum campo diferente dos campos requeridos")         #if not, it1s over pro betinha again
                message: dict = {"error": "the json file received has some field different from the required ones"}
                return message

        print("o json recebido tem exatamente 2 campos")

    email = json_data["email"]
    senha = json_data["senha"]

    try:                #se o json tem apenas 2 campos e eles sao //email// e //senha//, ent seguimos com esse try
        from database_conn import verify_on_database
        result_user_query = verify_on_database(email=email, senha=senha)
        return result_user_query

    except Exception as e:
        print("eita, surgiu uma Exception\n"
              "-- love the Lord your God with all your heart and with all you soul and with all your mind")
        print(e)
        return "unknown exception"


def adds_user(**kwargs):
    print("sidetasks.py adds_user() being called\n")
    json_data = kwargs["json_data"]

    json_data_keys = json_data.keys()
    lista: list = []

    for item in json_data_keys:
        lista.append(item)

    len_lista = len(lista)

    if len_lista != 3:
        print("o json recebido tem um numero de campos diferente de 3\n")
        message: dict = {"error": "the json received has a number of fields different from 3"}
        return message

    elif len_lista == 3:
        for item in lista:
            if item != "email" and item != "senha" and item != "name":
                print("o json recebido tetm algum campo diferente dos requeridos\n")
                message: dict = {"error": "the json file received has some field different from the required ones"}
                return message
        print("o json recebido tem exatamente 2 campos\n")

    email = json_data["email"]
    senha = json_data["senha"]
    name = json_data["name"]

    from database_conn import add_to_database
    result_user_add = add_to_database(email=email, senha=senha, name=name)
    return result_user_add


def resets_password(**kwargs):
    print("sidetasks.py resets_password() being called\n")

    json_data = kwargs["json_data"]

    json_data_keys = json_data.keys()
    lista: list = []

    for item in json_data_keys:
        lista.append(item)

    len_lista = len(lista)

    if len_lista != 2:
        print("o json recebido tem um numero de campos diferente de 2\n")
        message: dict = {"error": "the json received has a number of fields different from 2"}
        return message

    elif len_lista == 2:
        for item in lista:
            if item != "email" and item != "new_password":
                print("j son recebido tem algum campo diferente dos requeridos\n")
                message: dict = {"error": "the json received has some field different from the required ones"}
                return message
        print("o json recebido tem exatamente 2 campos\n")

    email = json_data["email"]
    new_password = json_data["new_password"]

    from database_conn import reset_password_on_database
    result_alter_on_database = reset_password_on_database(email=email, new_password=new_password)
    return result_alter_on_database


def resets_password_verify_email(**kwargs):
    print("sidetasks.py resets_password_verify_email() being called\n")

    json_data = kwargs["json_data"]

    json_data_keys = json_data.keys()
    lista: list = []

    for item in json_data_keys:
        lista.append(item)

    len_lista = len(lista)

    if len_lista != 2:
        print("o jjson recebido tem um numero de campos diferente de 2\n")
        message: dict = {"error": "the json received has a numebrrr of fields different from 2"}
        return message

    elif len_lista == 2:
        for item in lista:
            if item != "email" and item != "session_id":
                print("o json tem algum campo diferente dos requeridos\n")
                message: dict = {"error": "the json received has som field different from the required ones"}
                return message
        print("o json recebido tem exatamente 2 campos\n")

    email = json_data["email"]
    session_id = json_data["session_id"]

    counter = 0

    while counter < 11:
        codigo = generates_code()

        session_code = str(codigo) + "_" + email + "_" + session_id
        print("session_code -->", session_code)
        print("session_code type -->", type(session_code))

        from database_conn import write_sessioncode_on_database
        result_sessioncode = write_sessioncode_on_database(session_code=session_code, email=email)
        print("result_sessioncode --> ", result_sessioncode, "\n")

        if result_sessioncode[0]:
            response_email = sends_email(email_user=email, code=codigo)

            if response_email:
                message: dict = {"response": "email was sent successfully"}
                return message
            elif response_email == False:
                message: dict = {"error": "some error occurred on oyr sercer, try again"}
                return message
            break








def generates_code():
    print("sidetasks.py generates_code() being called\n")

    from random import randint
    numero = randint(0, 999_999)
    return numero


def sends_email(email_user: str, code: int):
    print("sidetasks.py sends_email() being called\n")

    import smtplib
    from email.message import EmailMessage

    email_remetente = "santuario.olinda@gmail.com"
    senha_remetente = "neln zrec tobo djqn"

    host_smtp = "smtp.gmail.com"
    porta = 587

    message = EmailMessage()
    message["Subject"] = "Reseting password"
    message["From"] = email_remetente
    message["To"] = email_user

    mensagem = f"""{code}\nthats your code, bro"""

    message.set_content(mensagem)

    try:
        with smtplib.SMTP(host=host_smtp, port=porta) as server:
            server.starttls()
            server.login(email_remetente, senha_remetente)
            server.send_message(message)
            print("email sent successfully\n")
            message: dict = {"success": "email was sent"}
            return True
    except Exception as e:
        print("Deu ruim aq. Exception right bellow\n")
        print(e)
        message: dict = {"error": "some internal error have occurred"}
        return False

