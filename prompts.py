from abc import ABC, abstractclassmethod
from PyInquirer import prompt
import requests
from pprint import pprint

class Prompt(ABC):
    """Interface defining Prompt actions"""

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


class Read(Prompt):

    def prompt(self):
        raise Exception("Method not needed for reading database")

    def confirm(self):
        raise Exception("Method not needed for reading databse")

    def execute(self):
        r = requests.get(base_url + self.path) # FIXME broken variable
        pprint(r.json()['projects'])
        
        
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
                'filter': lambda x: [i.strip() for i in x.split(',')] 
            },
            {
                'type': 'input',
                'name': 'github_link',
                'message': 'Github link: ' 
            }
        ]

        self.input = prompt(input)

    def confirm(self):
        print('Update the database with the following data?')
        pprint(self.input), 

    def execute(self):
        pass
