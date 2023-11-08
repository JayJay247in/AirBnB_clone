#!/usr/bin/python3
'''Console for the HBnB clone'''
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User

class HBNBCommand(cmd.Cmd):
    '''Command interpreter'''

    classes = {
               'BaseModel': BaseModel, 'User': User
              }
    
    prompt = '(hbnb) '

    def do_create(self, arg):
        '''Creates a new instance, saves it to JSON file and prints id'''
        
        # Get class name
        cls_name = arg.split()[0]  

        # Check class is valid
        if cls_name not in classes:
            print("** class doesn't exist **")
            return
        
        # Create instance
        if cls_name == "BaseModel":
            obj = BaseModel()
        elif cls_name == "User":
            obj = User()

        obj.save()
        print(obj.id)

    def do_show(self, arg):
        '''Prints an instance based on class name and id'''
        
        args = arg.split()
        cls_name = args[0]

        if cls_name not in classes:
            print("** class doesn't exist **")
            return
            
        if len(args) < 2:
            print("** instance id missing **")
            return
        
        key = "{}.{}".format(cls_name, args[1])        
        if key not in storage.all():
            print("** no instance found **")
            return

        # Get object and print
        obj = storage.all()[key]
        print(obj)

    def do_quit(self, arg):
        '''Quit command to exit the program'''
        return True

    def do_EOF(self, arg):
        '''Alternative way to exit program'''
        print()
        return True

    def emptyline(self):
        '''Override to not execute anything on empty line'''
        pass

    def do_help(self, arg):
        '''List available commands with "help" or detailed help with "help cmd"'''
        if arg:
            cmd.Cmd.do_help(self, arg)
        else:
            cmd.Cmd.print_topics(self, "Available commands", cmds, 15, 80)

    def do_all(self, arg):
        """Prints string representations of all instances"""
        objects = storage.all()
        print([str(obj) for obj in objects.values()])

    def do_destroy(self, arg):
        """Deletes an instance and saves to JSON file"""
        args = arg.split()
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
        """Updates an instance and saves to JSON file"""
        args = arg.split()
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
                # Cast value to attribute type
                attr_type = type(getattr(storage.all()[key], args[2]))
                value = attr_type(args[3]) 
                setattr(storage.all()[key], args[2], value)
                storage.all()[key].save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()