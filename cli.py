from __future__ import print_function, unicode_literals
from PyInquirer import prompt
from prompts import View, Add, Update
from rich.pretty import pprint as print


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
            {'name':'Exit', 'value': 'e'}
        ]
    }
]

choice = prompt(input)

if choice['action'] == 'v':
    p = View()
    response = p.execute()
    print(response, expand_all=True)

elif choice['action'] == 'a':
    p = Add()
    p.prompt()
    p.confirm()
    # TODO

elif choice['action'] == 'u':
    p = Update()
    p.prompt()
    p.confirm()
    # TODO
    
elif choice['action'] == 'r':
    pass
elif choice['action'] == 'e':
    sys.exit(0)
else:
    raise Exception("An error occured while parsing that selection")
    sys.exit(1)
    