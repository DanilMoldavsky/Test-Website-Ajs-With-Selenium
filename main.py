from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from utilities import Utilities
import random
import time

PATH_MESSAGE = 'messages.txt'
PATH_CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
PATH_DRIVER = 'chromedriver\chromedriver.exe'

service = Service(PATH_DRIVER)
url = 'https://ajs.su/'
options = webdriver.ChromeOptions()
options.add_argument('--log-level=3')
options.add_argument("--headless=new")
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36")
options.binary_location = PATH_CHROME


def get_message(path:str):
    choice = int(input('Выберите метод: 1 - Случайное сообщение, 2 - Сообщение из файла: '))
    messages = Utilities.get_string(path)
    
    if choice == 1:
        return random.choice(messages)
    else:
        choice_mess = int(input('Введите номер сообщения, если считать сверху стрОки: '))
        return messages[choice_mess]

def send_message(url:str, message:str):
    try:
        driver = webdriver.Chrome(service=service, options=options)
        driver.delete_all_cookies()
        driver.get(url)
        
        div_to_frame = driver.find_element(By.XPATH, '//div[@id="carrotquest-messenger-collapsed-container"]/div/div/iframe')
        driver.switch_to.frame(div_to_frame)

        driver.find_element(By.XPATH, '/html/body/div/div[1]').click()
        time.sleep(5)
        
        driver.switch_to.default_content()
        
        frame2 = driver.find_element(By.ID, 'carrot-messenger-frame')
        driver.switch_to.frame(frame2)
        
        driver.find_element(By.XPATH, '//*[@id="carrotquest-messenger"]/div/div/div[2]/div/div[1]/div/div/div[1]/div[1]/button').click()
        time.sleep(5)
        
        
        message_input = driver.find_element(By.ID, 'opened-textfield')
        message_input.send_keys(message)
        # message_input.send_keys(Keys.ENTER)
        print('Сообщение отправлено')
        
        
    except Exception as e:
        print(e)
        
    finally:
        # time.sleep(20)
        time.sleep(2)
        driver.close()
        driver.quit()

def main():
    message = get_message(PATH_MESSAGE)
    send_message(url, message)

if __name__ == '__main__':
    main()