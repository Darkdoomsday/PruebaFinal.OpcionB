from selenium import webdriver
from selenium.webdriver.common.by import By
from db import MongoDriver

driver = webdriver.Chrome()
driver.get("https://juegosdelamesaredonda.com/")
search_box = driver.find_element(by=By.CSS_SELECTOR, value="#search_query_top")
search_box.send_keys("Cartas")

search_button = driver.find_element(by=By.CSS_SELECTOR, value="#searchbox > button > span")
search_button.click()

articles = driver.find_elements(By.CSS_SELECTOR, "#center_column > ul > li:nth-child(n) > div")

mongodb = MongoDriver()

for card in articles:
    try:
        #image = card.find_element(By.CSS_SELECTOR, "div > div > div.left-block2.col-xs-4.col-xs-4.col-md-3 > div > a > img").image
        title = card.find_element(By.CSS_SELECTOR, "div > div > div.center-block2.col-xs-4.col-xs-7.col-md-6 > h3 > a").text
        description = card.find_element(By.CSS_SELECTOR, "div > div > div.center-block2.col-xs-4.col-xs-7.col-md-6 > p").text
        price = card.find_element(By.CSS_SELECTOR, "div > div > div.right-block2.col-xs-4.col-xs-7.col-md-3 > div > div.content_price.col-xs-12.col-md-12 > span").text
        print(title)
        print(description)
        print(f"{price}")

        juegos = {
            "Título": title,
            "Descripción": description,
            "Precio": price
        }



        mongodb.insert_record(record=juegos, username="cartas")

        print("++++++++++++++++++++++++++++++++")
    except Exception as e:
        print(e)
        print("++++++++++++++++++++++++++++++++")


driver.close()