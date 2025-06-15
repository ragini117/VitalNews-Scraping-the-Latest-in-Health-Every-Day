import schedule
import time
from scraper import scrape_health_news  

# Schedule the scraper to run every day at 8'o clock
schedule.every().day.at("08:00").do(scrape_health_news)

print("Scheduler started. Scraping will run every day at 8:00.")

while True:
    schedule.run_pending()
    time.sleep(60)  # Check every minute
