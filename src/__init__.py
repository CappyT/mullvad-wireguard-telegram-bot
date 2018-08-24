from mullvadaccount import startMullvad
from utils import loadconfig
from telegram.ext import Updater
from utils import log
from handlerproxy import handlerproxy
import vars
import i18n
import os


name = "mullvadbot"
log('starting...', 'info')
vars.init()
config = loadconfig()
i18n.load_path.append('..' + os.sep + 'translations')
#i18n.set('fallback', 'en')
vars.locale = config['TelegramBot']['Locale']
i18n.set('locale', vars.locale)

if config['Mullvad']['Active'] == '1':
    vars.vpn = startMullvad(config)

updater = Updater(token=config['TelegramBot']['Token'])
dispatcher = updater.dispatcher
handlerproxy(dispatcher)

if config['TelegramBot']['Enabled'] == '1':
    updater.start_polling()
