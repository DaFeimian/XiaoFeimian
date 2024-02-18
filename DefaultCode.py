# coding=utf-8

class DefaultCode:
    def DefaultConfig(self):
        DefaultCode = {
            "format_version": "1.0.3",
            "dfm:chat_learning": {
                "description": {
                    "key": "",
                    "host": "localhost",
                    "port": "23750",
                    "qq": "3567749021",
                    "session": ""
                },
                "components": {
                    "dfm:learning_list": {
                        "value": []
                    },
                    "dfm:reply_list": {
                        "value": []
                    },
                    "dfm:reply": {
                        "chance": 1.0,
                        "cos_match": True,
                        "cos_match_value": 0.5,
                        'reply_wait_base_time': 1.0,
                        'reply_wait_float_time': 0.5
                    },
                    "dfm:ban": {
                        "bool": True,
                        "ban_list": ['操', '操你妈', '丝袜', '色色', '立了', '群', '你妈'],     # 违禁词列表，宽泛检测。如'操.你.妈','你妈妈在操场'也会被是作为违禁词。
                        "admin_ban_text": "{name}你这个坏蛋！竟然说了{n}个坏字！我要撤回你！",    # 有管理员的时候遇到违禁词(会撤回对应消息)，值为空时则不回复，{n}表示违禁检测的数量,{name}表示名字
                        "not_admin_ban_text": "{name}你的话里有{n}个坏字！我不听！"    # 没有管理员的时候遇到违禁词时回复，值为空时则不回复，{n}表示违禁检测的数量,{name}表示名字
                    }
                }
            }
        }
        return DefaultCode

    def Msg(self):
        MsgDict = {
            "type": "GroupMessage",
            "messageChain": [
                {
                    "type": "Source",
                    "id": 730926,
                    "time": 1708207189
                },
                {
                    "type": "Plain",
                    "text": "成功了"
                }
            ],
            "sender": {
                "id": 2687145099,
                "memberName": "Staff-lonel(@我没用)",
                "specialTitle": "Staff",
                "permission": "ADMINISTRATOR",
                "joinTimestamp": 1688032169,
                "lastSpeakTimestamp": 1708207189,
                "muteTimeRemaining": 0,
                "group": {
                    "id": 687577485,
                    "name": "大肥免组件交流·①群",
                    "permission": "MEMBER"
                },
                "active": None
            }
        }
        MsgList = [{'type': 'GroupMessage',
                    'messageChain': [{'type': 'Source', 'id': 4061, 'time': 1708194224},
                                     {'type': 'Plain', 'text': '111'}],
                    'sender': {'id': 764416606, 'memberName': '大肥免', 'specialTitle': '啊？',
                               'permission': 'ADMINISTRATOR',
                               'joinTimestamp': 1675522314, 'lastSpeakTimestamp': 1708194225, 'muteTimeRemaining': 0,
                               'group': {'id': 766176115, 'name': '内测群', 'permission': 'MEMBER'}}},
                   {'type': 'GroupMessage',
                    'messageChain': [
                        {'type': 'Source',
                         'id': 4061,
                         'time': 1708194224},
                        {'type': 'Plain',
                         'text': '111'}],
                    'sender': {
                        'id': 764416606,
                        'memberName': '大肥免',
                        'specialTitle': '啊？',
                        'permission': 'ADMINISTRATOR',
                        'joinTimestamp': 1675522314,
                        'lastSpeakTimestamp': 1708194225,
                        'muteTimeRemaining': 0,
                        'group': {
                            'id': 766176115,
                            'name': '内测群',
                            'permission': 'MEMBER'}}},
                   {'type': 'GroupMessage',
                    'messageChain': [{'type': 'Source', 'id': 4061, 'time': 1708194224},
                                     {'type': 'Plain', 'text': '111'}],
                    'sender': {'id': 764416606, 'memberName': '大肥免', 'specialTitle': '啊？',
                               'permission': 'ADMINISTRATOR',
                               'joinTimestamp': 1675522314, 'lastSpeakTimestamp': 1708194225, 'muteTimeRemaining': 0,
                               'group': {'id': 766176115, 'name': '内测群', 'permission': 'MEMBER'}}},
                   {'type': 'GroupMessage',
                    'messageChain': [
                        {'type': 'Source',
                         'id': 4061,
                         'time': 1708194224},
                        {'type': 'Plain',
                         'text': '111'}],
                    'sender': {
                        'id': 764416606,
                        'memberName': '大肥免',
                        'specialTitle': '啊？',
                        'permission': 'ADMINISTRATOR',
                        'joinTimestamp': 1675522314,
                        'lastSpeakTimestamp': 1708194225,
                        'muteTimeRemaining': 0,
                        'group': {
                            'id': 766176115,
                            'name': '内测群',
                            'permission': 'MEMBER'}}}]
