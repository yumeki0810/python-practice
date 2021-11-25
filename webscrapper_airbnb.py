rom selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
for i in range(0,5):
    link = "https://zh.airbnb.com/s/Shenzhen--China/homes?items_offset=" + str(i *20)
    driver.get(link)
    time.sleep(10)
    rent_list = driver.find_elements(By.CSS_SELECTOR,'div._gig1e7')
    for eachhouse in rent_list:
        try:
            comment = eachhouse.find_element(By.CSS_SELECTOR,'span._1clmxfj') 
            comment = comment.text
            comment = comment.split("·")[1]
        except:
            comment = 0
        price = eachhouse.find_element(By.CSS_SELECTOR,'div._1orel7j7')
        price = price.text.replace("晚","").replace("价格","").replace("\n","")
        name = eachhouse.find_element(By.CSS_SELECTOR,'div._qrfr9x5')
        name = name.text
        details = eachhouse.find_element(By.CSS_SELECTOR,'span._faldii7')
        details = details.text.replace(",","").replace("·","").replace("\n","")
        #house_type = details.split(".")[0]
        #bed_number = details.split(".")[1]
        #print(comment,price,name,house_type,bed_number)
        print(comment,"\n",price,"\n",name,"\n",details)
        print("\n")
