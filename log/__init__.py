# encoding:utf-8
__author__ = 'gold'

import logging

def init_log():
    '''
    初始化日志
    :return:
    '''
    LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
    logging.basicConfig(filename='wechat.log', level=logging.DEBUG, format=LOG_FORMAT)

init_log()

def p(func):
    def inner(msg,*args,**kwargs):
        print(msg,*args,**kwargs)
        return func(msg,*args,**kwargs)
    return inner

@p
def info(msg, *args, **kwargs):
    # logging.info(msg,*args,**kwargs)
    pass

@p
def debug(msg, *args, **kwargs):
    # logging.debug(msg,*args,**kwargs)
    pass

@p
def warn(msg, *args, **kwargs):
    # logging.warning(msg,*args,**kwargs)
    pass

@p
def error(msg, *args, **kwargs):
    # logging.error(msg,*args,**kwargs)
    pass

@p
def fatal(msg, *args, **kwargs):
    # logging.fatal(msg,*args,**kwargs)
    pass
