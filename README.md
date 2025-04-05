📰 VitalNews-Scraping-the-Latest-in-Health-Every-Day
📌 Overview
A fully automated web application that scrapes the latest health-related news articles from Medical News Today, stores them in a SQLite database, and displays them using a Flask-powered frontend. The scraper runs daily at 8:00 AM to ensure content is always fresh and relevant. (

⚙️ Features
✅ Automated Web Scraping using BeautifulSoup and requests

🗃️ SQLite Database Integration with deduplication logic (INSERT OR IGNORE)

⏰ Scheduled Scraping using the schedule module (runs every day at 8:00 AM)

🌐 Flask Web App to display the top 10 latest health news articles

📄 Responsive Frontend UI built with Bootstrap 5

📑 Pagination Support to browse articles by page

🧱 Tech Stack
Backend: Python, Flask

Scraping: BeautifulSoup, Requests

Database: SQLite

Scheduling: schedule

Frontend: HTML5, Bootstrap 5
🚀 How It Works
scraper.py extracts titles, dates, descriptions, and URLs of the latest news.

scheduler.py triggers scraping automatically every morning at 8:00 AM.

app.py serves a Flask app to view the 10 most recent articles with pagination.

Duplicate entries are avoided using SQL constraints.

📈 Future Improvements

🔍 Add search and category-based filters

✉️ Send daily newsletters to subscribers

🛠️ Build an admin panel for managing articles




