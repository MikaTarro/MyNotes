import pprint
server_data = {
    "server": {
        "host": "127.0.0.1",
        "port": "10"
    },
    "configuration": {
        "access": "true",
        "login": "Ivan",
        "password": "qwerty"
    }
}


pprint.pprint(server_data, width=10, indent=2)
# { 'configuration': { 'access': 'true',
#                      'login': 'Ivan',
#                      'password': 'qwerty'},
#   'server': { 'host': '127.0.0.1',
#               'port': '10'}}


                                                        # 2й способ
# printer = pprint.PrettyPrinter(width=50, indent=4)
# printer.pprint(server_data)

# {   'configuration': {   'access': 'true',
#                          'login': 'Ivan',
#                          'password': 'qwerty'},
#     'server': {'host': '127.0.0.1', 'port': '10'}}
                                                        # пример!!
data = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "hobbies": ["reading", "playing guitar", "travelling"],
}

printer = pprint.PrettyPrinter(width=50, indent=4)
printer.pprint(data)