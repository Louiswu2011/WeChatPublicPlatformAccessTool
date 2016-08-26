from os import getcwd


def setdefaultvalue(appid, appsecret):
    filedir = getcwd() + '\\default'
    with open(filedir, 'w') as defaultfile:
        defaultfile.writelines(appid + '\n')
        defaultfile.writelines(appsecret)
    return True


def getdefaultvalue():
    filedir = getcwd() + '\\default'
    try:
        with open(filedir, 'r') as defaultfile:
            defaultvalue = defaultfile.readlines()
            return defaultvalue
    except FileNotFoundError:
        raise
