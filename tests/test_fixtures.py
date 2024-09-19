from selene import browser, have


def test_desktop(browser_desktop):
    browser.open('/')
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.element('.auth-form-header').should(have.text('Sign in to GitHub'))


def test_mobile(browser_mobile):
    browser.open('/')
    browser.element('.HeaderMenu-link.HeaderMenu-button').click()
    browser.element('.auth-form-header').should(have.text('Sign in to GitHub'))
