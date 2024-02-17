# coding=utf-8

class DefaultCode:
    def DefaultConfig(self):
        DefaultCode = {
            "format_version": "1.0.0",
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
                    }
                }
            }
        }
        return DefaultCode

    def Msg(self):
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
