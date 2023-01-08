import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.locators_order_page import OrderPageLocators



class OrderPage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Ввод имени')
    def input_name(self):
        self.driver.find_elements(*OrderPageLocators.input_name)[0].send_keys('Иван')

    @allure.step('Ввод фамилии')
    def input_surname(self):
        self.driver.find_elements(*OrderPageLocators.input_surname)[1].send_keys('Иванов')

    @allure.step('Ввод адреса')
    def input_address(self):
        self.driver.find_elements(*OrderPageLocators.input_address)[2].send_keys('Москва, улица Вавилова, дом 45')

    @allure.step('Выбор станции метро')
    def input_subway_station(self):
        self.driver.find_element(*OrderPageLocators.input_subway_station).send_keys('Академическая')
        self.driver.find_element(*OrderPageLocators.subway_station_dropdown).click()

    @allure.step('Ввод номера телефона')
    def input_phone_number(self):
        self.driver.find_elements(*OrderPageLocators.input_phone)[3].send_keys('+79111351234')

    @allure.step('Нажать на кнопку Далее')
    def click_next_page_button(self):
        self.driver.find_element(*OrderPageLocators.next_page_button).click()

    @allure.step('Введите дату аренды')
    def set_date(self):
        self.driver.find_elements(*OrderPageLocators.input_date)[0].send_keys('15.01.2023')
        self.driver.find_element(*OrderPageLocators.date_selected).click()

    @allure.step('Выбрать срок аренды')
    def set_rental_period(self):
        self.driver.find_elements(*OrderPageLocators.rental_date_menu).click()
        self.driver.find_element(*OrderPageLocators.rental_date).click()

    @allure.step('Выбрать цвет самоката')
    def click_black_checkbox(self):
        self.driver.find_element(*OrderPageLocators.black_checkbox).click()

    @allure.step('Выбрать другой цвет самоката')
    def click_grey_checkbox(self):
        self.driver.find_element(*OrderPageLocators.grey_checkbox).click()

    @allure.step('Ввести комментарий')
    def set_comment(self):
        self.driver.find_elements(*OrderPageLocators.input_comment).send_keys('Спасибо!')

    @allure.step('Нажать кнопку Заказать')
    def click_order_button(self):
        self.driver.find_element(*OrderPageLocators.order_button).click()

    @allure.step('Сообщение-вопрос о подтверждении заказа')
    def confirmation_message_text(self):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(OrderPageLocators.confirmation_message)).text

    @allure.step('Нажать кнопку Да')
    def click_yes_button(self):
        self.driver.find_element(*OrderPageLocators.confirmation_button).click()

    @allure.step('Сообщение "Заказ оформлен"')
    def order_has_been_confirmed_text(self):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(OrderPageLocators.order_confirmed)).text
