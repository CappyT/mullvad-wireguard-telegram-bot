import configparser

def loadconfig():
    config = configparser.ConfigParser()
    config['Mullvad'] = {'MullvadAccount': '123456789'}
    config['TelegramBot'] = {'Token': 'https://t.me/token/api', 'PoolInterval': '30', 'Enabled': 'false'}

    try:
        configfile = 'config.ini'
        config.read(configfile)
    except:
        with open('config.ini', 'w') as configfile:
            config.write(configfile)
    return config
