#!/usr/bin/python3
"""
This is the console module.
"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User



class HBNBCommand(cmd.Cmd):
    """Command class"""
    prompt = "(hbnb) "

    classes = {
            'BaseModel': BaseModel,
            'User': User
            }

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

    def do_create(self, arg):
        """Create a new instance of BaseModel, saves it, and prints the id."""
        if not arg:
            print("** class name missing **")
            return

        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance."""
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        try:
            class_name = args[0]
            if class_name not in self.classes:
                print("** class doesn't exist **")
                return

            if len(args) < 2:
                print("** instance id missing **")
                return

            instance_id = args[1]
            key = f"{class_name}.{instance_id}"
            if key not in storage.all():
                print("** no instance found **")
                return

            print(storage.all()[key])
        except IndexError:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id."""
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        try:
            if args[0] not in self.classes:
                print("** class doesn't exist **")
                return

            if len(args) < 2:
                print("** instance id missing **")
                return

            key = args[0] + "." + args[1]
            del storage.all()[key]
            storage.save()
        except IndexError:
            print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances."""
        objs = []
        if arg:
            if arg not in self.classes:
                print("** class doesn't exist **")
                return
            objs = [str(obj) for obj in storage.all().values()]
        print(objs)

    def do_update(self, arg):
        """Updates an instance based on the class name and id."""
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        try:
            if args[0] not in self.classes:
                print("** class doesn't exist **")
                return

            if len(args) == 1:
                print("** instance id missing **")
                return

            class_name = args[0]
            instance_id = args[1]
            key = f"{class_name}.{instance_id}"

            if key not in storage.all():
                print("** no instance found **")
                return

            if len(args) == 2:
                print("** attribute name missing **")
                return

            if len(args) == 3:
                print("** value missing **")
                return

            attribute_name = args[2]
            attribute_value = args[3].strip('"')
            if attribute_name not in ["id", "created_at", "updated_at"]:
                instance =  storage.all()[key]
                setattr(instance, attribute_name, attribute_value)
                storage.save()
        except IndexError:
            print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
