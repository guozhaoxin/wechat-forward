# encoding:utf-8
__author__ = 'gold'

import log
import yaml

def loadConfig(ymlFile):
    file = open(ymlFile, 'r', encoding="utf-8")
    file_data = file.read()
    file.close()
    data = yaml.load(file_data)
    log.info("配置信息是: {}".format(data))
    return data

if __name__ == '__main__':
    ymlFile = '../config/config.yml'
    data = loadConfig(ymlFile)
    print(data)
