import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

# 1
# url = "http://suninjuly.github.io/simple_form_find_task.html"
# try:
#     browser = webdriver.Chrome()
#     browser.get(url)
#
#     input1 = browser.find_element(By.TAG_NAME, "input")
#     input1.send_keys("Ivan")
#     input2 = browser.find_element(By.NAME, "last_name")
#     input2.send_keys("Petrov")
#     input3 = browser.find_element(By.CLASS_NAME, "form-control.city")
#     input3.send_keys("Smolensk")
#     input4 = browser.find_element(By.ID, "country")
#     input4.send_keys("Russia")
#     button = browser.find_element(By.CSS_SELECTOR, "button.btn")
#     button.click()
#
# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(30)
#     # закрываем браузер после всех манипуляций
#     browser.quit()

# 2
# url = 'http://suninjuly.github.io/find_link_text'
# with webdriver.Chrome() as browser:
#     browser.get(url)
#     link = browser.find_element(By.PARTIAL_LINK_TEXT, str(math.ceil(math.pow(math.pi, math.e)*10000)))
#     link.click()
#     input1 = browser.find_element(By.TAG_NAME, "input")
#     input1.send_keys("Ivan")
#     input2 = browser.find_element(By.NAME, "last_name")
#     input2.send_keys("Petrov")
#     input3 = browser.find_element(By.CLASS_NAME, "form-control.city")
#     input3.send_keys("Smolensk")
#     input4 = browser.find_element(By.ID, "country")
#     input4.send_keys("Russia")
#     button = browser.find_element(By.CSS_SELECTOR, "button.btn")
#     button.click()
#     time.sleep(20)

# 3
# try:
#     browser = webdriver.Chrome()
#     browser.get("http://suninjuly.github.io/huge_form.html")
#     elements = browser.find_elements(By.CSS_SELECTOR, ".first_block input")
#     for element in elements:
#         element.send_keys("Мой ответ")
#     browser.find_element(By.CSS_SELECTOR, "button.btn").click()
#
# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(20)
#     # закрываем браузер после всех манипуляций
#     browser.quit()

# не забываем оставить пустую строку в конце файла

# 4
# try:
#     browser = webdriver.Chrome()
#     browser.get("http://suninjuly.github.io/find_xpath_form")
#     for element in browser.find_elements(By.XPATH, '//input'):
#         element.send_keys("Мой ответ")
#     browser.find_element(By.XPATH, '//button[text()="Submit"]').click()
#
# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(20)
#     # закрываем браузер после всех манипуляций
#     browser.quit()

# 5
url_1 = 'http://suninjuly.github.io/registration1.html'
url_2 = 'http://suninjuly.github.io/registration2.html'
try:
    browser = webdriver.Chrome()
    browser.get(url_2)

    # Ваш код, который заполняет обязательные поля
    phs = ["Input your first name", "Input your last name", "Input your email"]
    classes = ["first", "second", "third"]
    browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your first name"]').send_keys('text')
    browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your last name"]').send_keys('text')
    browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your email"]').send_keys('text')


    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()


