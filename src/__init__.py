from mullvadaccount import getAccount
import configparser
from bs4 import BeautifulSoup


name = "mullvadbot"

config = configparser.ConfigParser()
config['Mullvad'] = {'MullvadAccount': '123456789'}
config['TelegramBot'] = {'Token': 'https://t.me/token/api', 'PoolInterval': '30', 'Enabled': 'false'}

try:
    configfile = 'config.ini'
    config.read(configfile)
except:
    with open('config.ini', 'w') as configfile:
        config.write(configfile)


accountnumber = config['Mullvad']['MullvadAccount']

browser = getAccount(accountnumber)
page = str(browser.get_current_page())

soup = BeautifulSoup(page, 'html.parser')

expire = soup.find('h4', attrs={'class': 'balance-header'})
print(expire.text.strip())
