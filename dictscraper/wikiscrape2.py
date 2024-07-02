from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

# Initialize the Chrome driver
service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# URL of the Wikipedia page
url = 'https://en.wikipedia.org/wiki/Glossary_of_computer_science'
driver.get(url)

# Find all glossary sections
glossary_sections = driver.find_elements(By.CSS_SELECTOR, 'dl.glossary')

terminologies = []
definitions = []

# Loop through each section to extract terms and definitions
for section in glossary_sections:
    terms = section.find_elements(By.TAG_NAME, 'dt')
    defs = section.find_elements(By.TAG_NAME, 'dd')

    for term, definition in zip(terms, defs):
        terminology = term.text.strip()
        definition_text = definition.text.strip()
        
        terminologies.append(terminology)
        definitions.append(definition_text)

# Close the driver
driver.quit()

# Save the extracted data into a spreadsheet using pandas
data = {
    'Terminology': terminologies,
    'Definition': definitions
}

df = pd.DataFrame(data)
df.to_excel('IT_Dictionary.xlsx', index=False)

print('Data has been successfully saved to IT_Dictionary.xlsx')
