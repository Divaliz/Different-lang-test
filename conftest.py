import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='ru',
                     help="Choose your language: (for example 'fr' or 'en')")


@pytest.fixture(scope="function")
def browser(request):
    browser = webdriver.Chrome()
    language = request.config.getoption("language")
    if language == "fr":
        browser.get("http://selenium1py.pythonanywhere.com/fr/catalogue/coders-at-work_207/")
    elif language == "en":
        browser.get("http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/")
    yield browser
    browser.quit()


# having an option to drag 'language' options from the website and storing them in list would be neat!

# ???
# lang_lst = browser.find_elements_by_css_selector("select > option")
# if language in lang_lst:
#    browser.get(f"http://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/")
# else:
#       raise pytest.UsageError("invalid parameter")
