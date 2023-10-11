#!/usr/bin/python3
import cmd
from models.base_model import BaseModels

"""script to impliment the console"""

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    """class to create the commandline using cmd"""

    def do_quit(self, commands):
        """Quit command to exit the program"""
        return True

    def do_EOF(self):
        """End of file"""
        return

    def do_create(self, cls_name):
        """Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id"""
        if not cls_name:
            print("** class name missing **")

        elif cls_name not in globals() or not isinstance(globals()[cls_name], type):
            print(f"Error: Class '{cls_name}' does not exist.")

        else:
            new = BaseModel()
            new.save()
            print("{}".format(new.id))

    def do_show(self, cls_name):
        """Prints the string representation of an instance based on the class name and id"""
        print(f"shows the instance {cls_name}")

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id (save the change into the JSON file)"""
        args = args.split()

        if not args:
            print("** class name missing **")

        elif len(args) < 2:
            print("** instance id missing **")

        else:
            cls_name, user_id = args[0], args[1]
            if cls_name not in globals() or not isinstance(globals()[cls_name], type):
                print("** class doesn't exist **")

            elif user_id not in globals() or not isinstance(globals()[user_id], type):
                print("** no instance found **")

            else:
                print(f"deletes {cls_name} with id {id}")

    def do_all(self, cls_name):
        """Prints all string representation of all instances based or not on the class name."""
        print(f"prints instances of {cls_name}")

    def do_update(self, args):
        """ Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file)."""
        args = args.split()

        if not args:
            print("** class name missing **")

        elif len(args) < 2:
            print("** instance id missing **")

        elif len(args) < 3:
            print("** attribute name missing **")

        elif len(args) < 4:
            print("** value missing **")

        else:
            cls_name, id, attribute_name, attribute_value = args[0], args[1], args[2], args[3]
            print(f"update {cls_name} with id {id} {attribute_name} of value {attribute_value}")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
