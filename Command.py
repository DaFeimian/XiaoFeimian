# coding=utf-8
from CommandControl import CommandControl

class Command(object):
    def __init__(self):
        self.CommandDict = {
            'help': ['Help'],
            '?': ['Help'],
            'config help': ['ConfigHelp']
        }
        self.CommandList = []
        for OneCommand in self.CommandDict:
            self.CommandList.append(OneCommand)
        print('Loading command list.')

    def ListenCommand(self, *args):
        try:
            UserCommand = repr(input('XiaoFeimian Command:'))
            CommandResult = self.TestCommand(UserCommand)
            if not CommandResult:
                print('Command error. You can send "help" to get command list.')
            self.ListenCommand()
        except:
            print('Command type error.')
            self.ListenCommand()

    def TestCommand(self, UserCommand):
        UserCommandKey = UserCommand.split("'")[1]
        Bool = True if UserCommandKey in self.CommandList else False
        if Bool:
            for FuncName in self.CommandDict[UserCommandKey]:
                Func = getattr(CommandControl, FuncName)
                Func(CommandControl, UserCommandKey)
        return Bool


