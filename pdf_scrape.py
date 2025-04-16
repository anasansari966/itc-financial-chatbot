import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import os

url = "https://www.itcportal.com/about-itc/shareholder-value/report-and-accounts.aspx"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

response = requests.get(url, headers=headers)
if response.status_code != 200:
    print("Failed to retrieve the webpage. Status code:", response.status_code)
    exit()

soup = BeautifulSoup(response.content, 'html.parser')

pdf_links = []
for link in soup.find_all('a'):
    href = link.get('href', '')
    if href.lower().endswith('.pdf'):
        pdf_links.append(href)

download_dir = "itc_pdfs"
os.makedirs(download_dir, exist_ok=True)

for href in pdf_links:
    absolute_url = urljoin(url, href)

    parsed_url = urlparse(absolute_url)
    filename = os.path.basename(parsed_url.path)

    if not filename:
        print(f"Skipping invalid URL: {absolute_url}")
        continue

    filepath = os.path.join(download_dir, filename)

    if os.path.exists(filepath):
        print(f"File '{filename}' already exists. Skipping download.")
        continue

    print(f"Downloading {absolute_url}...")
    pdf_response = requests.get(absolute_url, headers=headers)

    if pdf_response.status_code == 200:
        with open(filepath, 'wb') as f:
            f.write(pdf_response.content)
        print(f"Successfully saved '{filename}'")
    else:
        print(f"Failed to download '{filename}'. Status code: {pdf_response.status_code}")

print("PDF download process completed.")