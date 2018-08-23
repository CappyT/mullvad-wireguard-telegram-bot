from vars import vpn


def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Test if it works")
    print(update.message.text.split(' ', 1)[1])

def status(bot, update):
    from __init__ import vpn
    bot.send_message(chat_id=update.message.chat_id, text=vpn.status)
