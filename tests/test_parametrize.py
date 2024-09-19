import pytest
from selene import browser, have

desktop = pytest.mark.parametrize("browser_management", [(1920, 1080)], ids=['1920x1080'], indirect=True)
mobile = pytest.mark.parametrize("browser_management", [(412, 915)], ids=['Pixel 7'], indirect=True)


@desktop
def test_desktop_parametrize(browser_management):
    browser.open('/')
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.element('.auth-form-header').should(have.text('Sign in to GitHub'))


@mobile
def test_mobile_parametrize(browser_management):
    browser.open('/')
    browser.element('.HeaderMenu-link.HeaderMenu-button').click()
    browser.element('.auth-form-header').should(have.text('Sign in to GitHub'))
