# encoding:utf-8
__author__ = 'gold'

from business.config import loadConfig
import log
import time

import itchat
from itchat.content import TEXT,NOTE,SHARING,PICTURE,MAP

def init():
    log.info('初始化监听转发规则')

startTime = int(time.time())

CONTENT = "Content"
ACTUALNICKNAME = "ActualNickName"
ACTUALUSERNAME = "ActualUserName"
ISAT = "IsAt"
CREATETIME = "CreateTime"
USER = "User"
NICKNAME = "NickName"
MSGTYPE = 'MsgType'
FROMUSERNAME = 'FromUserName'

SRCGROUP = "srcGroup"
DSTGROUP = "dstGroup"
DUSER = "user"
DNAME = "name"
DID = "id"

def ifNeedToForward(msg,conf):
    srcGroupId = msg[FROMUSERNAME]
    for item in conf[SRCGROUP]:
        did = item[DID]
        if srcGroupId == did:
            realUserId = msg[ACTUALUSERNAME] # 获取实际用户 id
            for j in conf[DUSER]:
                if j[DID] == realUserId:
                    return True
    return False

def showMsg(msg):
    log.info('-----------------------')
    log.info('内容是: {}'.format(msg[CONTENT]))
    log.info('发言人为: {}'.format(msg[ACTUALNICKNAME]))
    log.info('实际用户id为:{}'.format(msg[ACTUALUSERNAME]))
    log.info('是否@：{}'.format(msg[ISAT]))
    log.info(msg[USER][NICKNAME])
    log.info(msg[USER][USER])
    log.info('创建时间为', msg[CREATETIME])
    groupName = msg[USER][NICKNAME]
    groupId = msg[USER][USER]
    log.info("群名为 {} 群 id 为 {}".format(groupName,groupId))
    log.info('-----------------------')

def sendMsg(msg, conf):
    srcId = msg[FROMUSERNAME]
    for item in conf:
        if item[DSTGROUP][DID] == srcId:
            continue
        log.info("从 {} 转发消息到:{} {}".format(srcId,item[DSTGROUP][DID],item[DSTGROUP][DNAME]))
        itchat.send_raw_msg(msg[MSGTYPE], msg[CONTENT],item[DSTGROUP][DID])

def checkIfValid(conf):
    src = conf[SRCGROUP]
    dst = conf[DSTGROUP]
    for item in src:
        for j in dst:
            if item[DID] == j[DID]:
                log.error("id 同时在源和目标中出现，会出现暴风！请修改后重试")
                log.error("id={} srcGroupName={} dstGroupName={}".format(item[DID],item[DNAME],j[DNAME]))
                exit(1)

def forward(configFile):
    log.info('启动群消息监听及转发模式,配置文件为 {}'.format(configFile))
    conf = loadConfig(configFile)
    log.info("检查配置有效性")
    checkIfValid(conf)
    log.info('配置为 {}'.format(conf))
    log.info('注册监听函数')
    
    @itchat.msg_register([TEXT,NOTE,SHARING,PICTURE,MAP], isGroupChat=True)
    def forward_group_info(msg):
        if int(msg[CREATETIME]) - startTime <= 10:
            log.info('消息比较早，放弃转发')
        if not ifNeedToForward(msg,conf):
            log.info("不需要转发")
            return

        showMsg(msg)
        sendMsg(msg, conf)

    
    log.info("进入监听服务")
    itchat.run()