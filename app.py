from flask import Flask, jsonify, send_from_directory

from categories import BRANCH_MAPPINGS
from news_fetcher import get_news
from data_cleaner import clean_article_text
from ai_summarizer import summarize_news


app = Flask(__name__)


# =========================
# FRONTEND
# =========================

@app.route("/")
def home():
    return send_from_directory("frontend", "index.html")


@app.route("/<path:filename>")
def frontend_files(filename):
    return send_from_directory("frontend", filename)


# =========================
# NEWS API
# =========================

@app.route("/api/news")
def get_latest_news():

    from flask import request

    branch = request.args.get(
        "category",
        "Artificial Intelligence"
    )

    if branch not in BRANCH_MAPPINGS:
        return jsonify({
            "error": "Invalid category"
        }), 400

    articles = get_news(
        BRANCH_MAPPINGS[branch],
        limit=3
    )

    news = []

    for article in articles:

        cleaned_description = clean_article_text(
            article["description"]
        )

        summary = summarize_news(
            cleaned_description
        )

        news.append({
            "title": article["title"],
            "link": article["link"],
            "source": article["source"],
            "description": cleaned_description,
            "summary": summary
        })

    return jsonify(news)


# =========================
# START SERVER
# =========================

if __name__ == "__main__":
    app.run(debug=True)