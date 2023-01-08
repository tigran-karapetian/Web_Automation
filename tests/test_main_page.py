import allure
from pages.main_page import MainPage


class TestMainPage:
    @allure.title('Проверка перехода на главную страницу Яндекса при нажатии на логотип Яндекса.')
    @allure.description('При нажатии на логотип Яндекс откроется главная страница Яндекса в новом окне.')
    def test_click_yandex_logo(self, driver):
        main_page = MainPage(driver)
        main_page.click_yandex_logo()
        assert len(driver.window_handles) == 2

    @allure.title('Проверка перехода на главную страницу сервиса Самокат.')
    @allure.description('При нажатии на логотип Самоката переход на главную страницу Самоката.')
    def test_click_scooter_logo(self, driver):
        main_page = MainPage(driver)
        main_page.click_scooter_logo()
        assert driver.current_url == "https://qa-scooter.praktikum-services.ru/"

    @allure.title('Проверка выпадающего списка в разделе Вопросы о важном')
    @allure.description('Проверка первого вопроса на открытие и соотвествие текста ответа')
    def test_question_one(self, driver):
        main_page = MainPage(driver)
        main_page.click_question_one()
        assert main_page.get_answer_one(driver) == 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'

    @allure.title('Проверка выпадающего списка в разделе Вопросы о важном')
    @allure.description('Проверка второго вопроса на открытие и соотвествие текста ответа')
    def test_question_two(self, driver):
        main_page = MainPage(driver)
        main_page.click_question_two()
        assert main_page.get_answer_two(driver) == 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'

    @allure.title('Проверка выпадающего списка в разделе Вопросы о важном')
    @allure.description('Проверка третьего вопроса на открытие и соотвествие текста ответа')
    def test_question_three(self, driver):
        main_page = MainPage(driver)
        main_page.click_question_three()
        assert main_page.get_answer_three(driver) == 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'


    @allure.title('Проверка выпадающего списка в разделе Вопросы о важном')
    @allure.description('Проверка четвертого вопроса на открытие и соотвествие текста ответа')
    def test_question_four(self, driver):
        main_page = MainPage(driver)
        main_page.click_question_four()
        assert main_page.get_answer_four(driver) == 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'

    @allure.title('Проверка выпадающего списка в разделе Вопросы о важном')
    @allure.description('Проверка пятого вопроса на открытие и соотвествие текста ответа')
    def test_question_five(self, driver):
        main_page = MainPage(driver)
        main_page.click_question_five()
        assert main_page.get_answer_five(
            driver) == 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'

    @allure.title('Проверка выпадающего списка в разделе Вопросы о важном')
    @allure.description('Проверка шестого вопроса на открытие и соотвествие текста ответа')
    def test_question_sixth(self, driver):
        main_page = MainPage(driver)
        main_page.click_question_sixth(driver)
        assert main_page.get_answer_sixth(
            driver) == 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'

    @allure.title('Проверка выпадающего списка в разделе Вопросы о важном')
    @allure.description('Проверка седьмого вопроса на открытие и соотвествие текста ответа')
    def test_question_seven(self, driver):
        main_page = MainPage(driver)
        main_page.click_question_seven(driver)
        assert main_page.get_answer_seven(
            driver) == 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'

    @allure.title('Проверка выпадающего списка в разделе Вопросы о важном')
    @allure.description('Проверка восьмого вопроса на открытие и соотвествие текста ответа')
    def test_question_eight(self, driver):
        main_page = MainPage(driver)
        main_page.click_question_eight(driver)
        assert main_page.get_answer_eight(driver) == 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'
