import requests
from bs4 import BeautifulSoup
import csv
import time

def scrape_website(url):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print("Error fetching " + url + ": " + str(e))
        return None
    
    return response.text

def extract_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    data = []
    
    for item in soup.find_all('div', class_='example-class'):
        title = item.find('h2').text.strip() if item.find('h2') else 'N/A'
        description = item.find('p').text.strip() if item.find('p') else 'N/A'
        link = item.find('a')['href'] if item.find('a') else 'N/A'
        
        data.append([title, description, link])
    
    return data

def save_to_csv(data, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "Description", "Link"])
        writer.writerows(data)
    
    print("Data saved to " + filename)

def main():
    url = "https://www.shadowfox.in/"
    html = scrape_website(url)
    
    if html:
        extracted_data = extract_data(html)
        save_to_csv(extracted_data, "scraped_data.csv")

if __name__ == "__main__":
    main()