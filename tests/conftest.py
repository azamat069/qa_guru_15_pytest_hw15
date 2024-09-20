import pytest
from selene import browser


@pytest.fixture(scope="function", params=[(1280, 1024), (1440, 900), (414, 896)],
                ids=['1280x1024', '1440x900', 'Iphone XR'])
def browser_management(request):
    browser.config.base_url = 'https://github.com'
    param_width, param_height = request.param
    browser.config.window_width = param_width
    browser.config.window_height = param_height
    if param_width >= 1010:
        return 'desktop'
    else:
        return 'mobile'

    browser.quit()


@pytest.fixture(scope="function", params=[(414, 896), (360, 740), (344, 882)],
                ids=['Iphone XR', 'Samsung Galaxy S8+', 'Galaxy Z Fold 5'])
def browser_mobile(request):
    browser.config.base_url = 'https://github.com'
    param_width, param_height = request.param
    browser.config.window_width = param_width
    browser.config.window_height = param_height
    yield
    browser.quit()


@pytest.fixture(scope="function", params=[(1280, 1024), (1440, 900), (1366, 768)],
                ids=['1280x1024', '1440x900', '1366x768'])
def browser_desktop(request):
    browser.config.base_url = 'https://github.com'
    param_width, param_height = request.param
    browser.config.window_width = param_width
    browser.config.window_height = param_height
    yield
    browser.quit()
