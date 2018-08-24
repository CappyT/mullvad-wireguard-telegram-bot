import configparser
import os
import logging


def loadconfig():
    config = configparser.ConfigParser()

    if not os.path.exists('config.ini'):
        with open('config.ini', 'w') as configfile:
            config['Mullvad'] = {'MullvadAccount': '123456789'}
            config['Mullvad'] = {'Active': '1'}
            config['TelegramBot'] = {'Token': 'https://t.me/token/api', 'PoolInterval': '30', 'Enabled': '1',
                                     'Locale': 'it'}
            config.write(configfile)
            logging.info('write config file')
            return config
    else:
        config.read('config.ini')
        logging.info('read config file')
        return config


def log(string, loglevel):
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level = logging.DEBUG)
    if loglevel == 'info':
        logging.info(string)
    elif loglevel == 'debug':
        logging.debug(string)
    elif loglevel == 'warning':
        logging.warning(string)
    elif loglevel == 'fatal':
        logging.fatal(string)
    elif loglevel == 'critical':
        logging.critical(string)
    elif loglevel == 'error':
        logging.error(string)
