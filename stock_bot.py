from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException   
from time import sleep
from stock import stocks,qty
price = []
size = len(stocks)


class stock_bot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.moneycontrol.com/india/stockpricequote/')
        sleep(2)
        i=0
        while(i<size):
            self.driver.find_element_by_xpath('/html/body/header/div[1]/div/div[2]/div[2]/div[1]/div/form/input[5]').send_keys(stocks[i])
            self.driver.find_element_by_xpath('/html/body/header/div[1]/div/div[2]/div[2]/div[1]/a').click()
            try:
                self.driver.find_element_by_xpath('/html/body/section[1]/div[2]/section[1]/div[2]/div/div[2]/div[2]/div[1]/div[1]/div[1]/div/div[2]/span[1]')
            except NoSuchElementException:
                try:
                    self.driver.find_element_by_xpath('/html/body/div[2]/div[3]/div[2]/div/table/tbody/tr[1]/td[1]/p/a/strong')
                except:
                    price.append(0)
                    i = i+1
                    continue
                self.driver.find_element_by_xpath('/html/body/div[2]/div[3]/div[2]/div/table/tbody/tr[1]/td[1]/p/a/strong').click()
            price.append(self.driver.find_element_by_xpath('/html/body/section[1]/div[2]/section[1]/div[2]/div/div[2]/div[2]/div[1]/div[1]/div[1]/div/div[2]/span[1]').text)  
            i=i+1

stock_bot()

total = 0
for j in range(0,size):
    print(stocks[j],' : ',price[j])
    total += qty[j]*float(price[j])
print ('Total = ',total)
