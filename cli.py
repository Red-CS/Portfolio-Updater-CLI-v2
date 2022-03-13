from __future__ import print_function, unicode_literals
from PyInquirer import prompt
from prompts import Read, Add

input = [
    {
        'type': 'list',
        'name': 'action',
        'message': 'What would you like to do?',
        # TODO: 'default': [index]
        'choices': [
            'View the database',
            'Add a project',
            'Edit a project',
            'Remove a project',
            'Exit'
        ]
    }
]

choice = prompt(input)
print(choice)

if 'View' in choice['action']:
    p = Read("/api/projects")
    p.execute()
    # pass

elif 'Add' in choice['action']:
    p = Add()
    p.prompt()
    p.confirm()
elif 'Edit' in  choice['action']:
    pass
elif 'Remove' in choice['action']:
    pass
elif 'Exit' in choice['action']:
    sys.exit(0)
else:
    raise Exception("An error occured while parsing that selection")
    