#Task 3

import pandas as pd
import json
import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
try:
    driver.get("https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart")
    print(driver.title)

    #find li elements
    ul = driver.find_element(By.CSS_SELECTOR, '.results')
    li_entries = ul.find_elements(By.CSS_SELECTOR, "li.row.cp-search-result-item")
    print(len(li_entries))
    # create a empty list 'results'
    results = []
    for li in li_entries:
        # entries that contains the title of the book:
        book_title = li.find_element(By.CSS_SELECTOR, 'span.title-content').text.strip()
        
        #entries that contain the authors of the book, and get the text for each, more than one author, you want to join the author names with a semicolon ; between each
        book_author = li.find_element(By.CSS_SELECTOR, 'a.author-link').text.strip()
        #author_text = "; ".join(authors)
        #find the div that contains the format and the year, and then you find the span entry within it that contains this information.  You get that text too
        format_div = li.find_element(By.CSS_SELECTOR, '.cp-format-info')
        format_year = format_div.find_element(By.CSS_SELECTOR, 'span.cp-screen-reader-message').text.strip()

        #Create a dict that stores these values, with the keys being Title, Author, and Format-Year.  Then append that dict to your results list.
        book_dict = {"Title": book_title, "Author": book_author, "Format-Year": format_year}
        #append the dict to results list
        results.append(book_dict)

    #Create a DataFrame from this list of dicts.  Print the DataFrame
    book_info = pd.DataFrame(results)
    print(book_info)


except Exception as e:
    print(f"Error: {type(e).__name__}: {e}")

finally:
     driver.quit()

# Task 4 Write out the Data
book_info.to_csv('./assignment8/get_books.csv', index=False)
with open('./assignment8/get_books.json', 'w') as json_file:
    json.dump(results, json_file, indent=4)


