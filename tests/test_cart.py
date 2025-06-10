def test_add_product_to_cart(home_page, product_page):
    home_page.open()
    product_page.select_first_product()
    product_page.add_to_cart()
    alert_text = product_page.accept_alert()
    assert "Product added" in alert_text

def test_delete_product_from_cart(home_page, product_page, cart_page):
    home_page.open()
    product_page.select_first_product()
    product_page.add_to_cart()
    product_page.accept_alert()
    cart_page.go_to_cart()
    cart_page.delete_product()
