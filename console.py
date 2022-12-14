#!/usr/bin/python3
"""Cmd module to develop shell"""

import cmd


from models.user import User


from models.state import State


from models.city import City


from models.amenity import Amenity


from models.place import Place


from models.review import Review


import json


import models


def create_aux(a):
    """Auxiliar functin for create"""
    if a == 'BaseModel':
        return models.base_model.BaseModel()
    if a == 'User':
        return User()
    if a == 'State':
        return State()
    if a == 'City':
        return City()
    if a == 'Place':
        return Place()
    if a == 'Review':
        return Review()
    if a == 'Amenity':
        return Amenity()


class HBNBCommand(cmd.Cmd):
    classes = [
        'BaseModel',
        'User',
        'State',
        'City',
        'Amenity',
        'Place',
        'Review'
    ]

    prompt = '(hbnb) '

    def do_EOF(self, line):
        return True

    def do_quit(self, args):
        """Quit command to exit the program"""
        raise SystemExit

    def emptyline(self):
        """Do nothing after empty line + enter"""
        pass

    def do_create(self, args):
        """Create command"""
        if len(args) < 1:
            print('** class name missing **')
            return
        if args in self.classes:
            obj = create_aux(args)
        else:
            print('** class doesn\'t exist **')
            return
        models.storage.save()
        print(obj.id)

    def do_show(self, args):
        """Show command"""
        line = args.split(' ')
        if len(line) == 1 and line[0] == '':
            print('** class name missing **')
            return
        if line[0] not in self.classes:
            print('** class doesn\'t exist **')
            return
        if len(line) == 1:
            print('** instance id missing **')
            return
        a = models.storage.all()
        for i in a:
            b = i.split('.')
            if b[1] == line[1] and b[0] == line[0]:
                print(a[i])
                return
        print("** no instance found **")

    def do_destroy(self, args):
        """Destroy command"""
        line = args.split(' ')
        if len(line) == 1 and line[0] == '':
            print('** class name missing **')
            return
        if len(line) < 2:
            print('** instance id missing **')
            return
        if line[0] not in self.classes:
            print('** class doesn\'t exist **')
            return
        try:
            a = models.storage.all()
            key = line[0] + '.' + line[1]
            a[key]
        except:
            print('** no instance found **')
            return
        with open('file.json', 'w') as f:
            del a[key]
            f.write(json.dumps(a, default=str))
        models.storage.reload()

    def do_all(self, args):
        """Show all"""
        line = args.split(' ')
        arr = []
        a = models.storage.all()
        if len(line) < 1 or line[0] == '':
            for i in a:
                arr.append(str(a[i]))
            print(arr)
            return
        if line[0] not in self.classes:
            print('** class doesn\'t exist **')
            return
        for i in a:
            b = i.split('.')
            if b[0] == line[0]:
                arr.append(str(a[i]))
        print(arr)

    def do_update(self, args):
        """Update command"""
        line = args.split(' ')
        if len(line) < 1 or line[0] == '':
            print("** class name missing **")
            return
        if line[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(line) < 2:
            print("** instance id missing **")
            return
        if len(line) < 3:
            print("** attribute name missing **")
            return
        if len(line) < 4:
            print("** value missing **")
            return
        a = models.storage.all()
        for i in a:
            b = i.split('.')
            if b[1] == line[1]:
                d = a[line[0] + '.' + line[1]]
                break
        else:
            print('** no instance found **')
            return
        d.__dict__[line[2]] = line[3]
        models.storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
