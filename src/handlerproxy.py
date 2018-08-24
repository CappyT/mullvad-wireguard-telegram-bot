from enum import Enum
from telegram.ext import CommandHandler
import commands
from utils import log


def handlerproxy(dispatcher):
    for c in Commands:
        handler_proxy = CommandHandler(c.value, getattr(commands, c.value))
        dispatcher.add_handler(handler_proxy)
        log('added: ' + c.value, 'info')


class Commands(Enum):
    start = "start"
    status = "status"
