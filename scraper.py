import requests
from bs4 import BeautifulSoup
import sqlite3
from datetime import datetime

def scrape_health_news():
    #  it will Connect to SQLite database
    conn = sqlite3.connect("health_news.db")
    cursor = conn.cursor()

    # Base URL for scraping
    base_url = "https://www.medicalnewstoday.com"
    url = f"{base_url}/news"

    # Lists to store data
    date_list, title_list, desc_list, news_urls = [], [], [], []
     
    while url:
        print(f"Scraping: {url}")
        
        try:
            r = requests.get(url, timeout=10)
            r.raise_for_status()
        except requests.RequestException as e:
            print(f"Error fetching page: {e}")
            break

        soup = BeautifulSoup(r.text, "html.parser")

        # Extract dates
        dates = soup.find_all("div", class_="css-19hhrie")
        date_list.extend([i.text.strip() for i in dates])

        # Extract titles
        titles = soup.find_all("a", class_="css-aw4mqk")
        title_list.extend([i.text.strip() for i in titles])

        # Extract descriptions
        descriptions = soup.find_all("p", class_="css-1hw29i9")
        desc_list.extend([i.text.strip() for i in descriptions])



        # Extract news URLs
        links = soup.find_all("a", class_="css-aw4mqk")
        for i in links:
            link = i.get("href")
            if link.startswith("http"):
                news_urls.append(link)
            else:
                news_urls.append(base_url + link)

        # Ensure all lists are the same length
        min_length = min(len(date_list), len(title_list), len(desc_list), len(news_urls))
        date_list, title_list, desc_list, news_urls = (
            date_list[:min_length],
            title_list[:min_length],
            desc_list[:min_length],
            news_urls[:min_length],
        )
        # Find next page link
        next_page = soup.find("a", class_="css-aw4mqk")
        if next_page:
            next_url = next_page.get("href")
            url = base_url + next_url if not next_url.startswith("http") else next_url
        else:
            break

    # Convert date format to YYYY-MM-DD
    for i in range(len(date_list)):
        try:
            formatted_date = datetime.strptime(date_list[i], "%B %d, %Y").strftime("%Y-%m-%d")
            date_list[i] = formatted_date
        except ValueError:
            print(f"Skipping invalid date: {date_list[i]}")
            date_list[i] = None
    # Insert data into SQLite
    if min_length > 0:
        inserted_count = 0
        for i in range(min_length):
            try:
                cursor.execute("""
                    INSERT OR IGNORE INTO news (date, title, description, news_url) 
                    VALUES (?, ?, ?, ?)
                """, (date_list[i], title_list[i], desc_list[i], news_urls[i]))

                if cursor.rowcount > 0:
                    print(f"Inserted: {title_list[i]}")
                    inserted_count += 1
                else:
                    print(f"Skipped (duplicate): {title_list[i]}")

            except sqlite3.Error as e:
                print(f"Error inserting {title_list[i]}: {e}")

        print(f"Inserted {inserted_count} new articles into the database.")
        conn.commit()

    conn.close()
    print("Database connection closed.")

# If the script is run directly, scrape news immediately
if __name__ == "__main__":
    scrape_health_news()






