import os

def read_urls_from_file(file_path):
    urls = []
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            urls = [line.strip() for line in file if line.strip()]
    return urls

# Get URLs from urls.txt
urls_file_path = './Data/News/urls.txt'
urls_list = read_urls_from_file(urls_file_path)

# Get URLs from new_urls.txt
new_urls_file_path = './Data/News/new_urls.txt'
new_urls_list = read_urls_from_file(new_urls_file_path)

print(f"Number of URLs in urls.txt: {len(urls_list)}")
print(f"Number of URLs in new_urls.txt: {len(new_urls_list)}")

import requests

import json
from bs4 import BeautifulSoup

def extract_text_blocks(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find the script tag containing the JSON data
        script_tag = soup.find('script', type='application/json')
        
        if script_tag:
            json_data = json.loads(script_tag.string)
            
            # Extract text blocks from the JSON data
            text_blocks = []
            for item in json_data.get('props', {}).get('pageProps', {}).get('initialState', {}).get('article', {}).get('content', []):
                if item.get('type') == 'text_block':
                    text_blocks.append(item.get('value', ''))
            
            return text_blocks
        else:
            print(f"No JSON data found in the script tag for URL: {url}")
            return []
    except requests.RequestException as e:
        print(f"Error fetching URL {url}: {e}")
        return []

if urls_list:
    first_url = urls_list[0]
    text_blocks = extract_text_blocks(first_url)
    
    print(f"Text blocks extracted from {first_url}:")
    for i, block in enumerate(text_blocks, 1):
        print(f"Block {i}: {block}")
else:
    print("No URLs found in urls_list.")

