from categories import BRANCH_MAPPINGS
from news_fetcher import get_news
from data_cleaner import clean_article_text
from ai_summarizer import summarize_news


def main():
    print("=" * 60)
    print("        AI ENGINEERING NEWS SUMMARIZER")
    print("=" * 60)

    print("\nAvailable branches:")

    for number, branch in enumerate(BRANCH_MAPPINGS, start=1):
        print(f"{number}. {branch}")

    choice = input(
        "\nChoose a branch number "
        "(or press Enter for all): "
    ).strip()

    if choice:
        try:
            index = int(choice) - 1
            branches = [
                list(BRANCH_MAPPINGS.keys())[index]
            ]

        except (ValueError, IndexError):
            print("Invalid choice. Please run the program again.")
            return

    else:
        branches = list(BRANCH_MAPPINGS.keys())

    for branch in branches:

        print("\n" + "=" * 60)
        print(f"NEWS FOR: {branch.upper()}")
        print("=" * 60)

        articles = get_news(
            BRANCH_MAPPINGS[branch],
            limit=3
        )

        if not articles:
            print("No articles found.")
            continue

        for number, article in enumerate(
            articles,
            start=1
        ):

            print(f"\n[{number}] {article['title']}")
            print(f"Source: {article['source']}")
            print(f"Link: {article['link']}")

            text = clean_article_text(
                article["description"]
            )

            summary = summarize_news(text)

            print("\nSummary:")
            print(summary)

            print("-" * 60)


if __name__ == "__main__":
    main()