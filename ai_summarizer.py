import os

from dotenv import load_dotenv
from google import genai

load_dotenv()


def summarize_news(article_text):
    if not article_text or len(article_text) < 40:
        return (
            "- Not enough article content was available.\n"
            "- Please open the original article for more information.\n"
            "- The news feed did not provide enough text to summarize."
        )

    api_key = os.getenv("AI_API_KEY")

    if not api_key:
        return (
            "- AI API key is not configured.\n"
            "- Add AI_API_KEY to your .env file.\n"
            "- Summary unavailable."
        )

    try:
        client = genai.Client(api_key=api_key)

        prompt = f"""You are an engineering news summarizer.

Summarize the article below into exactly THREE concise bullet points.

Rules:
- Use simple English.
- Focus on the actual engineering or technology development.
- Avoid unnecessary jargon.
- Do not invent facts.
- Each bullet should be one short sentence.
- Start every bullet with a normal hyphen (-).

Article:
{article_text}"""

        interaction = client.interactions.create(
            model="gemini-2.5-flash",
            input=prompt,
        )

       response = client.models.generate_content(
           model="gemini-2.5-flash",
           contents=prompt,
       )

return response.text.strip()

    except Exception as error:
        print(f"AI Summarization Error: {error}")

        return (
            "- The AI could not summarize this article right now.\n"
            "- The news article was retrieved successfully.\n"
            "- Open the original article using the link above."
        )
