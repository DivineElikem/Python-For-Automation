import time
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd


url = 'https://en.wikipedia.org/wiki/Glossary_of_computer_science'

driver = webdriver.Chrome()
driver.get(url)


time.sleep(5)


page_source = driver.page_source


driver.quit()


soup = BeautifulSoup(page_source, 'html.parser')


glossary_entries = soup.find_all('dl', class_='glossary')


terminologies = []
definitions = []

print(f"Found {len(glossary_entries)} glossary entries")

print("Glossary: ", glossary_entries)

for entry in glossary_entries:
    term_list = entry.find_all('dt')
    definition_list = entry.find_all('dd')

print("Term list: ", term_list, "\nDefinition list: ", definition_list)   
for term in term_list:    
    terminology = term.text.strip()        
    terminologies.append(terminology)

for definition in definition_list:
    definition = definition.text.strip()
    definitions.append(definition)


df = pd.DataFrame({
    'Terminology': terminologies,
    'Definition': definitions
})


df.to_excel('IT_wiki.xlsx', index=False)

print("Scraping complete. Data saved to IT_wiki_glossary.xlsx")
