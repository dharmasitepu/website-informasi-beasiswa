import json
from bs4 import BeautifulSoup
import pandas as pd

# Read HTML data from the file
with open('./Back-End/kominfo/data.txt', 'r', encoding='utf-8') as file:
    html_data = file.read()

# Parse HTML using BeautifulSoup
soup = BeautifulSoup(html_data, 'html.parser')

# Extract relevant information
beasiswa_list = []
for idx, beasiswa_div in enumerate(soup.find_all('div', class_='flex flex-col mx-3 p-4 rounded-lg text-secondary-700 gap-4 shadow-md border-[1px] bg-gray-200 border-gray-500')):
    beasiswa = {}
    beasiswa['_id'] = idx  # Assign an ID to each row
    beasiswa['name'] = beasiswa_div.find('div', class_='text-base').text.strip()
    beasiswa['status'] = beasiswa_div.find('div', class_='p-2 ml-auto rounded-md text-xs font-normal text-red-500 bg-red-200').text.strip()
    
    category_info = beasiswa_div.find_all('div', class_='my-1')
    beasiswa['category'] = category_info[0].text.strip()
    beasiswa['periode_penerimaan'] = category_info[1].text.strip()

    university_info = beasiswa_div.find('div', class_='font-normal text-sm').text.split('\n')
    beasiswa['university'] = university_info[0].strip()
    
    logo_src = beasiswa_div.find('img')['src']
    beasiswa['logo'] = f"https://beasiswa.kominfo.go.id/{logo_src}"  # Replace with your actual base URL
    
    beasiswa_list.append(beasiswa)

# Convert the list of dictionaries to a JSON-formatted string with correct structure
json_data = json.dumps(beasiswa_list, indent=2)

# Save JSON string to a file
with open('./Back-End/kominfo/data_with_id.json', 'w', encoding='utf-8') as json_file:
    json_file.write(json_data)
