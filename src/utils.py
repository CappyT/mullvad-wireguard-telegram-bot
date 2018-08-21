import configparser
import os


def loadconfig():
    config = configparser.ConfigParser()

    if not os.path.exists('config.ini'):
        with open('config.ini', 'w') as configfile:
            config['Mullvad'] = {'MullvadAccount': '123456789'}
            config['Mullvad'] = {'Active': '1'}
            config['TelegramBot'] = {'Token': 'https://t.me/token/api', 'PoolInterval': '30', 'Enabled': 'false'}
            config.write(configfile)
            print('write')
            return config
    else:
        config.read('config.ini')
        print('read')
        return config