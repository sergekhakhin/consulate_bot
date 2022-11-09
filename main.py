from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from captcha_solver import solve_captcha

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
url = ""


def main() -> None:
    driver.get(url)
    fill_captcha_textbox(solve_captcha(get_captcha_img()))
    sleep(3)
    submit_captcha()
    sleep(3)
    click_enroll_button()
    sleep(15)


def get_captcha_img() -> str:
    return driver.find_element(By.ID, "ctl00_MainContent_imgSecNum").screenshot_as_base64


def fill_captcha_textbox(solution: str) -> None:
    captcha_textbox = driver.find_element(By.ID, "ctl00_MainContent_txtCode")
    captcha_textbox.send_keys(solution)


def submit_captcha() -> None:
    submit_button = driver.find_element(By.ID, "ctl00_MainContent_ButtonA")
    submit_button.click()


def click_enroll_button() -> None:
    enroll_button = driver.find_element(By.ID, "ctl00_MainContent_ButtonB")
    enroll_button.click()


if __name__ == '__main__':
    main()
