from urllib import request
import json


def getaccesstoken(appid, appsecret):
    getpackage = request.urlopen('https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=' + appid + '&secret=' + appsecret)
    receivepackage = getpackage.read()
    receive = receivepackage.decode('utf-8')
    jsonreceive = json.loads(receive)
    try:
        if jsonreceive['errcode'] != '':
            return False
    except KeyError:
        return jsonreceive['access_token']


def getwechatserverid(accesstoken):
    getpackage = request.urlopen('https://api.weixin.qq.com/cgi-bin/getcallbackip?access_token=' + accesstoken)
    receivepackage = getpackage.read()
    receive = receivepackage.decode('utf-8')
    jsonreceive = json.loads(receive)
    try:
        if jsonreceive['errcode'] != '':
            return False
    except KeyError:
        return jsonreceive['ip_list']