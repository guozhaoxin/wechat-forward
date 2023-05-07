# encoding:utf-8
__author__ = 'gold'

from business.common import REMARKkNAME,NICKNAME,USERNAME
import log

import itchat

def queryGroup(args):
    '''
    查询组信息
    :param args:
    :return:
    '''
    log.info("查询组信息, 查询的组为: {}".format(str(args)))
    groupList = itchat.get_chatrooms()
    log.info('一共有 {} 组'.format(len(groupList)))
    log.info("组信息如下")
    for item in groupList:
        try:
            log.info(item)
        except Exception as e:
            log.error("打印失败 {}".format(e))
    log.info(groupList)
    args = set(args)
    for item in groupList:
        nickName = item[NICKNAME]
        groupId = item[USERNAME]
        for a in args:
            if nickName.startswith(a):
                log.info("{} 名称符合 {}, 组 id 为{}".format(nickName,a,groupId))
                log.info('目标完整信息如下')
                log.info(item)


def queryUser(args):
    '''
    查询用户信息
    :param args:
    :return:
    '''
    log.info("查询用户信息, 查询的用户为: {}".format(str(args)))
    log.info("获取所有用户信息")
    userList = itchat.get_friends()
    log.info('一共有 {} 好友'.format(len(userList)))
    yourSelf = userList[0]
    log.info("自己的信息为: {}".format(str(yourSelf)))
    log.info("自己的 UserName(即 id) 为 {}".format(yourSelf[USERNAME]))
    if len(args) == 0:
        log.info("好友信息如下")
        for u in userList:
            try:
                log.info(u)
            except Exception as e:
                log.error("打印错误:{}".format(e))
        return
    args = set(args)
    for item in userList:
        nickName = item[NICKNAME]
        remarkName = item[REMARKkNAME]
        userId = item[USERNAME]
        for a in args:
            if nickName.startswith(a):
                log.info("{} 昵称符合 {}, 用户 id 为{}".format(nickName,a,userId))
                log.info('目标完整信息如下')
                try:
                    log.info(item)
                except Exception as e:
                    log.error("打印错误:{}".format(e))
            elif remarkName.startswith(a):
                log.info("{} 备注符合 {},用户 id 为 {}".format(remarkName,a,userId))
                log.info('目标完整信息如下')
                try:
                    log.info(item)
                except Exception as e:
                    log.error("打印错误:{}".format(e))
