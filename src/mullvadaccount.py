import mechanicalsoup
from bs4 import BeautifulSoup
from datetime import datetime

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
    expire = datetime.strptime(soup.find('h4', attrs={'class': 'balance-header'}).text.strip().split('\n')[0]
                               .split(': ', 1)[-1], '%d %B %Y')
    return expire


def getPorts(authorized_browser):
    authorized_browser.open("https://mullvad.net/en/account/")
    print(authorized_browser.get)
    # TODO: Correctly implement ports
