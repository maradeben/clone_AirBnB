#!/usr/bin/python3
""" module containing implementation of the console
    command line interface for the AirBnB website """
import cmd


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


if __name__ == "__main__":
    HBNBCommand().cmdloop()
