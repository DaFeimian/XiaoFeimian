# coding=utf-8
import os
import json
import threading
import time

from Command import Command
from DefaultCode import DefaultCode
from Main import Main

class XiaoFeimian(object):
    def __init__(self):
        print('Welcome to use DaFeimian python exe -- XiaoFeimian Chat Learning\n欢迎使用大肥免python程序——小肥免聊天学习')
        print('Tips： Idk if Chinese can run the display smoothly, so some content uses English prompts.\n我不知道中文能不能顺利运行显示，所以一些内容使用的是英文提示，肥免懒得设置编码')
        self.InitBaseConfigFile()
        self.Config = {}
        self.CommandThread = None
        self.MainThread = None

    # 开始运行
    def StartRunning(self):
        self.MainThread = threading.Thread(target=Main, args=(self.Config,), name='Main')
        self.MainThread.start()
        time.sleep(1)
        print('Wait 10 seconds to start the command.')
        time.sleep(10)
        self.CommandThread = threading.Thread(target=Command().ListenCommand, args=(1,), name='Command')
        self.CommandThread.start()


    # 生成基础配置文件
    def InitBaseConfigFile(self):
        self.TestAndCreateFolder('/XiaoFeimianConfig')
        try:
            with open('/XiaoFeimianConfig/config.json', 'r') as ConfigFile:
                Data = ConfigFile.read()
                self.Config = json.loads(Data)
                print('Config file loading completed. Version is {0}'.format(self.Config['format_version']))
        except:
            with open('/XiaoFeimianConfig/config.json', 'w') as ConfigFile:
                DefaultConfigJson = DefaultCode().DefaultConfig()
                json.dump(DefaultConfigJson, ConfigFile, indent=4, ensure_ascii=False)
                self.Config = DefaultConfigJson
                print('The config file is in disk root path.')

        TestResult, ErrorNum, ErrorKeyList = self.TestConfigFile()
        if not TestResult:
            print('Config file error. Error num is {0}. Error list is {1}'.format(ErrorNum, ErrorKeyList))
        else:
            self.StartRunning()
            # self.CommandThread.join()

    def TestConfigFile(self):
        print('Starting config file simple verification. Maybe have other error what can not test.')
        ErrorNum = 0
        ErrorKeyList = []
        RootKeyList = ['dfm:chat_learning']
        FirstKeyDict = {
            'dfm:chat_learning': ['description', 'components']
        }
        for RootKey in RootKeyList:
            RootDict = self.Config.get(RootKey, None)
            if not RootDict:
                ErrorNum += 1
                ErrorKeyList.append(RootKey)
            else:
                FirstKeyDictList = FirstKeyDict[RootKey]
                for FirstKey in FirstKeyDictList:
                    FirstDict = RootDict.get(FirstKey, None)
                    if not FirstDict:
                        ErrorNum += 1
                        ErrorKeyList.append(FirstKey)
        Bool = True if not ErrorNum else False
        return Bool, ErrorNum, ErrorKeyList


    def TestAndCreateFolder(self, Path):
        folder = os.path.exists(Path)
        if not folder:
            os.makedirs(Path)


if __name__ == '__main__':
    XiaoFeimian()