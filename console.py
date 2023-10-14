#!/usr/bin/python3

"""script to impliment the console"""

import cmd
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import sys


class HBNBCommand(cmd.Cmd):
    """class to create the commandline using cmd"""
    prompt = "(hbnb) "

    def __init__(self, interactive=True):
        """initilisation phase"""
        super().__init__()
        self.my_instances = {}
        self.interactive = interactive

    def do_quit(self, command):
        """Quit command to exit the program"""
        if self.interactive:
            return True
        exit()

    def do_EOF(self, args):
        """End of file"""
        print()
        exit()

    def emptyline(self):
        """prevents repetition of the previous command if no command"""
        pass

    def do_create(self, cls_name):
        """Creates a new instance and prints the id"""
        if not cls_name:
            print("** class name missing **")
            return

        elif (
                cls_name not in globals() or not
                isinstance(globals()[cls_name], type)
                ):
            print("** class doesn't exist **")

        else:
            new_instance = globals()[cls_name]()
            new_instance.save()
            instances_name = "my_instance_{}".format(len(self.my_instances))
            self.my_instances[instances_name] = new_instance
            print("{}".format(new_instance.id))

    def do_show(self, args):
        """Prints the string representation of an instance"""
        args = args.split()
        if not args:
            print("** class name missing **")
        elif len(args) < 2:
            print("** instance id missing **")

        else:
            cls_name, user_id = args[0], args[1]
            if (
                    cls_name not in globals() or not
                    isinstance(globals()[cls_name], type)
                    ):
                print("** class doesn't exist **")

            else:
                for key, value in self.my_instances.items():
                    if user_id in value:
                        print(value)
                        return
                print("** no instance found **")

    def do_destroy(self, args):
        """Deletes an instance)"""
        args = args.split()

        if not args:
            print("** class name missing **")

        elif len(args) < 2:
            print("** instance id missing **")

        else:
            cls_name, user_id = args[0], args[1]

            keys_to_remove = []
            for key, value in self.my_instances.items():
                if user_id in value:
                    keys_to_remove.append(key)
                    for key in keys_to_remove:
                        del self.my_instances[key]
                    return
            print("** no instance found **")

    def do_all(self, args):
        """Prints all string representation of all instances"""

        instances = []

        if not args:
            for key, value in self.my_instances.items():
                instances.append(str(value))

        elif (
                args not in globals() or not
                isinstance(globals()[args], type)
                ):
            print("** class doesn't exist **")
            return

        else:
            for key, value in self.my_instances.items():
                if isinstance(value, globals()[args]):
                    instances.append(str(value))

        print(instances)

    def do_update(self, args):
        """ Updates an instance"""
        args = args.split()

        if not args:
            print("** class name missing **")

        elif len(args) < 2:
            print("** instance id missing **")

        elif len(args) < 3:
            print("** attribute name missing **")

        elif len(args) < 4:
            print("** value missing **")

        elif len(args) > 4:
            print("too many arguments")

        else:
            cls_name, user_id, attribute_name,
            attribute_value = args[0], args[1], args[2], args[3]

            if (
                    cls_name not in globals() or not
                    isinstance(globals()[cls_name], type)
                    ):
                print("** class doesn't exist **")
                return

            for key, value in self.my_instances.items():
                if (
                        isinstance(value, globals()[cls_name]) and
                        value.id == user_id
                        ):
                    setattr(value, attribute_name, attribute_value)
                    value.save()
                    return

            print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
