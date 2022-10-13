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
 
if __name__ == '__main__':
    HBNBCommand().cmdloop()
