# Auction Lot Scraper README

## Purpose

This project aims to scrape auction Lot object names from the 403 Auction website. It specifically targets the auction pages that follow the URL structure `https://403auction.hibid.com/catalog/{auction_id}/{auction_name}/?cpage={page_number}`. The script retrieves all Lot object names across multiple pages for a given auction and outputs them in order.

## Parallel Execution

To speed up the scraping process, the script uses parallel execution with the help of the `ThreadPoolExecutor` from the `concurrent.futures` library. By default, the `ThreadPoolExecutor` uses the number of processors on the machine, multiplied by 5, as the maximum number of threads that can be spawned. The script allows for customization of the `max_workers` parameter, which determines the maximum number of concurrent requests.

Increasing the number of concurrent requests speeds up the scraping process, but it may put more load on the user's machine and the target website. Users should exercise caution when increasing the `max_workers` value to avoid potential issues.

## Data Extraction

The script extracts the Lot object names from the given auction pages. The Lot object names are contained within the HTML structure under the `div.row.panel.panel-primary.position-relative.m-b-0 h2 a` CSS selector. The script uses the Selenium library to load the web pages, allowing for the rendering of JavaScript content. After loading each page, the script retrieves the Lot object names and adds them to a master list. Finally, the script outputs the complete list of Lot object names for the provided auction.

Note that the script requires the Selenium and WebDriver Manager Python libraries, as well as the Google Chrome browser installed on the user's system.

## Installation

To run the project, you need to have Python 3.x installed on your system. You also need to install the required libraries, which can be done using pip:

```bash
pip install selenium webdriver-manager beautifulsoup4
```

After installing the required libraries, you can run the script provided in this project. Make sure Google Chrome is installed on your system, as the script uses Chrome as the default browser for the Selenium webdriver.