import allure
from locators.locators_main_page import MainPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class MainPage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Нажать на лого Яндекса')
    def click_yandex_logo(self):
        self.driver.find_element(*MainPageLocators.yandex_logo).click()

    @allure.step('Нажать на лого Самоката')
    def click_scooter_logo(self):
        self.driver.find_element(*MainPageLocators.scooter_logo).click()

    @allure.step('Закрыть сообщение о cookie')
    def click_close_cookie(self):
        self.driver.find_element(*MainPageLocators.cookie_button).click()

    @allure.step('Нажать на кнопку Заказать вверху страницы')
    def click_first_order_button(self):
        self.driver.find_elements(*MainPageLocators.order_button)[0].click()

    @allure.step('Нажать на кнопку Заказать внизу страницы')
    def click_second_order_button(self):
        self.driver.find_elements(*MainPageLocators.order_button)[2].click()

    @allure.step("Раздел Вопросы о важном - Нажать на первый вопрос")
    def click_question_one(self):
        last_question = self.driver.find_element(*MainPageLocators.question_eight)
        self.driver.execute_script("arguments[0].scrollIntoView();", last_question)
        element = WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.question_one))
        element.click()

    @allure.step("Раздел Вопросы о важном - Ответ на первый вопрос")
    def get_answer_one(self, driver):
        return WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(*MainPageLocators.answer_one)).text

    @allure.step("Раздел Вопросы о важном - Нажать на второй вопрос в списке")
    def click_question_two(self):
        last_question = self.driver.find_element(*MainPageLocators.question_eight)
        self.driver.execute_script("arguments[0].scrollIntoView();", last_question)
        element = WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.question_two))
        element.click()

    @allure.step("Раздел Вопросы о важном - Ответ на второй вопрос")
    def get_answer_two(self, driver):
        return WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.answer_two)).text

    @allure.step("Раздел Вопросы о важном - Нажать на третий вопрос в списке")
    def click_question_three(self):
        last_question = self.driver.find_element(*MainPageLocators.question_eight)
        self.driver.execute_script("arguments[0].scrollIntoView();", last_question)
        element = WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.question_three))
        element.click()

    @allure.step("Раздел Вопросы о важном - Ответ на третий вопрос")
    def get_answer_three(self, driver):
        return WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.answer_three)).text

    @allure.step("Раздел Вопросы о важном - Нажать на четвертый вопрос в списке")
    def click_question_four(self):
        last_question = self.driver.find_element(*MainPageLocators.question_eight)
        self.driver.execute_script("arguments[0].scrollIntoView();", last_question)
        element = WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.question_four))
        element.click()

    @allure.step("Раздел Вопросы о важном - Ответ на четвертый вопрос")
    def get_answer_four(self, driver):
        return WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.answer_four)).text

    @allure.step("Раздел Вопросы о важном - Нажать на пятый вопрос в списке")
    def click_question_five(self):
        last_question = self.driver.find_element(*MainPageLocators.question_eight)
        self.driver.execute_script("arguments[0].scrollIntoView();", last_question)
        element = WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.question_five))
        element.click()

    @allure.step("Раздел Вопросы о важном - Ответ на пятый вопрос")
    def get_answer_five(self, driver):
        return WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.answer_five)).text

    @allure.step("Раздел Вопросы о важном - Нажать на шестой вопрос в списке")
    def click_question_sixth(self,driver):
        last_question = driver.find_element(*MainPageLocators.question_eight)
        driver.execute_script("arguments[0].scrollIntoView();", last_question)
        element = WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.question_sixth))
        element.click()

    @allure.step("Раздел Вопросы о важном - Ответ на шестой вопрос")
    def get_answer_sixth(self, driver):
        return WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.answer_sixth)).text

    @allure.step("Раздел Вопросы о важном - Нажать на седьмой вопрос в списке")
    def click_question_seven(self, driver):
        last_question = driver.find_element(*MainPageLocators.question_eight)
        driver.execute_script("arguments[0].scrollIntoView();", last_question)
        element = WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.question_seven))
        element.click()

    @allure.step("Раздел Вопросы о важном - Ответ на седьмой вопрос")
    def get_answer_seven(self, driver):
        return WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.answer_seven)).text

    @allure.step("Раздел Вопросы о важном - Нажать на восьмой вопрос в списке")
    def click_question_eight(self, driver):
        last_question = driver.find_element(*MainPageLocators.question_eight)
        driver.execute_script("arguments[0].scrollIntoView();", last_question)
        element = WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.question_eight))
        element.click()

    @allure.step("Раздел Вопросы о важном - Ответ на восьмой вопрос")
    def get_answer_eight(self, driver):
        return WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.answer_eight)).text
