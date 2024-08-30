import time
from typing import List

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class Emulator:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://mate.academy/type")
        self.login_mate()

    def login_mate(self) -> None:
        driver = self.driver
        email_input = driver.find_element(By.NAME, "email")
        email_input.click()
        email_input.send_keys("necobrane105@gmail.com")
        submit_button = driver.find_element(By.CSS_SELECTOR, "[type='submit']")
        submit_button.click()
        time.sleep(1)
        password_input = driver.find_element(By.NAME, "password")
        password_input.click()
        password_input.send_keys("Xx2005zZ@")
        submit_button = driver.find_element(By.CSS_SELECTOR, "[type='submit']")
        submit_button.click()
        time.sleep(10)

    def parse_words(self, words_block: WebElement) -> str:
        *first_word, other_words = words_block.text.split("\n")
        first_word = "".join(first_word)
        return first_word + " " + other_words

    def type_words(self, typing_input: WebElement, text: str) -> None:
        typing_input.send_keys(text[:-1])
        typing_input.send_keys(text[-1])

    def hack_typing(self):
        driver = self.driver

        words_block = driver.find_element(By.CSS_SELECTOR, "[data-qa='test-block-words']")
        text = self.parse_words(words_block)
        print(text)
        typing_input = driver.find_element(By.CSS_SELECTOR, "[class^='TestBlock_testInput']")
        self.type_words(typing_input, text)


if __name__ == "__main__":
    emulator = Emulator()
    emulator.hack_typing()
    time.sleep(100)
