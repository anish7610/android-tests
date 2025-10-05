from account_page import AccountPage


def test_accounts(android_driver, login):
    account_page = AccountPage(android_driver)
    account_types = account_page.get_account_type()

    expected_account_types = ["Checking", "Savings"]

    for idx, account in enumerate(account_types):
        assert expected_account_types[idx] in account.text
