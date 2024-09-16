import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage

class TestOrderPage:

    @allure.title('Сценарий заказа по кнопке Заказать вверху страницы')
    @allure.description('Позитивный кейс заказа самоката по кнопке Заказать вверху страницы')
    def test_first_order(self, driver):
        main_page = MainPage(driver)
        main_page.click_close_cookie()
        main_page.click_first_order_button()
        order_page = OrderPage(driver)
        order_page.input_name()
        order_page.input_surname()
        order_page.input_address()
        order_page.input_subway_station()
        order_page.input_phone_number()
        order_page.click_next_page_button()
        order_page.set_date()
        order_page.driver.implicitly_wait(4)
        order_page.set_rental_period()
        order_page.click_black_checkbox()
        order_page.set_comment()
        order_page.click_order_button()
        order_page.click_yes_button()
        assert order_page.order_has_been_confirmed_text().startswith('Заказ оформлен')

    @allure.title('Сценарий заказа по кнопке Заказать внизу страницы')
    @allure.description('Позитивный кейс заказа самоката по кнопке Заказать внизу страницы')
    def test_second_order(self, driver):
        main_page = MainPage(driver)
        main_page.click_close_cookie()
        main_page.click_second_order_button()
        order_page = OrderPage(driver)
        order_page.input_name()
        order_page.input_surname()
        order_page.input_address()
        order_page.input_subway_station()
        order_page.input_phone_number()
        order_page.click_next_page_button()
        order_page.set_date()
        order_page.set_rental_period()
        order_page.click_grey_checkbox()
        order_page.click_order_button()
        order_page.click_yes_button()
        assert order_page.order_has_been_confirmed_text().startswith('Заказ оформлен')