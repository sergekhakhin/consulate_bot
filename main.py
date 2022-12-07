from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from captcha_solver import solve_captcha

service = ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

url = "https://gyumri.kdmid.ru/queue/orderinfo.aspx?id=16487&cd=00b29879&ems=BF464C54"


def main() -> None:
    driver.get(url)
    sleep(2)
    fill_captcha_textbox(solve_captcha(get_captcha_img()))
    sleep(5)
    submit_captcha()
    sleep(5)
    click_enroll_button()
    sleep(5)


def get_captcha_img() -> bytes:
    return driver.find_element(By.ID, "ctl00_MainContent_imgSecNum").screenshot_as_png


def save_captcha_img(img: bytes) -> None:
    with open("captcha.png", "wb") as f:
        f.write(img)


def fill_captcha_textbox(solution: str) -> None:
    captcha_textbox = driver.find_element(By.ID, "ctl00_MainContent_txtCode")
    captcha_textbox.send_keys(solution)


def submit_captcha() -> None:
    submit_button = driver.find_element(By.ID, "ctl00_MainContent_ButtonA")
    submit_button.click()


def click_enroll_button() -> None:
    enroll_button = driver.find_element(By.ID, "ctl00_MainContent_ButtonB")
    enroll_button.click()


if __name__ == "__main__":
    main()
