from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

def fetch_news(limit=10, offset=0):
    conn = sqlite3.connect("health_news.db")
    cursor = conn.cursor()
    cursor.execute("SELECT date, title, description, news_url FROM news ORDER BY date DESC LIMIT ? OFFSET ?", (limit, offset))
    news_list = cursor.fetchall()
    conn.close()
    return news_list

@app.route("/")
def index():
    page = request.args.get("page", 1, type=int)  # Get the current page number
    limit = 10  # Number of articles per page
    offset = (page - 1) * limit  # Calculate the offset

    news = fetch_news(limit, offset)
    return render_template("index.html", news=news, page=page)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000, debug=True)

