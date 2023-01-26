import pytest
from auth_page import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



# смоук тест полей ввода
def test_smoke(start_page):
    ros_tel = AuthPage(start_page)
    ros_tel.input.click()
    ros_tel.password.click()
    ros_tel.checkbox.click()

    assert ros_tel.find_element(By.XPATH,
                                '//*[@id="page-right"]/div/div/h1').text == 'Авторизация'
    assert ros_tel.find_element(By.XPATH,
                                '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/div/div[2]')
    assert ros_tel.find_element(By.XPATH,
                                '// *[ @ id = "page-right"] / div / div / div / form / div[2] / div / span[2]')


# проверка авторизации по номеру телефона

def test_auth_with_valid_phone(start_page):
    ros_tel = AuthPage(start_page)
    ros_tel.input.send_keys('+79175394021')
    ros_tel.password.send_keys('Suninis22')
    ros_tel.auth_btn.click()

    assert ros_tel.find_element(By.ID, 'lk-btn').text == 'Личный кабинет'


# проверка авторизаци по почте

def test_auth_with_valid_mail(start_page):
    ros_tel = AuthPage(start_page)
    ros_tel.input.send_keys('sanmosk2212@gmail.com')
    ros_tel.password.send_keys('Sun123test')
    ros_tel.auth_btn.click()

    assert ros_tel.find_element(By.ID, 'lk-btn').text == 'Личный кабинет'


# проверка авторизации по ЛС

def test_auth_with_login(start_page):
    ros_tel = AuthPage(start_page)
    ros_tel.input.send_keys('lk_32428591')
    ros_tel.password.send_keys('Suninis22')
    ros_tel.auth_btn.click()

    assert ros_tel.find_element(By.ID, 'lk-btn').text == 'Личный кабинет'


# проверка входа по временному коду до момента ввода кода

def test_auth_with_sms(start_page):
    ros_tel = CodePage(start_page)
    ros_tel.address.send_keys('+79175394021')
    ros_tel.get_code.click()

    assert ros_tel.find_element(By.CLASS_NAME, 'card-container__title').text == 'Код подтверждения отправлен'


# проверка входа по ссылке на почту до момента ввода

def test_auth_with_mail(start_page):
    ros_tel = CodePage(start_page)
    ros_tel.address.send_keys('sanmosk2212@gmail.com')
    ros_tel.get_code.click()
    assert ros_tel.find_element(By.CLASS_NAME, 'card-container__title').text == 'Код подтверждения отправлен'


# проверка регистрации нового пользователя до момента подтверждения

def test_register_new_user(start_page):
    ros_tel = AuthPage(start_page)
    ros_tel.scroll_down()
    ros_tel.reg_click()
    reg_page = RegPage(start_page, ros_tel.get_current_url())
    reg_page.name.send_keys('Леев')
    reg_page.lastname.send_keys('Толстой')
    reg_page.address.send_keys('levtolstoy@mail.ru')
    reg_page.new_pass.send_keys('Tolstoy1751')
    reg_page.confirm.send_keys('Tolstoy1751')
    reg_page.get_click()

    try:
        assert reg_page.find_element(By.CLASS_NAME, 'card-container__title').text == 'Подтверждение email'
    except:
        assert reg_page.find_element(By.CLASS_NAME, 'card-modal__title').text == 'Учётная запись уже существует'


# набор тестов для авторизации через соцсети
def test_auth_with_social_01(start_page):
    ros_tel = AuthPage(start_page)
    ros_tel.vk_btn.click()
    assert ros_tel.get_base_url() == 'oauth.vk.com'


def test_auth_with_social_02(start_page):
    ros_tel = AuthPage(start_page)
    ros_tel.ok_btn.click()
    assert ros_tel.get_base_url() == 'connect.ok.ru'


def test_auth_with_social_03(start_page):
    ros_tel = AuthPage(start_page)
    ros_tel.mail_btn.click()
    assert ros_tel.get_base_url() == 'connect.mail.ru'


def test_auth_with_social_04(start_page):
    ros_tel = AuthPage(start_page)
    ros_tel.google_btn.click()
    assert ros_tel.get_base_url() == 'accounts.google.com'


# яндекс падает - не знаю, что с ним делать
def test_auth_with_social_05(start_page):
    ros_tel = AuthPage(start_page)
    ros_tel.ya_btn.click()
    assert ros_tel.get_base_url() == 'passport.yandex.ru'


# проверка ссылки Пользовательское соглашение
def test_link_agreement(start_page):
    ros_tel = AuthPage(start_page)
    original_window = ros_tel.driver.current_window_handle
    ros_tel.agree.click()
    WebDriverWait(ros_tel.driver, 5).until(EC.number_of_windows_to_be(2))
    for window_handle in ros_tel.driver.window_handles:
        if window_handle != original_window:
            ros_tel.driver.switch_to.window(window_handle)
            break
    win_title = ros_tel.driver.execute_script("return window.document.title")

    assert win_title == 'User agreement'


# проверка чекбокса "запомнить"
def test_chekbox_memory(start_page):
    ros_tel = AuthPage(start_page)
    ros_tel.input.send_keys('+79175394021')
    ros_tel.password.send_keys('Suninis22')
    ros_tel.checkbox.click()
    ros_tel.auth_btn.click()

    assert ros_tel.find_element(By.ID, 'lk-btn').text == 'Личный кабинет'
