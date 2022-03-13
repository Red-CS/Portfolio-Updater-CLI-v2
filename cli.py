from __future__ import print_function, unicode_literals
from PyInquirer import prompt
from prompts import Read, Add, Update
from pprint import pprint

input = [
    {
        'type': 'list',
        'name': 'action',
        'message': 'What would you like to do?',
        # TODO: 'default': [index]
        'choices': [
            {'name':'View the database', 'value': 'v'},
            {'name':'Add a project', 'value': 'a'},
            {'name':'Update a project', 'value': 'u'},
            {'name':'Remove a project', 'value': 'r'},
            {'name':'Exit', 'value': 'a'}
        ]
    }
]

choice = prompt(input)
print(choice)

if choice['action'] == 'v':
    p = Read()
    response = p.execute()
    pprint(response)

elif choice['action'] == 'a':
    p = Add()
    p.prompt()
    p.confirm()

elif choice['action'] == 'u':
    p = Update()
    p.prompt()
    p.confirm()
    
elif choice['action'] == 'r':
    pass
elif choice['action'] == 'e':
    sys.exit(0)
else:
    raise Exception("An error occured while parsing that selection")
    sys.exit(1)
    