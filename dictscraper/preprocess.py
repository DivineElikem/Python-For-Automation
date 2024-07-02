import re

def clean_text(file_path, output_path):

    with open(file_path, 'r') as file:
        content = file.read()
    
   
    cleaned_content = re.sub(r'[\[\]0-9]', '', content)
    
    
    with open(output_path, 'w') as file:
        file.write(cleaned_content)


input_file = 'IT_Dictionary.json'
output_file = 'cleaned_Dictionary.json'
clean_text(input_file, output_file)
