# 基本说明
- 基于Mirai及mirai-api-http制作的QQ学习群友说话机器人。

- 灵感来源及基本参考来源于：[ChatLearning(Github)](https://github.com/Nana-Miko/ChatLearning)

- 项目命名为：小肥免 (XiaoFeimian)，因为之前一直是把这个QQ当机器人用`ChatLearning`放在我的`MC模组交流群`里面聊天的，但是昨天不知道为什么我自己用`ChatLearning`效果一直很怪，于是就花了`5`个小时沿用了我写的我的世界`自主学习机器人`模组的原理自己写了一个，因此项目本身比较简单，也没有很完善的对未来拓展功能提前写好底层~

- 简单原理介绍：监听获取群消息(当然后面也可以做好友消息，但是感觉没那么有意思，就只做了群消息)，上一个消息作为问题，下一个消息作为答案来进行记录，只要是相同的问题，答案都重复记录以增加权重(其实可以直接设置一个`times`但是我好累！)，这样就可以进行匹配群友的对话来给出答案回复了~

# 安装
1. 安装[Mirai(Github)](https://github.com/mamoe/mirai)
2. 前往`Release`下载`XiaoFeimian.exe`程序
3. 前往[mirai-api-http(Github)](https://github.com/project-mirai/mirai-api-http/tree/master)安装**2.10.0**版本的的`mirai-api-http`，高版本可能会有api变动导致`小肥免(XiaoFeimian)`无法使用。
4. 设置`mirai-api-http`的配置文件`setting.yml`，当然你可以参考我目前自己用的这个设置：
```
   ## 配置文件中的值，全为默认值

## 启用的 adapter, 内置有 http, ws, reverse-ws, webhook
adapters:
  - http
  - ws

## 是否开启认证流程, 若为 true 则建立连接时需要验证 verifyKey
## 建议公网连接时开启
enableVerify: false
verifyKey: 1234567890

## 开启一些调试信息
debug: false

## 是否开启单 session 模式, 若为 true，则自动创建 session 绑定 console 中登录的 bot
## 开启后，接口中任何 sessionKey 不需要传递参数
## 若 console 中有多个 bot 登录，则行为未定义
## 确保 console 中只有一个 bot 登录时启用
singleMode: true

## 历史消息的缓存大小
## 同时，也是 http adapter 的消息队列容量
cacheSize: 4096

## adapter 的单独配置，键名与 adapters 项配置相同
adapterSettings:
  ## 详情看 http adapter 使用说明 配置
  http:
    host: 0.0.0.0
    port: 23750
    cors: ["*"]
  
  ## 详情看 websocket adapter 使用说明 配置
  ws:
    host: localhost
    port: 8080
    reservedSyncId: -1
```
5. 把`XiaoFeimian.exe`程序放在你容易找到的地方，双击打开然后关闭，配置文件将会生成在程序所在位置的根目录下的`XiaoFeimianConfig`文件夹。例如：`XiaoFeimian.exe`程序放在`D:\DaFeimian\Robot\dfm520\...`下，第一次打开后，配置文件就会在`D:\XiaoFeimianConfig\...`下。**注意：**程序是多线程运行的，可能关闭之后会卡到线程，需要在任务管理器中查看是否仍在后台运行，然后关闭掉！
6. 修改`小肥免(XiaoFeimian)`的配置文件`config.json`：
   - format_version: 版本号
   - key: 不用填
   - host: 地址，对应mirai-api-http-2.10.0的配置文件http里的那个host
   - port: 端口，对应mirai-api-http-2.10.0的配置文件http里的那个port
   - qq: 你的QQ号，对应mirai-api-http-2.10.0的配置文件http里的那个port
   - session: 不用填，对应mirai-api-http-2.10.0的配置文件singleMode设置为true
   - dfm:learning_list: 学习群聊的群号列表
   - dfm:reply_list: 回复群聊的群号列表
   - dfm:chance: 回复概率(0~1)
   - dfm:cos_match: 是否进行相似度计算以寻找答案(bool)
   - dfm:cos_match_value: 相似度计算达到多少就匹配答案(0~1)
   - dfm:reply_wait_base_time: 回复行为的基础等待时间
   - dfm:reply_wait_float_time: 回复行为的浮动时间(+-)
   你也可以在`XiaoFeimian.exe`程序里输入`config help`来查看这些信息。示范：
```json
{
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
                "value": [
                    766176115,
                    687577485,
                    456370680,
                    212048505,
                    180568043
                ]
            },
            "dfm:reply_list": {
                "value": [
                    766176115,
                    687577485,
                    456370680,
                    598874379,
                    212048505,
                    180568043
                ]
            },
            "dfm:reply": {
                "chance": 1.0,
                "cos_match": true,
                "cos_match_value": 0.5,
                "reply_wait_base_time": 1.0,
                "reply_wait_float_time": 0.5
            }
        }
    }
}
```
7. 修改完毕之后，保证`Mirai`正常运行以及登录QQ，然后打开`XiaoFeimian.exe`程序就可以辣！看到这个就表示连接成功~
   ![image](https://github.com/DaFeimian/XiaoFeimian/assets/135980226/871521ff-7fd8-4295-b591-c752fc4d0877)
