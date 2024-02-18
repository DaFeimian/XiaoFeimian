# coding=utf-8

class CommandControl:
    def Help(self, Command):
        print('\nhelp: 帮助\n'
              'config help: 配置文件帮助\n'
              '下面的这些都还没写！你可以输入config help来帮助你配置！\n'
              'learning add <群号>： 添加学习群聊\n'
              'learning remove <群号>: 删除学习群聊\n'
              'reply add <群号>: 添加回复群聊\n'
              'reply remove <群号>: 删除回复群聊\n'
              'reply set <Key: chance, cos_match, cos_match_value, reply_wait_base_time, reply_wait_float_time> <值>: 设置<回复概率，是否开启相似度计算，相似度计算范围，回复基础时间，回复浮动时间>\n')

    def tips(self, Command):
        print('\n需要重启程序以更新配置，啊因为这是1.0.0版本，肥免还没写这么都功能哦！\n')

    def disable(self, Command):
        print(
            '\n啊这个程序只花了5个小时写，所以肥免还没写这个功能呢！你可以手动前往程序所在磁盘根目录的"XiaoFeimianConfig"文件夹，里面的"config.json"就是配置文件~')

    def ConfigHelp(self, Command):
        print('\n啊这个程序只花了5个小时写，所以肥免还没写这个功能呢！你可以手动前往程序所在磁盘根目录的"XiaoFeimianConfig"文件夹，里面的"config.json"就是配置文件~')
        print('\nconfig.json文件架构是直接学Minecraft BE的！因为肥免刚好是我的世界中国版开发者，学了一点python!')
        print('\nconfig.json翻译：')
        print('\nformat_version: 版本号')
        print('\nkey: 不用填')
        print('\nhost: 地址，对应mirai-api-http-2.10.0的配置文件http里的那个host')
        print('\nport: 端口，对应mirai-api-http-2.10.0的配置文件http里的那个port')
        print('\nqq: 你的QQ号，对应mirai-api-http-2.10.0的配置文件http里的那个port')
        print('\nsession: 不用填，对应mirai-api-http-2.10.0的配置文件singleMode设置为true')
        print('\ndfm:learning_list: 学习群聊的群号列表')
        print('\ndfm:reply_list: 回复群聊的群号列表')
        print('\ndfm:chance: 回复概率(0~1)')
        print('\ndfm:cos_match: 是否进行相似度计算以寻找答案(bool)')
        print('\ndfm:cos_match_value: 相似度计算达到多少就匹配答案(0~1)')
        print('\ndfm:reply_wait_base_time: 回复行为的基础等待时间')
        print('\ndfm:reply_wait_float_time: 回复行为的浮动时间(+-)')
        print('\ndfm:ban <bool>: 是否开启违禁词检测')
        print('\ndfm:ban <ban_list>: 违禁词列表，宽泛检测。如"操.你.妈","你妈妈在操场"也会被是作为违禁词')
        print('\ndfm:ban <admin_ban_text>: 有管理员的时候遇到违禁词(会撤回对应消息)，值为空时则不回复，{n}表示违禁检测的数量,{name}表示名字')
        print('\ndfm:ban <not_admin_ban_text>: 没有管理员的时候遇到违禁词时回复，值为空时则不回复，{n}表示违禁检测的数量,{name}表示名字')
        print('\n后面有空再完善叭！')