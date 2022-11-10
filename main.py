import math
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


def main():
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    try:
        button = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
        WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
        button.click()
        x = int(browser.find_element(By.CSS_SELECTOR, "span#input_value").text)
        answer = calc(x)
        browser.find_element(By.CSS_SELECTOR, "input#answer").send_keys(answer)
        browser.find_element(By.CSS_SELECTOR, "#solve").click()
        time.sleep(10)
    finally:
        time.sleep(5)
        browser.quit()


if __name__ == '__main__':
    main()
