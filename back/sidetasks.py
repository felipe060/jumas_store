def verify_header(**kwargs):
    """Verifies if the Content-Type is application/json"""
    print("\nsidetasks.py verify_header() being called\n")

    content_type = kwargs["content_type"]       #recebi o content-type atraves do kwargs com type string

    if content_type == "application/json":
        return True

    elif content_type.strip() == "":                                  #verifies if the content-type is indeed in the request
        message = {"error": "missing //content-type// header"}        #if not, returns a json
        return message

    elif content_type != "application/json":                                    #verifies if the header id content-type=application/json
        message = {"error": "//content-type// must be application/json"}        #if not, returns a json
        return message


def verifies_user(**kwargs):
    """Verifies if the user and password are correct"""
    print("\nsidetasks.py verifies_user() being called\n")

    json_data = kwargs["json_data"]             #receives the json from the app.py and put it into a variable
    json_data_keys = json_data.keys()           #put the json keys on a variable

    if len(json_data_keys) != 2:                                                          #if the list has something different from 2 items, its over pro betinha
        print("o json recebido tem um numero de campos diferente de 2\n")        #eu so preciso de 2 itens //email// e //senha//
        message: dict = {"error": "the json file received has a number of fields different from 2"}
        return message

    elif len(json_data_keys) == 2:            #if the json received has exactly 2 items
        for item in json_data_keys:
            if item != "email" and item != "senha":                                     #we check if these items are //email// and //senha//
                print("o json tem algum campo diferente dos campos requeridos\n")         #if not, it1s over pro betinha again
                message: dict = {"error": "the json file received has some field different from the required ones"}
                return message
        print("o json recebido tem exatamente 2 campos\n")

    email = json_data["email"]
    senha = json_data["senha"]

    try:                #se o json tem apenas 2 campos e eles sao //email// e //senha//, ent seguimos com esse try
        from database_conn import verify_on_database
        result_user_query = verify_on_database(email=email, senha=senha)
        return result_user_query

    except Exception as e:          #i dont know what to do when an exception is raised here
        print("eita, surgiu uma Exception\n"
              "-- love the Lord your God with all your heart and with all you soul and with all your mind")
        print(e)
        message: dict = {"error": f"{e}"}
        return message


def adds_user(**kwargs):
    """Tries to add a new user to the database"""
    print("sidetasks.py adds_user() being called\n")

    json_data = kwargs["json_data"]         #i need 3 fields //email// and //senha// and //name//
    json_data_keys = json_data.keys()

    if len(json_data_keys) != 3:        #if i the request has anything different from 3 fields
        print("o json recebido tem um numero de campos diferente de 3\n")
        message: dict = {"error": "the json received has a number of fields different from 3"}
        return message                  #the function returns this message

    elif len(json_data_keys) == 3:      #if we receive 3 fields
        for item in json_data_keys:
            if item != "email" and item != "senha" and item != "name":      #we verify if they are the ones we want
                print("o json recebido tem algum campo diferente dos requeridos\n")
                message: dict = {"error": "the json file received has some field different from the required ones"}
                return message                              #anything different from the 3 fields we want, returns this message
        print("o json recebido tem exatamente 3 campos\n")

    email = json_data["email"]      #just defining the variables with the json received
    senha = json_data["senha"]
    name = json_data["name"]

    from database_conn import add_to_database
    result_user_add = add_to_database(email=email, senha=senha, name=name)
    return result_user_add


def resets_password(**kwargs):
    """Resets the password"""
    print("\nsidetasks.py resets_password() being called\n")

    json_data = kwargs["json_data"]     #i need 2 fields //email// and //new_password//
    json_data_keys = json_data.keys()

    if len(json_data_keys) != 2:        #if we receive a json with something different from 2 fields
        print("o json recebido tem um numero de campos diferente de 2\n")
        message: dict = {"error": "the json received has a number of fields different from 2"}
        return message                  #the function returns this message

    elif len(json_data_keys) == 2:      #if we receive exactly 2 fields
        for item in json_data_keys:
            if item != "email" and item != "new_password":      #we check if they are the required ones
                print("j son recebido tem algum campo diferente dos requeridos\n")
                message: dict = {"error": "the json received has some field different from the required ones"}
                return message                                  #if not, we return this message
        print("o json recebido tem exatamente 2 campos\n")

    email = json_data["email"]                  #just defining the variables
    new_password = json_data["new_password"]

    from database_conn import reset_password_on_database
    result_alter_on_database = reset_password_on_database(email=email, new_password=new_password)
    return result_alter_on_database


def generates_code():
    """Just generates a random integer number between zero and 999.999"""
    print("\nsidetasks.py generates_code() being called\n")

    from random import randint
    numero = randint(0, 999_999)
    return numero


