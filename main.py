import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import concurrent.futures


def get_lot_names(url):
    # Set up a Selenium webdriver
    chrome_service = ChromeService(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=chrome_service)

    # Load the URL with Selenium to render the JavaScript content
    driver.get(url)

    # Add a delay to ensure the JavaScript loads completely
    time.sleep(5)

    # Get the page source and parse it using BeautifulSoup
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # Find all Lot object names on the page
    lot_names = []

    # Find the Lot object names using the CSS selector
    for lot_title in soup.select('div.row.panel.panel-primary.position-relative.m-b-0 h2 a'):
        lot_name = lot_title.get_text(strip=True)
        lot_names.append(lot_name)

    # Close the Selenium webdriver
    driver.quit()

    return lot_names


def get_total_pages(url):
    # Set up a Selenium webdriver
    chrome_service = ChromeService(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=chrome_service)

    # Load the URL with Selenium to render the JavaScript content
    driver.get(url)

    # Add a delay to ensure the JavaScript loads completely
    time.sleep(5)

    # Get the page source and parse it using BeautifulSoup
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # Find the pagination element
    pagination = soup.find('ul', class_='pagination')

    # Find the last page number
    last_page_number = int(pagination.find_all('li')[-2].get_text(strip=True))

    # Close the Selenium webdriver
    driver.quit()

    return last_page_number


def get_all_lots_for_auction(auction_id, auction_name):
    base_url = f"https://403auction.hibid.com/catalog/{auction_id}/{auction_name}/?cpage="
    first_page_url = base_url + "1"

    total_pages = get_total_pages(first_page_url)
    all_lot_names = []

    # Use ThreadPoolExecutor for parallel processing
    with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
        page_urls = [base_url + str(page_number) for page_number in range(1, total_pages + 1)]
        results = executor.map(get_lot_names, page_urls)

    for result in results:
        all_lot_names.extend(result)

    return all_lot_names


# Scrape all pages for the given auction
auction_id = "444436"
auction_name = "premium-lost-and-undeliverable-freight--1799"
all_lots = get_all_lots_for_auction(auction_id, auction_name)

# Print the Lot objects
for lot in all_lots:
    print(lot)