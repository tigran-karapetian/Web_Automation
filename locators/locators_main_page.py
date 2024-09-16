from selenium.webdriver.common.by import By


class MainPageLocators:

    yandex_logo = [By.CLASS_NAME, 'Header_LogoYandex__3TSOI']
    scooter_logo = [By.CLASS_NAME, 'Header_LogoScooter__3lsAR']
    order_button = [By.CLASS_NAME, 'Button_Button__ra12g']
    cookie_button = [By.ID, 'rcc-confirm-button']

    # локаторы вопросов на главной странице

    question_one = [By.ID, 'accordion__heading-0']
    question_two = [By.ID, 'accordion__heading-1']
    question_three = [By.ID, 'accordion__heading-2']
    question_four = [By.ID, 'accordion__heading-3']
    question_five = [By.ID, 'accordion__heading-4']
    question_sixth = [By.ID, 'accordion__heading-5']
    question_seven = [By.ID, 'accordion__heading-6']
    question_eight = [By.ID, 'accordion__heading-7']

    # локаторы ответов на главной странице

    answer_one = [[By.ID, 'accordion__panel-0']]
    answer_two = [By.ID, 'accordion__panel-1']
    answer_three = [By.ID, 'accordion__panel-2']
    answer_four = [By.ID, 'accordion__panel-3']
    answer_five = [By.ID, 'accordion__panel-4']
    answer_sixth = [By.ID, 'accordion__panel-5']
    answer_seven = [By.ID, 'accordion__panel-6']
    answer_eight = [By.ID, 'accordion__panel-7']
