import pandas as pd
from langchain_huggingface import HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
import os

os.environ["HUGGINGFACE_API_TOKEN"] = "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"

# List of predefined categories
categories = [
    "Algorithms and Algorithm Design", 
    "Data Structures", 
    "Programming Concepts", 
    "Software Engineering", 
    "Networking", 
    "Hardware & Architecture", 
    "Computational/Mathematical Disciplines", 
    "General Computer fundamentals", 
    "Applications and Domains", 
    "General Concepts", 
    "Operating Systems", 
    "Database", 
    "Machine Learning and Artificial Intelligence"
]

prompt = PromptTemplate.from_template(
    """Below is a list containing strings. These strings are suggested\
    categories of IT and computer science terminologies.\
    ```
    categories = [\
    "Algorithms and Algorithm Design", 
    "Data Structures", 
    "Programming Concepts", 
    "Software Engineering", 
    "Networking", 
    "Hardware & Architecture", 
    "Computational/Mathematical Disciplines", 
    "General Computer fundamentals", 
    "Applications and Domains", 
    "General Concepts", 
    "Operating Systems", 
    "Database", 
    "Machine Learning and Artificial Intelligence"].\
    ```
    With the categories above you will be given an IT or computer
    science terminology and work is to choose among the list of
    categories which would best suit as a category for that terminology.

    REMEMBER:
    The human provides a 'terminology' and you provide a 'response'

    Example:
    terminology: Routing Table
    response: Netwoking
    
    NOTE:
    'response' must be one of the Categories list.

    Here is the terminology:
    {terminology}
    """
    
)

def predict_category(terminology):
    predictor = HuggingFaceEndpoint(repo_id="mistralai/Mixtral-8x7B-Instruct-v0.1")

    # Predict category
    chain = prompt | predictor
    category = chain.invoke({"terminology": terminology})

    for defined_category in categories:
        if defined_category in category:
            category = defined_category
    
    return category

# Load the Excel file into a DataFrame
file_path = 'IT_glossary.xlsx'
df = pd.read_excel(file_path)

df.columns = df.columns.str.strip()

# Add a new column for categories
df['Category'] = ''

print(df.head())
exit

# Iterate through each terminology and predict its category
for index, row in df.iterrows():
    terminology = row['Terminology']
    category = predict_category(terminology)
    df.at[index, 'Category'] = category

# Save the updated DataFrame back to the Excel file
updated_file_path = 'IT_glossary_updated.xlsx'
df.to_excel(updated_file_path, index=False)

print(f"Categorization complete. Updated data saved to {updated_file_path}")
