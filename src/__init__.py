from mullvadaccount import getAccount, getExpiration, getPorts
from datetime import timedelta, datetime
from utils import loadconfig


name = "mullvadbot"

config = loadconfig()
accountnumber = config['Mullvad']['MullvadAccount']

authorized_browser = getAccount(accountnumber)
expired = getExpiration(authorized_browser)

if expired < datetime.now():
    print('expired')
if expired < (datetime.now() + timedelta(days=5)):
    print('about to expire')
else:
    print('valid')





