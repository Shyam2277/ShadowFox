#simple code for web scraping data using beautiful soup!

import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    headers = {'User-Agent': 'Mozilla/5.0'} 
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        print("Failed to retrieve page:",response.status_code)
        return None
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    links = [a['href'] for a in soup.find_all('a', href=True)]
    
    return links

if __name__ == "__main__":
    url = "https://www.youtube.com/@DingDingboi" 
    scraped_data = scrape_website(url)
    
    if scraped_data:
        print("extracted links:")
        for link in scraped_data:
            print(link)
    
    