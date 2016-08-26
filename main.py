import httptask
import filetask


try:
    defaultvalue = filetask.getdefaultvalue()
    # print(defaultvalue)
    appid = defaultvalue[0].strip()
    appsecret = defaultvalue[1]
    # print(appid, appsecret)
except FileNotFoundError:
    print('Default file not found, please input default value.')
    appid = input('AppID: ')
    appsecret = input('AppSecret: ')
    filetask.setdefaultvalue(appid, appsecret)
package = httptask.getaccesstoken(appid, appsecret)
if not httptask.getaccesstoken(appid, appsecret):
    print('Invalid AppID or AppSecret.')
    exit(0)
else:
    accesstoken = package
    print('Successfully grabbed access token.')
    # print(accesstoken)

'''MENU
print()
print('1. Get WeChat Server IP')
'''

iptables = httptask.getwechatserverid(accesstoken)
for ip in iptables:
    print(ip.replace('/', ' Port:'))
