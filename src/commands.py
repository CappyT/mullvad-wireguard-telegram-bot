import i18n
from utils import log
import vars
import os


def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Test if it works")
    try:
        log(update.message.text.split(' ', 1)[1], 'info')
    except IndexError:
        log('No input given.', 'info')


def status(bot, update):
    global vpn
    global locale
    string = i18n.t('lang.status.' + vars.vpn.status, date=vars.vpn.expiredate.strftime("%d-%m-%Y"), locale=vars.locale)
    bot.send_message(chat_id=update.message.chat_id, text=string)
