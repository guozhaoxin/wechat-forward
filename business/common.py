# encoding:utf-8
__author__ = 'gold'

import itchat

import log

USERNAME = "UserName"
NICKNAME = "NickName"
REMARKkNAME = "RemarkName"

log.info("显示二维码准备登录")
itchat.auto_login(True)
log.info("登录成功")