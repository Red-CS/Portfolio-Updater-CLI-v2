from __future__ import print_function, unicode_literals
from PyInquirer import prompt

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

if 'View' in choice.action:
    pass
elif 'Add' in choice.action:
    pass
elif 'Edit' in choice.action:
    pass
elif 'Remove' in choice.action:
    pass
elif 'Exit' in choice.action:
    sys.exit(0)
else:
    raise Exception("An error occured while parsing that selection")
    