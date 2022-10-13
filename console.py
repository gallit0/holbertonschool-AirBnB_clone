#!/usr/bin/python3
"""Cmd module to develop shell"""

import cmd


import models


class HBNBCommand(cmd.Cmd):


    classes = ['BaseModel']

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
            if b[1] == line[1]:
                print(a[i])
                return
        print("** no instance found **")
    def do_destroy(self, args):
        """Destroy command"""
        line = args.split(' ')
        if len(line) < 1:
            print('** class name missing **')
            return





if __name__ == '__main__':
    HBNBCommand().cmdloop()
