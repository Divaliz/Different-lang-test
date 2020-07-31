def test_button_presence(browser):
    browser.implicitly_wait(50)
    button = browser.find_element_by_css_selector("button.btn-add-to-basket").text
    assert button == "Ajouter au panier"
