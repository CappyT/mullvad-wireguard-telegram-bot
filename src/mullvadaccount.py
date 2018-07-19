import mechanicalsoup


def getAccount(accountnumber):
    browser = mechanicalsoup.StatefulBrowser()
    browser.open("https://mullvad.net/account/")
    browser.select_form('form[action="/en/account/auth/"]')
    browser["account_number"] = accountnumber
    browser.submit_selected()
    return browser
