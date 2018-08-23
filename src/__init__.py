from mullvadaccount import startMullvad
from utils import loadconfig
from telegram.ext import Updater
from handlerproxy import registerhandler
import logging

name = "mullvadbot"
config = loadconfig()

updater = Updater(token=config['TelegramBot']['Token'])
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime) - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
registerhandler(dispatcher)


if config['Mullvad']['Active'] == '1':
    vpn = startMullvad(config)
if config['TelegramBot']['Enabled'] == '1':
    updater.start_polling()