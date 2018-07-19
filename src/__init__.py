from mullvadaccount import getAccount
from bs4 import BeautifulSoup
from utils import loadconfig


name = "mullvadbot"

config = loadconfig()
accountnumber = config['Mullvad']['MullvadAccount']

browser = getAccount(accountnumber)
page = str(browser.get_current_page())

soup = BeautifulSoup(page, 'html.parser')

expire = soup.find('h4', attrs={'class': 'balance-header'}).text.strip()
print(expire)
