server_data = {"server":
                   {"host": "127.0.0.1",
                    "port": "10"
                    },
               "configuration":
                   {"access": "true",
                    "login": "Ivan",
                    "password": "qwerty"
                    }
               }

for key_1, val_1 in server_data.items():
    print(f'\n{key_1}:')
    for key_2, val_2 in val_1.items():
        print(f'\t {key_2}: {val_2}')
