#!/usr/bin/python3
"""Cmd module to develop shell"""

import cmd


import models


class HBNBCommand(cmd.Cmd):

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
        if args == 'BaseModel':
            obj = models.base_model.BaseModel()
        else:
            print('** class doesn\'t exist **')
            return
        print(obj.id)
 
    def do_show(self, args):
        """Show command"""
        line = args.split(' ')
        if len(line) < 1:
            print('** class name missing **')
            return
        if len(line) < 2:
            print('** instance id missing **')
            return
        if line[0] == 'BaseModel':
            a = models.storage.all()
        else:
            print("** class doesn't exist **")
            return
        try:
            d = a[line[0] + '.' + line[1]]
        except Exception as e:
                print('** no instance found **')
                return
        print(d.__dict__)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
