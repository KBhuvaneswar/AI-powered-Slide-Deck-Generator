from modules.search import search_web
from modules.scrape import scrape_url
from modules.llm import summarize_article
from modules.slides import generate_slide_outline
from modules.pptx import create_pptx

if __name__ == "__main__":
    topic = input("Enter topic: ")
    results = search_web(topic, num_results=5)
    summaries = []
    
    for r in results:
        text = scrape_url(r["url"])
        if not text:
            print("Could not extract text from:", r["url"])
            continue

        summary = summarize_article(text, r["title"], topic)
        summaries.append(summary)

    slides = generate_slide_outline(summaries)
    create_pptx(slides, topic.replace(" ", "_") + ".pptx")