import mechanicalsoup
import collections
from bs4 import BeautifulSoup
from datetime import timedelta, datetime
from utils import log


def startMullvad(config):
    accountnumber = config['Mullvad']['MullvadAccount']
    Mullvad = collections.namedtuple('Mullvad', ['status', 'authorized_browser', 'expiredate'])
    Mullvad.authorized_browser = getAccount(accountnumber)
    expired = getExpiration(Mullvad.authorized_browser)
    Mullvad.expiredate = expired

    if expired < datetime.now():
        if expired < (datetime.now() + timedelta(days=5)) and expired != datetime(2001, 1, 1):
            # Checking against hardcoded value to be sure
            Mullvad.status = 'aboutexpire'
        else:
            Mullvad.status = 'expired'
    elif expired > datetime.now():
        Mullvad.status = 'valid'
    else:
        Mullvad.status = 'error'
    log('Mullvad configuration loaded.', 'info')
    return Mullvad


def getAccount(accountnumber):
    browser = mechanicalsoup.StatefulBrowser()
    browser.open("https://mullvad.net/en/account/")
    browser.select_form('form[action="/en/account/auth/"]')
    browser["account_number"] = accountnumber
    browser.submit_selected()
    return browser


def getExpiration(authorized_browser):
    authorized_browser.open("https://mullvad.net/en/account/")
    page = str(authorized_browser.get_current_page())
    soup = BeautifulSoup(page, 'html.parser')
    try:
        expire = datetime.strptime(soup.find('h4', attrs={'class': 'balance-header'}).text.strip().split('\n')[0]
                                   .split(': ', 1)[-1], '%d %B %Y')
        return expire
    except:
        expire = datetime(2001, 1, 1)  # Hardcode a value just to pass its results.
        return expire


def getPorts(authorized_browser):
    authorized_browser.open("https://mullvad.net/en/account/")
    print(authorized_browser.get)
    # TODO: Correctly implement ports


def getRenewAddress(authorized_browser):
    authorized_browser.open("https://mullvad.net/en/account/")
    print(authorized_browser.get)
    # TODO: Correctly implement bitcoin address get
