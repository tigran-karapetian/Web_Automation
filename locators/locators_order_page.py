from selenium.webdriver.common.by import By


class OrderPageLocators:

    input_name = [By.XPATH, "//input[contains(@class, 'Input_Responsible__1jDKN')]"]
    input_surname = [By.XPATH, "//input[contains(@class, 'Input_Responsible__1jDKN')]"]
    input_address = [By.XPATH, "//input[contains(@class, 'Input_Responsible__1jDKN')]"]
    input_phone = [By.XPATH, "//input[contains(@class, 'Input_Responsible__1jDKN')]"]
    input_subway_station = [By.CLASS_NAME, 'select-search__input']
    subway_station_dropdown = [By.CLASS_NAME, 'select-search__row']
    next_page_button = [By.XPATH, "//button[contains(text(), 'Далее')]"]
    input_date = [By.XPATH, "//input[contains(@class, 'Input_Responsible__1jDKN')]"]
    date_selected = [By.XPATH, "//div[contains(@class, 'react-datepicker__day--selected')]"]
    rental_date_menu = [By.CLASS_NAME, 'Dropdown-placeholder']
    rental_date = [By.XPATH, './/div[@class="Dropdown-menu"]/div']
    black_checkbox = [By.ID, 'black']
    grey_checkbox = [By.ID, 'grey']
    input_comment = [By.XPATH, "//input[contains(@placeholder, 'Комментарий для курьера')]"]
    order_button = [By.XPATH, "//button[contains(text(), 'Заказать') and contains(@class, 'Button_Middle__1CSJM')]"]
    confirmation_message = [By.XPATH, "//div[contains(text(), 'Хотите оформить заказ?')]"]
    confirmation_button = [By.XPATH, "//button[contains(text(), 'Да') and contains(@class, 'Button_Middle__1CSJM')]"]
    order_confirmed = [By.CLASS_NAME, 'Order_ModalHeader__3FDaJ']
