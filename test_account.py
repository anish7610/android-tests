from account_page import AccountPage
from appium.webdriver.common.appiumby import AppiumBy


def test_accounts(driver, login):
    
    account_page = AccountPage(driver)

    accounts_listview = account_page.get_accounts_listview()

    account_types = accounts_listview.find_elements(AppiumBy.ID, account_page.account_type_textfield)

    expected_account_types = ["Checking", "Savings"]

    for idx, account in enumerate(account_types):
        assert expected_account_types[idx] in account.text
