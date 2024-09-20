import pytest
from selene import browser, have


def test_desktop_skip_mobile_screen(browser_management):
    if browser_management == 'mobile':
        pytest.skip(reason='Размер окна не соответствует desktop')

    browser.open('/')
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.element('.auth-form-header').should(have.text('Sign in to GitHub'))


def test_mobile_skip_desktop_screen(browser_management):
    if browser_management == 'desktop':
        pytest.skip(reason='Размер окна не соответствует mobile')

    browser.open('/')
    browser.element('.HeaderMenu-link.HeaderMenu-button').click()
    browser.element('.auth-form-header').should(have.text('Sign in to GitHub'))
