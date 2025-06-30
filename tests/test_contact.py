import pytest

def test_send_contact_message(contact_page):

    contact_page.open_contact_modal()
    contact_page.enter_email("test@example.com")
    contact_page.enter_name("Test User")
    contact_page.enter_message("This is a test message.")
    contact_page.click_send()
    alert_text = contact_page.accept_alert()
    assert "Thanks" in alert_text or "Thank you" in alert_text


def test_send_empty_contact_message(contact_page):
    contact_page.open_contact_modal()
    contact_page.click_send()
    alert_text = contact_page.accept_alert()
    assert "Thanks for the message" in alert_text


def test_close_contact_modal(contact_page):

    contact_page.open_contact_modal()
    contact_page.click_close()
    assert contact_page.is_modal_closed(), "Modal powinien być zamknięty, ale nadal jest widoczny."