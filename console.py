#!/usr/bin/python3
""" module containing implementation of the console
    command line interface for the AirBnB website """
import cmd
from models import storage
from models.base_model import BaseModel
import shlex


class HBNBCommand(cmd.Cmd):
    """ the console object """
    prompt = "(hbnb) "

    def do_quit(self, args):
        """Quit command to exit the program"""
        return (True)

    def do_EOF(self, args):
        """implement EOF"""
        return (True)

    def emptyline(self):
        """ prevent running previous command on empty line """
        pass

    def do_create(self, args):
        """ Usage: create <class_name> """
        if not args:
            print("** class name missing **")
        elif args not in storage.valid_models:
            print("** class doesn't exist **")
        else:
            new_model = eval(args)()
            print(new_model.id)
            new_model.save()
    
    def do_show(self, args):
        """ show <class_name> <model_id> """
        args = self.parse(args)
    
        if not args:
            print("** class name missing **")
        elif args[0] not in storage.valid_models:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            id_class, the_object = storage.get_model_n_ids(args[0], args[1])
            if args[1] not in [obj[1] for obj in id_class]:
                print("** no instance found **")
            else:
                for name, id in id_class:
                    if args[0] == name and args[1] == id:
                        print(the_object)
                        break

    def do_destroy(self, args):
        """ destroy <class_name> <model_id>\ndelete a model """
        args = self.parse(args)

        if not args:
            print("** class name missing **")
        elif args[0] not in storage.valid_models:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            id_class,_ = storage.get_model_n_ids(args[0], args[1])
            if args[1] not in [obj[1] for obj in id_class]:
                print("** no instance found **")
            else:
                for name, id in id_class:
                    key_to_delete = f"{name}.{id}"
                    storage.delete_model(key_to_delete)
                    break

    def do_all(self, args):
        """ all or all <class_name>
            print all objects or all objects that are instance of class_name
        """
        args = self.parse(args)

        if not args:  # no class name passed
            storage.print_all()
        elif args[0] not in storage.valid_models:
            print("** class doesn't exist **")
        else:
            storage.print_all(args[0])

    def do_update(self, args):
        """ update an instance based on class name and id """
        args = self.parse(args)
        l = len(args)

        if not l:
            print("** class name missing **")
        elif args[0] not in storage.valid_models:
            print("** class doesn't exist **")
        elif l < 2:
            print("** instance id missing **")
        elif l >= 2:
            id_class,_ = storage.get_model_n_ids(args[0], args[1])
            if args[1] not in [obj[1] for obj in id_class]:
                print("** no instance found **")
            elif l < 3:
                print("** attribute name missing **")
            elif l < 4:
                print("** value missing **")
            else:
                storage.update_model(*args)

    def parse(self, args)->list:
        """ parse the args string
        Args:
            args(str): the string of arguments
        
        Return:
            the list of args
        """
        return (shlex.split(args))

if __name__ == "__main__":
    HBNBCommand().cmdloop()
