import time
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd


url = 'https://adacomputerscience.org/glossary?examBoard=all&stage=all'

driver = webdriver.Chrome()
driver.get(url)


time.sleep(5)


page_source = driver.page_source


driver.quit()


soup = BeautifulSoup(page_source, 'html.parser')


glossary_entries = soup.find_all('div', class_='glossary_term row')


terminologies = []
definitions = []

print(f"Found {len(glossary_entries)} glossary entries")


for entry in glossary_entries:
    term_tag = entry.find('div', class_='glossary_term_name col-md-3').find('strong')
    definition_tag = entry.find('div', class_='col-md-7').find('p')
    
    if term_tag and definition_tag:
        terminology = term_tag.text.strip()
        definition = definition_tag.text.strip()
        
        terminologies.append(terminology)
        definitions.append(definition)


df = pd.DataFrame({
    'Terminology': terminologies,
    'Definition': definitions
})


df.to_excel('IT_glossary.xlsx', index=False)

print("Scraping complete. Data saved to IT_glossary.xlsx")
