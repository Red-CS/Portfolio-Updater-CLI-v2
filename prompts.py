from abc import ABC, abstractclassmethod
from PyInquirer import prompt
import requests
from pprint import pprint


class Prompt(ABC):
    """Interface defining Prompt actions"""

    def __init__(self):
        self.url = 'https://redwilliams.dev/api/projects/'

    @abstractclassmethod
    def prompt(self):
        """Prompts the user the necessary questions
        depending on the action chosen.
        """
        pass

    @abstractclassmethod
    def confirm(self):
        """Defines an aciton for confirming to the user
        about their selection(s)
        """
        pass

    @abstractclassmethod
    def execute(self):
        """Executes the necessary API calls to fulfill the
        users requests
        """
        pass


class Read(Prompt): # TODO clarify naming between files: Read or View

    def prompt(self):
        raise Exception("Method not needed for reading database")

    def confirm(self):
        raise Exception("Method not needed for reading databse")

    def execute(self):
        r = requests.get(self.url)
        output = r.json()['projects']
        return output


class Add(Prompt):

    def __init__(self):
        self.input = {}

    def prompt(self):
        input = [
            {
                'type': 'input',
                'name': 'name',
                'message': 'Project name:'
            },
            {
                'type': 'input',
                'name': 'description',
                'message': 'Project description:'
            },
            {
                'type': 'input',
                'name': 'techs',
                'message': 'Technologies used: (comma-separated)',
                'filter': lambda list: [i.strip() for i in list.split(',')]
            },
            {
                'type': 'input',
                'name': 'github_link',
                'message': 'Github link:'
            },
            {
                'type': 'input',
                'name': 'project_link',
                'message': 'Project link:'
            },
            {
                'type': 'confirm',
                'name': 'featured',
                'message': 'Is this a featured project? (y/n)',
                'default': False
            }
        ]

        self.input = prompt(input)

    def confirm(self):
        print('Update the database with the following data?')
        pprint(self.input)

    def execute(self):
        pass


class Update(Prompt):

    def __init__(self):
        self.input = {}

    def prompt(self):
        
        project_list = sorted([project['project_name'] for project in Read().execute()])
        
        input = [
            {
                'type': 'list',
                'name': 'name',
                'message': 'Select the project to update:',
                'choices': project_list
            }
        ]

        self.input = prompt(input)

    def confirm(self):
        pass

    def execute(self):
        pass
