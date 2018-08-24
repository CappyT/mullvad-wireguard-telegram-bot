import configparser
import os
import logging
import vars


def loadconfig():
    global config
    config = configparser.ConfigParser()

    if not os.path.exists('config.ini'):
        with open('config.ini', 'w') as configfile:
            config['Mullvad'] = {'MullvadAccount': '123456789'}
            config['Mullvad'] = {'Active': '1'}
            config['TelegramBot'] = {'Token': 'https://t.me/token/api', 'PoolInterval': '30', 'Enabled': '1',
                                     'Locale': 'it', 'Logging': 'info'}
            config.write(configfile)
            logging.info('write config file')
            return config
    else:
        config.read('config.ini')
        logging.info('read config file')
        return config


def log(string, loglevel):
    logger = logging.getLogger('logger')
    Log = logging.StreamHandler(logger)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    Log.setFormatter(formatter)
    logger.addHandler(Log)
    global config
    # level = logging.getLevelName((config['TelegramBot']['Logging']).upper())
    logger.setLevel(config['TelegramBot']['Logging'].upper())

    if loglevel.lower() == 'info':
        logging.info(string)
    elif loglevel.lower() == 'debug':
        logging.debug(string)
    elif loglevel.lower() == 'warning':
        logging.warning(string)
    elif loglevel.lower() == 'fatal':
        logging.fatal(string)
    elif loglevel.lower() == 'critical':
        logging.critical(string)
    elif loglevel.lower() == 'error':
        logging.error(string)
