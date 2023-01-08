import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service


# Инициализация драйвера
@pytest.fixture
def driver():
    service = Service(executable_path='/Users/tigrankarapetian/PycharmProjects/Sprint_4/geckodriver')
    driver = webdriver.Firefox(service=service)
    driver.maximize_window()
    driver.get("https://qa-scooter.praktikum-services.ru/")
    yield driver
    driver.quit()
