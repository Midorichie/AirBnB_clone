#!/usr/bin/python3
"""It contains the entry point of the command interpreter"""
import cmd
import re
import models
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.user import User
from models.place import Place
from models.state import State
from models.review import Review
# from models.engine.file_storage import FileStorage


class HBNBCommand(cmd, CMD):
    """The class that handles the command line interpreter"""

    prompt = '(hbnb) '

class_mapping = {
        'BaseModel': BaseModel,
        'User': User,
        'Place': Place,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Review': Review
        # Add more class mappings as needed
    }
    
    def precmd(self, line):
        """Intercepting command flow
        Commands are intercepted and redesigned
        This allows for valid alternate means of passing a command
        USAGE:
            User.all() === all User
            BaseModel.create === create BaseModel

        Return:
            It returns the precmd function with the redesigned command
            on the valid command entered
        """


        if "." in line:
            line = re.sub(r'(?<!@)[.,(]', ' ', re.sub(r'[),"]', '', line))
            line = re.sub(r'(\w+)\s+(\w+)', r'\2 \1', line, 1)
        return cmd.Cmd.precmd(self, line)
    
    def do_create(self, line):
        """Creates a new instance of BaseModel, saves it"""
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return

        cls_name = args[0]

        if cls_name in HBNBCommand.class_mapping:
            new_instance = HBNBCommand.class_mapping[cls_name]()
            print('{}'.format(new_instance.id))
            new_instance.save()
        else:
            print("** class doesn't exist **")

    def help_create(self):
        """documentation for when 'help create' is called"""
        print('Creates a new instance of BaseModel, saves it')
        print('(to the JSON file) and prints the id\n')

    def do_show(self, line):
        """Prints the string representation of an instance
        based on the class name and id"""

        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        
        if len(args) < 2:
            print("** instance id missing **")
            return

        cls_name = args[0]
        instance_id = args[1]

        if cls_name in HBNBCommand.class_mapping:
            instance_key = '{}.{}'.format(cls_name, instance_id)
            all_objs = models.storage.all()

            if instance_key in all_objs.keys():
                obj = all_objs[instance_key]
                print(obj)
            else:
                print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def help_show(self):
        """documentation for when 'help show' is called"""
        print("\n".join([
            "Usage: show [class_name e.g User] [id]",
            "Prints the string representation of an instance",
            "based on the class name and id"]))

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id
        (save the change into the JSON file)"""
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        
        if len(args) < 2:
            print("** instance id missing **")
            return

        cls_name = args[0]
        instance_id = args[1]

        if cls_name in HBNBCommand.class.mapping:
            instance_key = '{}.{}'.format(cls_name, instance_id)
            all_objs = models.storage.all()

            if instance_key in all_objs.keys():
                del models.storage.all()[instance_key]
                models.storage.save()
            else:
                print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def help_destroy(self):
        """documentation for when 'help destroy' is called"""
        print('Deletes an instance based on the class name and id '
                '(save the change into the JSON file).\n')

    def do_all(self, line):
        """Prints all string representation of all instances
        based or not on the class name"""
        args = line.split()

        all_objs = models.storage.all()

        all_objs_list = []
        if not line:
            for obj in all_objs.values():
                all_objs_list.append(str(obj))
            print(all_objs_list)
            return

        cls_name = args[0]
        if cls_name not in HBNBCommand.class_mapping:
            print("** class doesn't exist **")
            return

        specific_objs_list = []
        for obj in all_objs.values():
            if type(obj).__name__ == cls_name:
                specific_objs_list.append(str(obj))
        print(specific_objs_list)

    def help_all(self):
        """documentation for when 'help all' is called"""
        print('Prints all string representation of all instances '
                'based or not on the class name.\n')

    def do_update(self, line):
        """Updates an instance based on the class name and id"""
        args = line.split()
        if not line:
            print("** class name missing **")
            return

        if len(args) == 1:
            print("** instance id missing **")
            return

        cls_name = args[0]
