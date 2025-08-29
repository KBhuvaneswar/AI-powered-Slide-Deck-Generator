from ddgs import DDGS

def search_web(topic: str, num_results: int = 5):
    """
    Search the web for a given topic using DuckDuckGo.
    
    Args:
        topic (str): Search topic
        num_results (int): Number of results to return

    Returns:
        list[dict]: Each result contains {title, href}
    """
    results = []
    with DDGS() as ddgs:
        for r in ddgs.text(topic, max_results=num_results):
            results.append({
                "title": r.get("title"),
                "url": r.get("href")
            })
    return results
