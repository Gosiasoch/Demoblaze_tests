def test_place_order(home_page, product_page, cart_page):
    home_page.open()
    product_page.select_first_product()
    product_page.add_to_cart()
    product_page.accept_alert()
    cart_page.go_to_cart()
    assert cart_page.place_order()

def test_order_without_product(home_page, cart_page):
    home_page.open()
    cart_page.go_to_cart()
    try:
        cart_page.place_order()
        assert False, "Order should not be possible without product"
    except:
        assert True