from mullvadaccount import getAccount, getExpiration, getPorts
from datetime import timedelta, datetime
from utils import loadconfig


name = "mullvadbot"

config = loadconfig()
accountnumber = config['Mullvad']['MullvadAccount']

authorized_browser = getAccount(accountnumber)
expired = getExpiration(authorized_browser)

if expired < datetime.now():
    if expired < (datetime.now() + timedelta(days=5)) and expired != datetime(2001, 1, 1):
        # Checking against hardcoded value to be sure
        print('about to expire')
    else:
        print('expired')
else:
    print('valid')





