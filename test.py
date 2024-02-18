banlist = ['nm', '草', '操你妈']

Usertext = '你妈妈在操场'

Bantext = '你这个坏蛋！竟然说了个坏字！要是我有管理员我就撤回你！'


messageChain = [
                {
                    "type": "Source",
                    "id": 730926,
                    "time": 1708207189
                },
                {
                    "type": "Plain",
                    "text": "成功了"
                },
                {
                    "type": "Plain",
                    "text": "成功了"
                },
                {
                    "type": "Plain",
                    "text": "成功了"
                }
            ]

print(messageChain[1:])

def GetBan(text):
    Bool = False
    AllBanNum = 0
    for ban in banlist:
        AllNum = len(ban)
        BanNum = 0
        for Oneban in ban:
            for Onetext in text:
                if Onetext == Oneban:
                    BanNum += 1
                    AllBanNum += 1
        if BanNum >= AllNum:
            Bool = True
    return Bool, AllBanNum

Bool, AllBanNum = GetBan(Usertext)
if Bool:
    print(Bantext.format(n=AllBanNum))

test = '1'

print(True if test else False)