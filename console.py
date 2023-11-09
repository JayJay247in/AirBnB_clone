#!/usr/bin/python3
'''Console for the HBnB clone'''
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
        print()

    def postloop(self):
        print() 

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

    def do_show(self, arg):
        '''Prints object based on class and id'''
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = args[0] + "." + args[1]
        if key not in storage.all():
            print("** no instance found **")
            return
        print(storage.all()[key])

    def do_all(self, arg):
        '''Prints string representations of instances'''
        print([str(obj) for obj in storage.all().values()])

    def do_destroy(self, arg):
        '''Deletes an instance and saves to file'''
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            if key not in storage.all():
                print("** no instance found **")
            else:
                del storage.all()[key]  
                storage.save()

    def do_update(self, arg):
        '''Updates instance and saves to file'''
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            if key not in storage.all():
                print("** no instance found **")
            elif len(args) < 3:
                print("** attribute name missing **")
            elif len(args) < 4:
                print("** value missing **")
            else:
                attr_type = type(getattr(storage.all()[key], args[2]))
                value = attr_type(args[3])
                setattr(storage.all()[key], args[2], value)
                storage.all()[key].save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()