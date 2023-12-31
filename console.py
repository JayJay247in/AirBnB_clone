#!/usr/bin/python3
"""Console for the HBnB clone"""

import cmd
import sys
import shlex

from models.base_model import BaseModel
from models import storage
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State

classes = {
    'BaseModel': BaseModel, 'User': User, 'State': State,
    'City': City, 'Amenity': Amenity, 'Place': Place,
    'Review': Review
}

class HBNBCommand(cmd.Cmd):
    '''Command interpreter'''
    
    prompt = '(hbnb) '

    def preloop(self):
        """Prints if isatty is false"""
        if not sys.__stdin__.isatty():
            print("(hbnb)") 

    def postloop(self):
        """Prints if isatty is false"""
        if not sys.__stdin__.isatty():
            print("(hbnb) ", end="")

    def do_quit(self, arg):
        '''Quit command to exit'''
        return True

    def do_EOF(self, arg):
        '''Alternative exit'''
        return True

    def emptyline(self):
        '''Overrides default behavior'''
        pass

    def do_create(self, arg):
        '''Creates a new instance, saves to JSON file and prints id'''
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        obj = classes[args[0]]()
        obj.save()
        print(obj.id)
    
    def do_count(self, arg):
        """Retrieves the number of instances of a class""" 
        args = arg.split('.')
        if len(args) < 2:
            print("** class name missing **") 
            return

        if args[0] not in classes:
            print("** class doesn't exist **")
            return

        count = storage.count(classes[args[0]])
        print(count)

    def do_show(self, arg):
        """Prints an instance based on the class name and id"""
        args = arg.split('.')
        if len(args) < 2:
            print("** class name missing **")
            return

        if args[0] not in classes:
            print("** class doesn't exist **")
            return

        if len(args) < 3:
            print("** instance id missing **")
            return

        key = "{}.{}".format(args[0], args[1])
        if key not in storage.all():
            print("** no instance found **")
            return

        print(storage.all()[key])

    def do_all(self, arg):
        """Prints string representations of instances"""
        args = arg.split('.')
        if len(args) < 2:
            print("** class name missing **") 
            return

        if args[0] not in classes:
            print("** class doesn't exist **")
            return

        objs = storage.all(classes[args[0]])
        print([str(obj) for obj in objs.values()])


    def do_destroy(self, arg):
        """Deletes an instance and saves to JSON file"""
        args = arg.split('.')
        if len(args) < 2:
            print("** class name missing **")
            return

        if args[0] not in classes:
            print("** class doesn't exist **")
            return

        if len(args) < 3:
            print("** instance id missing **")
            return

        key = "{}.{}".format(args[0], args[1])
        if key not in storage.all():
            print("** no instance found **")
            return

        del storage.all()[key]
        storage.save()

    def do_update(self, arg):
        """Updates an instance and saves to JSON file"""
        args = arg.split('.')
        if len(args) < 2:
            print("** class name missing **")  
            return

        if args[0] not in classes:
            print("** class doesn't exist **")
            return

        if len(args) < 3:
            print("** instance id missing **")
            return

        key = "{}.{}".format(args[0], args[1])
        if key not in storage.all():
            print("** no instance found **")
            return

        if len(args) < 4:
            print("** attribute name missing **")
            return

        obj = storage.all()[key]

        if isinstance(args[3], dict):
            for attr, value in args[3].items():
                setattr(obj, attr, value) 
        else:
            # Update single attribute
            attr_type = type(getattr(obj, args[3]))
            value = attr_type(args[4])
            setattr(obj, args[3], value)

        storage.all()[key].save()

    def emptyline(self):
        """Overrides empty line behavior"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()