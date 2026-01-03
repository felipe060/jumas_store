def verify_header(**kwargs):
    content_type = kwargs["content_type"]

    if content_type.strip() == "":
        message = {"error": "missing //content-type// header"}
        return message

    elif content_type != "application/json":
        message = {"error": "//content-type// must be application/json"}
        return message

    elif content_type == "application/json":
        return True


def verifies_user(**kwargs):
    """Verifies if the user and password are correct"""

    print("sidetasks.py verifies_user() being called\n")

    json_data = kwargs["json_data"]                         #receives the json from the app.py and put it into a variable

    json_data_keys = json_data.keys()           #put the json keys on a variable
    lista: list = []
    for item in json_data_keys:                 #put the keys on a list
        lista.append(item)

    len_lista = len(lista)                      #checks the length of the list with json keys

    if len_lista != 2:                                                          #if the list has something different from 2 items, its over pro betinha
        print("o json recebido tem um numero de campos diferente de 2")         #eu so preciso de 2 itens //email// e //senha//
        message: dict = {"error": "the json file received has a number of fields differente from 2"}
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

    try:
        from database_conn import verify_on_database
        result_user_query = verify_on_database(email=email, senha=senha)
        return result_user_query

    except Exception as e:
        print("eita\n"
              "-- love the Lord your God with all your heart and with all you soul and with all your mind")
        print(e)
        return "unknown exception"
