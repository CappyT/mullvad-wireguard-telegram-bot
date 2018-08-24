from mullvadaccount import startMullvad
from utils import loadconfig
from telegram.ext import Updater
from utils import log
from handlerproxy import handlerproxy
import vars
import i18n
import os


name = "mullvadbot"
vars.init()
config = loadconfig()
log('starting...', 'info')
i18n.load_path.append('..' + os.sep + 'translations')
i18n.set('fallback', 'en')
vars.locale = config['TelegramBot']['Locale']
if vars.locale == '':
    i18n.set('fallback', 'en')
    vars.locale = 'en'
else:
    i18n.set('locale', vars.locale)
log('Locale loaded', 'info')


if config['Mullvad']['Active'] == '1':
    vars.vpn = startMullvad(config)

updater = Updater(token=config['TelegramBot']['Token'])
dispatcher = updater.dispatcher
handlerproxy(dispatcher)

if config['TelegramBot']['Enabled'] == '1':
    updater.start_polling()