def sends_email(email_user: str, code: int):
    """Tries to send an email to the user"""
    print("\nsidetasks.py sends_email() being called\n")

    from dotenv import find_dotenv, load_dotenv     #the function needs 2 fields //email_user// and //code//
    from os import environ
    import resend

    dotenv_path = find_dotenv()
    load_dotenv(dotenv_path)

    resend.api_key = environ.get("RESEND_API_KEY")
    email_remetente = environ.get("RESEND_EMAIL")

    print("email_user --> ", email_user)

    try:
        r = resend.Emails.send({            #trynna send the email
            "from": email_remetente,
            "to": email_user,
            "subject": "Code",
            "html": f"<p>your code --> <strong>{code}</strong></p>"
        })
        print("email sent successfully\n")
        message: dict = {"success": "email was sent"}   #if the email is sent
        return True          #the function returns True
    except Exception as e:
        print("Deu ruim aq. Exception right bellow\n")  #if some Exception is raised
        print(e)
        message: dict = {"error": f"{e}"}
        return False      #return False


def resets_password_verify_email(**kwargs):
    print("\nsidetasks.py resets_password_verify_email() being called\n")

    json_data = kwargs["json_data"]         #this function receives 1 argument --> email
    json_data_keys = json_data.keys()

    if len(json_data_keys) != 1:                #if the function receives something differente from 1 argument
        print("o json recebido tem um numero de campos diferente de 1\n")
        message: dict = {"error": "the json received has a number of fields different from 1"}
        return message          #returns this message

    elif len(json_data_keys) == 1:          #if the function receives 1 argumento
        for item in json_data_keys:         #we check if it is //email//
            if item != "email":
                print("o campo recebido no json é diferente do campo requerido\n")
                message: dict = {"error": "the json received has a field different from the required one"}
                return message              #if not, return this message
        print("o json recebido tem exatamente 1 campo\n")

    email = json_data["email"]      #put the email received on a variable
    counter = 0                     #define the counter to the while loop
    print("counter --> ", counter)

    while counter < 6:
        codigo = generates_code()   #gera um numero aleatorio 6 digits from zero till 999_999

        session_code = str(codigo) + "_" + email        #cria o sessioncode com codigo + emai

        from database_conn import write_sessioncode_on_database
        result_sessioncode = write_sessioncode_on_database(session_code=session_code, email=email)  #tenta escrever o sessioncode no database

        if result_sessioncode[0]:       #caso consiga escrever o sessioncode no database
            response_email = sends_email(email_user=email, code=codigo)     #try to send an email to the user

            if response_email:                                              #if the email was sent
                message: dict = {"response": "email was sent successfully"}
                return message                                              #returns this message
            elif not response_email:                                                        #if the email wasnt sent
                print("response_email --> ", response_email)
                message: dict = {"error": "some error occurred on our server, try again"}
                return message                                                              #returns this message
            break               #and stops the loop

        elif not result_sessioncode[0]:     #in case sessioncode isnt written down on database

            if result_sessioncode[1]["error"] == "this sessioncode is already written on database":     #if this is the reason
                print("o sessioncode gerado ja existe no database, estou gerando outro\n")
                counter += 1                        #adds 1 number to the counter
                continue                            #continues the loop, heading to generate other code and trying to send another email

            elif result_sessioncode[1]["error"] == "this email isnt on our database":       #if this is the reason
                print("esse email n ta escrito no database\n")
                message: dict = {"response": "this email isnt written on our database"}
                return message                                                              #returns this message


def verifies_code_password(**kwargs):
    """Verifies if the code received mathces with the code on database"""
    print("\nsidetasks.py verifies_code_password() being called\n")     #needs 2 fields --> code / email

    json_data = kwargs["json_data"]         #just defining json_data
    json_data_keys = json_data.keys()       #putting the keys on a variable

    if len(json_data_keys) != 2:                #if the json received has something differente from 2 fields
        print("o json recebido tem um numero de campos diferente de 2\n")
        message: dict = {"error": "the json received has a number of fields different from 3"}
        return message          #the function returns this message

    elif len(json_data_keys) == 2:      #if we receive exactly 2 fields
        for item in json_data_keys:
            if item != "code" and item != "email":      #verify if they are the fields we want
                print("o json recebido tem algum campo diferente dos requeridos\n")
                message: dict = {"error": "the json received has some field different from the required ones"}
                return message                              #if not, return this message
        print("o json recebdio tem exatamente 2 campos")

    code = json_data["code"]        #just defining the variables
    email = json_data["email"]

    session_code = str(code) + "_" + email       #making the sessioncode to verify

    from database_conn import lookfor_sessioncode_on_database
    result_query = lookfor_sessioncode_on_database(received_sessioncode=session_code)
    print("seila result_query() --> ", result_query)
    return result_query[1]

