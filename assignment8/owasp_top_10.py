#Task 6
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

url_2021_list = 'https://owasp.org/Top10/2021/'
driver.get(url_2021_list)

#create list vulnerabilities
vulnerabilities = []
# find the 2021 top 10 list  links 
link_elements = driver.find_elements(By.XPATH, '//h3[@id="the-top-102021-list"]/following-sibling::ol/li/a')

for link in link_elements:
        #print(f"{link.text}: {link.get_attribute('href')}")
        name = link.text.strip()
        url = link.get_attribute("href")
        if name and url:
            vulnerabilities.append({"name": name, "url": url})


#print list vulnerabilities
print(vulnerabilities)

driver.quit()

#write data to csv file
import csv
with open('./assignment8/owasp_top_10.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Link"])
    for link in vulnerabilities:
        writer.writerow([link["name"], link["url"]])