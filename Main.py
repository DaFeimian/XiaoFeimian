# coding=utf-8
import json
import os
import random
import threading
import time
import difflib

import requests as r

class Main(object):
    def __init__(self, Config, *args):
        self.Config = Config
        self.IsConnect = False
        print('Starting Completed')
        self.ConnectHttp()
        self.IsListen = False
        self.IsConnected = False
        self.ListenMsgThread = None

    def GetIsConnect(self):
        return self.IsConnect

    def SetIsListen(self, Value):
        self.IsListen = Value
        if self.IsListen and self.IsConnected:
            self.ListenMsgThread = threading.Thread(target=self.ListenMsg, args=(self.Config,), name='ListenMsg')
            self.ListenMsgThread.start()

    def ConnectHttp(self):

        def Reconnect():
            print('Connect http failed. Reconnecting...')
            time.sleep(5)
            self.ConnectHttp()

        Description = self.Config['dfm:chat_learning']['description']
        print('Start connect http')
        key, host, port, qq, session = Description['key'], Description['host'], Description['port'], Description['qq'], Description['session']
        print('\nkey:', key)
        print('host:', host)
        print('port:', port)
        print('qq:', qq)
        print('session:', session, '\n')
        def test():
            Url = 'http://' + host + ':' + port + '/groupList?sessionKey=' + session
            # Url = 'http://' + host + '/groupList?sessionKey=' + session
            Result = r.request('get', Url)
            print(Result)
            if Result:
                Result = json.loads(Result.text)
                Message = Result['data']
                print(Message)
        try:
            Url = 'http://' + host + ':' + port + '/groupList?sessionKey=' + session
            Result = r.request('get', Url)
            print(Result)
            if Result:
                Result = json.loads(Result.text)
                if Result['code'] == 0:
                    self.IsConnected = True
                    print('Http is connected.')
                    self.Connected()
                else:
                    Reconnect()
            else:
                Reconnect()
        except:
            Reconnect()

    def Connected(self):
        self.ListenMsgThread = threading.Thread(target=self.ListenMsg, args=(self.Config,), name='ListenMsg')
        self.ListenMsgThread.start()

    def GetUrl(self, GetName):
        Description = self.Config['dfm:chat_learning']['description']
        key, host, port, qq, session = Description['key'], Description['host'], Description['port'], Description['qq'], Description['session']
        Url = 'http://' + host + ':' + port + '/{0}?sessionKey='.format(GetName) + session
        return Url

    def PostUrl(self, PostName):
        Description = self.Config['dfm:chat_learning']['description']
        key, host, port, qq, session = Description['key'], Description['host'], Description['port'], Description['qq'], Description['session']
        Url = 'http://' + host + ':' + port + '/{0}'.format(PostName)
        return Url

    def RequestGet(self, Url):
        Result = r.request('get', Url)
        if Result:
            Result = json.loads(Result.text)
            if Result['code'] == 0:
                return Result
            else:
                return False
        else:
            return False

    def ListenMsg(self, *args):
        while True:
            MsgCountUrl = self.GetUrl('countMessage')
            MsgCountResult = self.RequestGet(MsgCountUrl)
            if MsgCountResult:
                Count = MsgCountResult['data']
                if Count:
                    print('Robot has {0} messages not read.'.format(Count))
                    GetMsgUrl = self.GetUrl('fetchMessage') + '&count={0}'.format(Count)
                    GetMsgResult = self.RequestGet(GetMsgUrl)
                    if GetMsgResult:
                        MsgList = GetMsgResult['data']
                        self.ProcessMsg(MsgList)
            time.sleep(1)

    # 处理消息，好像是老版本的http接口有bug会给4个一样的缓存消息
    def ProcessMsg(self, MsgList):
        self.TestAndCreateFolder('/XiaoFeimianConfig/Msg')
        for MsgDict in MsgList:
            # 群消息
            if MsgDict['type'] == 'GroupMessage':
                # 学习
                LearningList = self.Config['dfm:chat_learning']['components']['dfm:learning_list']['value']
                if MsgDict['sender']['group']['id'] in LearningList:
                    print('Add Learning Msg.')
                    MsgPath = '/XiaoFeimianConfig/Msg/{0}.json'.format(str(MsgDict['sender']['group']['id']))
                    if os.path.exists(MsgPath):
                        with open(MsgPath, 'r', encoding='utf-8') as MsgFile:
                            Json = MsgFile.read()
                            Dict = json.loads(Json)
                            DictMsgList = Dict['MsgList']
                            DictMsgList.append(MsgDict)
                            NewDict = {
                                'MsgList': DictMsgList
                            }
                        with open(MsgPath, 'w', encoding='utf-8') as MsgFile:
                            json.dump(NewDict, MsgFile, indent=4, ensure_ascii=False)
                    else:
                        DictMsgList = []
                        DictMsgList.append(MsgDict)
                        NewDict = {
                            'MsgList': DictMsgList
                        }
                        with open(MsgPath, 'w', encoding='utf-8') as MsgFile:
                            json.dump(NewDict, MsgFile, indent=4, ensure_ascii=False)
                    self.LearningUpdate(MsgPath, MsgDict['sender']['group']['id'], MsgDict)
                else:
                    print('Not learning msg.')

                # 回复
                ReplyList = self.Config['dfm:chat_learning']['components']['dfm:reply_list']['value']
                if MsgDict['sender']['group']['id'] in ReplyList:
                    print('Found answer msg.')
                    Chance = random.randint(1, 100)
                    ReplyConfigDict = self.Config['dfm:chat_learning']['components']['dfm:reply']
                    if Chance <= ReplyConfigDict['chance'] * 100:
                        # 检索对应群词库，后续应该补充，检索对应群词库不到的去检索整合词库
                        AnswerMsgPath = '/XiaoFeimianConfig/Msg/{0}_QA.json'.format(MsgDict['sender']['group']['id'])
                        try:
                            with open(AnswerMsgPath, 'r', encoding='utf-8') as AnswerMsgFile:
                                Json = AnswerMsgFile.read()
                                AnswerDict = json.loads(Json)
                                AnswerList = AnswerDict['QAList']
                        except:
                            AnswerList = []
                        QuestionType, QuestionData = self.ProcessMsgTypeToLearning(MsgDict)
                        SendNum = 0
                        for OneQA in AnswerList:
                            # 100% 匹配
                            if QuestionType == OneQA['QuestionMsgType'] and QuestionData == OneQA['QuestionMsg']:
                                AnswerMsgDict = random.choice(OneQA['AnswerList'])
                                AnswerMsg = {
                                    "type": AnswerMsgDict['AnswerMsgType']
                                }
                                MsgType = AnswerMsgDict['AnswerMsgType']
                                if MsgType == 'Plain':
                                    AnswerMsg['text'] = AnswerMsgDict['AnswerMsg']
                                if MsgType == 'Image' or MsgType == 'Voice':
                                    AnswerMsg['url'] = AnswerMsgDict['AnswerMsg']
                                if MsgType == 'Face':
                                    AnswerMsg['faceId'] = AnswerMsgDict['AnswerMsg']
                                Timer = random.uniform(ReplyConfigDict['reply_wait_base_time'] - ReplyConfigDict['reply_wait_float_time'],
                                                  ReplyConfigDict['reply_wait_base_time'] + ReplyConfigDict['reply_wait_float_time'])
                                print('Send msg wait time: {0} seconds'.format(Timer))
                                time.sleep(Timer)
                                SendNum += 1
                                self.SendGroupAnswerMsg(AnswerMsg, MsgDict['sender']['group']['id'])
                        # 如果不匹配，就找相似问题的答案
                        if QuestionType == 'Plain' and not SendNum and ReplyConfigDict['cos_match']:
                            SimilarList = []
                            for OneQA in AnswerList:
                                OneMatch = difflib.SequenceMatcher(None, str(QuestionData), str(OneQA['QuestionMsg'])).ratio()
                                if OneMatch >= ReplyConfigDict['cos_match_value']:
                                    MatchDict = {
                                        'Match': OneMatch,
                                        'AnswerList': OneQA['AnswerList']
                                    }
                                    SimilarList.append(MatchDict)
                            if SimilarList:
                                SortSimilarList = self.NewSortListByNumberMagnitude(SimilarList, 'Match', True)
                                AnswerMsgDict = random.choice(SortSimilarList[0]['AnswerList'])
                                AnswerMsg = {
                                    "type": AnswerMsgDict['AnswerMsgType'],
                                    'text': AnswerMsgDict['AnswerMsg']
                                }
                                Timer = random.uniform(
                                    ReplyConfigDict['reply_wait_base_time'] - ReplyConfigDict['reply_wait_float_time'],
                                    ReplyConfigDict['reply_wait_base_time'] + ReplyConfigDict['reply_wait_float_time'])
                                print('Send similar msg wait time: {0} seconds'.format(Timer))
                                time.sleep(Timer)
                                self.SendGroupAnswerMsg(AnswerMsg, MsgDict['sender']['group']['id'])

    # 肥免api模块迁移
    def NewSortListByNumberMagnitude(self, List, Key, IsPositiveSequence):
        # type: (list, str, bool) -> list
        """ *推荐 根据数字排序由Dict元素组成的List--[{}, {}, ...]
        :param List: 需要排序的List
        :param Key: 按List内的哪个Key排序，没有则填None
        :param IsPositiveSequence: 是否为正序
        :return: ResultList(list) 处理完毕之后的list
        """
        def SortKey(Var):
            return Var[Key]
        List.sort(key=SortKey, reverse=not IsPositiveSequence)
        return List

    # 学习，处理msg的json文件，进行问题，答案归类
    def LearningUpdate(self, MsgPath, GroupId, NewMsgDict):
        with open(MsgPath, 'r', encoding='utf-8') as MsgFile:
            Json = MsgFile.read()
            Dict = json.loads(Json)
        MsgList = Dict['MsgList']
        AnswerType, AnswerData = self.ProcessMsgTypeToLearning(NewMsgDict)
        QuestionMsgDict = MsgList[-2]
        QuestionType, QuestionData = self.ProcessMsgTypeToLearning(QuestionMsgDict)

        # 是否有QA文件
        MsgPath = '/XiaoFeimianConfig/Msg/{0}_QA.json'.format(GroupId)
        if os.path.exists(MsgPath):
            # 直接读取文件
            with open(MsgPath, 'r', encoding='utf-8') as QAFile:
                QAFileDict = json.loads(QAFile.read())
        else:
            QAFileDict = {
                'QAList': []
            }

        # 是否有对应消息问题
        Num = 0
        for OneQA in QAFileDict['QAList']:
            if OneQA['QuestionMsg'] == QuestionData and OneQA['QuestionMsgType'] == QuestionType:
                Num += 1
                AnswerDict = {
                    'AnswerMsg': AnswerData,
                    'AnswerMsgType': AnswerType
                }
                AnswerList = OneQA['AnswerList']
                AnswerList.append(AnswerDict)
                OneQA['AnswerList'] = AnswerList
        if not Num:
            QADict = {
                'QuestionMsg': QuestionData,
                'QuestionMsgType': QuestionType,
                # 直接append这个就相当于加权重了
                'AnswerList': [
                    {
                        'AnswerMsg': AnswerData,
                        'AnswerMsgType': AnswerType
                    }
                ]
            }
            QAFileDict['QAList'].append(QADict)
        # 写入新的QAList
        with open(MsgPath, 'w', encoding='utf-8') as QAFile:
            json.dump(QAFileDict, QAFile, indent=4, ensure_ascii=False)

    # 处理消息类型以用于学习
    def ProcessMsgTypeToLearning(self, MsgDict):
        TypeList = ['Plain', 'Image', 'Face', 'Voice']
        MsgType = MsgDict['messageChain'][-1]['type']
        if MsgType in TypeList:
            MsgData = False
            if MsgType == 'Plain':
                MsgData = MsgDict['messageChain'][-1]['text']
            if MsgType == 'Image' or MsgType == 'Voice':
                MsgData = MsgDict['messageChain'][-1]['url']
            if MsgType == 'Face':
                MsgData = MsgDict['messageChain'][-1]['faceId']
            return MsgType, MsgData
        else:
            print('不属于记录类型')
            return False, False


    def SendGroupAnswerMsg(self, AnswerMsg, GroupId):
        MsgList = [AnswerMsg]
        Description = self.Config['dfm:chat_learning']['description']
        key, host, port, qq, session = Description['key'], Description['host'], Description['port'], Description['qq'], Description['session']
        Data = {
          "sessionKey": session,
          "target": GroupId,
          "messageChain": MsgList
        }
        Url = self.PostUrl('sendGroupMessage')
        Result = r.request('post', Url, json=Data)
        if Result:
            Result = json.loads(Result.text)
            if Result['code'] == 0:
                print('Send Answer Msg')
            else:
                print('Send Answer Msg Failed')
        else:
            print('Send Answer Msg Failed')

    def TestAndCreateFolder(self, Path):
        folder = os.path.exists(Path)
        if not folder:
            os.makedirs(Path)

