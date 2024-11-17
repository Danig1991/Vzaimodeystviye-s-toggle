import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# базовый url
base_url = 'https://the-internet.herokuapp.com/horizontal_slider'

# добавить опции/оставить браузер открытым
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

# автоматическая загрузка драйвера
service = ChromeService(ChromeDriverManager().install())

# открытие браузера с параметрами
driver_chrome = webdriver.Chrome(
    options=options,
    service=service
)

# переход по url в браузере/развернуть на весь экран
driver_chrome.get(base_url)
driver_chrome.maximize_window()

# расширение возможностей драйвера
action = ActionChains(driver_chrome)

# пауза
time.sleep(1)

# найти слайдер и передвинуть вправо на значение 3
slider = driver_chrome.find_element(By.XPATH, "//input[@type='range']")
action.click_and_hold(slider).move_by_offset(10, 0).release().perform()

# пауза
time.sleep(1)

# проверка, что ползунок передвинулся на позицию 3
get_value_slider = driver_chrome.find_element(
    By.XPATH, "//span[@id='range']"
).text
print(f"Значение ползунка - {get_value_slider}.")
assert get_value_slider == "3", "Ошибка: Значение ползунка должно быть 3."
print("Проверка пройдена.")

# закрытие браузера
driver_chrome.quit()
print("Закрытие браузера.")
