from telegram.ext import CommandHandler
from enum import Enum
import commands


def registerhandler(dispatcher):
    for c in Commands:
        handler_proxy = CommandHandler(c.value, getattr(commands, c.value))
        dispatcher.add_handler(handler_proxy)

class Commands(Enum):
    start = "start"
    status = "status"