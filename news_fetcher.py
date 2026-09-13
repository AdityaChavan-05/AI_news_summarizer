import requests
import xml.etree.ElementTree as ET
from urllib.parse import quote


def get_news(query, limit=5):
    url = (
        "https://news.google.com/rss/search?"
        f"q={quote(query)}&hl=en-IN&gl=IN&ceid=IN:en"
    )

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        response = requests.get(
            url,
            headers=headers,
            timeout=30
        )

        response.raise_for_status()

        root = ET.fromstring(response.content)

        articles = []

        for item in root.findall("./channel/item")[:limit]:
            source_element = item.find("source")

            if source_element is not None and source_element.text:
                source = source_element.text
            else:
                source = "Unknown source"

            articles.append({
                "title": item.findtext(
                    "title",
                    default="No title"
                ),
                "link": item.findtext(
                    "link",
                    default=""
                ),
                "description": item.findtext(
                    "description",
                    default=""
                ),
                "source": source
            })

        return articles

    except requests.RequestException as error:
        print(f"News request failed: {error}")
        return []

    except ET.ParseError as error:
        print(f"Could not read news feed: {error}")
        return []