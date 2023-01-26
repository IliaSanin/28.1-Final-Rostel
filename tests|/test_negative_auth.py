import pytest
from auth_page import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


# авторизация по номеру, почте, логину и ЛС с невалидными данными
@pytest.mark.parametrize('input', ['', '+79175394020', 'sanmosk2212@gmail.ru', \
                                   'почта@мыло.ру', '@ru', '23423423987645627883', '%@!#$%^&*()_+><'])
@pytest.mark.parametrize('password', ['Sun321test', '12345443', '!@#$%^&*()'])
def test_auth_with_invalid_volue(start_page, input, password):
    ros_tel = AuthPage(start_page)
    ros_tel.input.send_keys(input)
    ros_tel.password.send_keys(password)
    ros_tel.auth_btn.click()

    try:
        assert ros_tel.find_element(By.ID,
                                    'form-error-message').text == 'Неверный логин или пароль' or 'Неверно введен текст с картинки'

    except:
        assert ros_tel.find_element(By.XPATH,
                                    '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/span').text == 'Введите номер телефона' or 'Неверный формат телефона'


# проверка регистрации с невалидными данными
@pytest.mark.parametrize('name', ['K', 'С1'])
@pytest.mark.parametrize('lastname', ['аагмпиролтодьлотрипмриотгнгрорпмганприрмпмрил'])
@pytest.mark.parametrize('address', ['234f+79175394021', '6854659mail.ru', 'почта@мыло.ру'])
@pytest.mark.parametrize('password', ['Sun123', '123456789', ')))'])
@pytest.mark.parametrize('confirm', ['Sun12', 'sun123'])
def test_reg_with_invalid_volue(start_page, name, lastname, address, password, confirm):
    ros_tel = AuthPage(start_page)
    ros_tel.scroll_down()
    ros_tel.reg_click()
    reg_page = RegPage(start_page, ros_tel.get_current_url())
    reg_page.name.send_keys(name)
    reg_page.lastname.send_keys(lastname)
    reg_page.address.send_keys(address)
    reg_page.new_pass.send_keys(password)
    reg_page.confirm.send_keys(confirm)
    reg_page.get_click()

    assert reg_page.find_element(By.XPATH,
                                 '//*[@id="page-right"]/div/div/div/form/div[1]/div[1]/span').text == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'
    assert reg_page.find_element(By.XPATH,
                                 '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/span').text == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'
    assert reg_page.find_element(By.XPATH,
                                 '//*[@id="page-right"]/div/div/div/form/div[3]/span').text == 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru'
    assert reg_page.find_element(By.XPATH,
                                 '//*[@id="page-right"]/div/div/div/form/div[4]/div[1]/span').text == 'Длина пароля должна быть не менее 8 символов' or 'Пароли не совпадают' or 'Пароль должен содержать хотя бы одну заглавную букву'
