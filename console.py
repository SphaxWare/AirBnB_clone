#!/usr/bin/python3
"""command interpreter"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Command class"""
    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, line):
        """EOF exit the program
        """
        print("")
        return True

    def emptyline(self):
        """Ignore empty lines
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
