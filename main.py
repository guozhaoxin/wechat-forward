#encoding:utf-8

from typing import List
import sys

import log
from business.forward import forward
from business.query import queryGroup,queryUser

QUERYG = '--group'
QUERYU = '--user'
FORWARD = '--forward'

def show_help():
    msg = '''
        本代码用来处理微信的自动化转发事务，支持如下模式：
        模式 1，只打印帮助手册，并立马退出进程。
            或者使用 -h --help，也同样如此。
            python ./main.py
            python ./main.py -h
            python ./main.py --help
        
        模式 2，群消息监听转发模式，只要指定参数为 --forward，此时进程会按照给定的规则进行消息转发，转发规则请修改 config/
            python ./main --forward
        
        模式 3，查询组模式，根据组名称查询组 id
            python ./main --group                      #查出所有能查到的组 id，微信比较尴尬，只能列出部分组，如果要看的组不存在，可以先向那个组中发条消息
            python ./main --group 大学同学              #查出群名以 "大学同学" 开头的群信息
            python ./main --group 大学同学 高中同学       #查出群名以 "大学同学" 或者 "高中同学" 开头的群信息，可以指定多个，会将所有满足的都列出来
        
        模式 4，查询用户模式，根据用户名称查询用户信息
            python ./main --user                      #查出所有能查到的用户信息
            python ./main --user wgc                  #查出用户名或者备注名以 "wgc" 开头的用户信息
            python ./main --user wgc 田锐              #查出用户名或者备注名以 "wgc" 或者 "田锐" 开头的用户信息，可以指定多个，会将所有满足的都列出来

    '''
    log.info(msg)

def parse(commands: List[str]):
    log.info("commands are: {}".format(commands))
    if len(commands) <= 1:
        show_help()
    elif len(commands) == 2:
        com = commands[1].lower()
        if com == '-h' or com == '--help':
            show_help()
            exit(0)
        elif com not in (FORWARD,QUERYG,QUERYU):
            log.fatal("无法识别的参数: {}".format(commands[1]))
            show_help()
            exit(1)
        if com == FORWARD:
            forward("./config/config.yml")
        elif com == QUERYU:
            queryUser([])
        else:
            queryGroup([])

    else:
        com = commands[1].lower()
        args = [] if len(commands) == 2 else commands[2:]
        if com != QUERYG and com != QUERYU:
            log.fatal("无法识别的参数: {}".format(commands[1]))
            show_help()
            exit(1)
        if com == QUERYU:
            queryUser(args)
        else:
            queryGroup(args)


if __name__ == '__main__':
    parse(sys.argv)