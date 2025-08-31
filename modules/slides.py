from modules.llm import generate_text

SLIDE_PROMPT = """
You are an AI assistant that structures content into a 7-slide presentation.
You have two sources of information:
1. Web search results (Summaries).
2. Your own general knowledge as a large language model. 

Task: Combine both sources to create a 7-slide outline. 
Each slide should have a clear title and 5 bullet points. 
Ensure the outline is accurate, up-to-date, and engaging.
Each slide except Slide 1 (Title slide) must be structured as:
- {{title}}: a concise slide title
- {{bullets}}: 3–5 bullet points

Summaries:
{summaries}

Generate slides in JSON format:
[
  {{
    "title": "Slide Title",
    "bullets": ["Point 1", "Point 2"]
  }}, ...
]

Structure the slides with this flow:
Slide 1: Title (This slide should have the main presentation title. 
Make it catchy and relevant to the topic. 
Avoid bullet points only for this slide. But this slide should also be in JSON format.)

Slide 2: Overview

Slide 3–6: Key points / trends / arguments

Slide 7: Conclusion / Takeaways

Return only valid JSON. Do not include explanations, markdown, code fencing, backticks, extra text.
"""

def generate_slide_outline(summaries: list[str]) -> list[dict]:
    """
    Takes multiple summaries and converts them into a structured 7-slide outline.
    """
    prompt = SLIDE_PROMPT.format(summaries="\n".join(summaries))
    response = generate_text(prompt)

    import json
    slides = json.loads(response)
    return slides
