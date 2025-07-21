# Crawl-ML

Scrapy project for web scraping and machine learning.

Scraping useful information from Alcohol Beverage Control (ABC) to be injested into a machine learning model on DataBricks.

## Setup

1. Clone the repository
    ```bash
    git clone https://github.com/silakonsyko/crawl-ml.git
    cd crawl-ml
    ```
2. Create a virtual environment
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```
3. Install dependencies
    ```bash
    pip install -r requirements.txt
    ```
4. Run the scraper
    ```bash
    scrapy crawl abc_news -o news_data.json
    ```
5. 

