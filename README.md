# Web Scraping and Dashboard Project with Scrapy, Pandas, and Streamlit

This project demonstrates the process of web scraping data on men's sneakers from Mercado Livre using Scrapy, data processing with Pandas, storing the data in a SQLite database, and building an interactive dashboard with Streamlit. It showcases a complete data journey, from collection to visualization.

## Project Structure

1. **Web Scraping with Scrapy**
   - The project uses Scrapy to extract information on men's sneakers from Mercado Livre.
   - Data collected includes: brand, rating, and price of products.
   - The scraper is configured to traverse the first 10 pages of results.

2. **Data Processing with Pandas**
   - After data collection, Pandas is used to clean and prepare the data for analysis.
   - Cleaning processes include removing duplicates and handling missing values.

3. **Storage with SQLite**
   - Processed data is stored in an SQLite database.
   - This allows for efficient querying and manipulation of data for further analysis.

4. **Interactive Dashboard with Streamlit**
   - Streamlit is used to create an interactive and visual dashboard.
   - The dashboard enables data visualization and analysis, facilitating insights and comparisons.

## How to Run the Project

### Prerequisites

- Python 3.x
- Scrapy
- Pandas
- SQLite
- Streamlit

### Reference

This project is inspired by Luciano Galvão’s data journey. For more information on data collection and analysis, check out the video:
https://www.youtube.com/watch?v=qNu1VCtUedg

