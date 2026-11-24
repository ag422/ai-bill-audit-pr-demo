import anthropic

client = anthropic.Anthropic()

CATEGORIES = ["billing", "bug", "feature request", "other"]


def tag_ticket(ticket_text: str) -> str:
    """Sorts an incoming support ticket into one category."""
    response = client.messages.create(
        model="claude-opus-5-5",
        max_tokens=10,
        messages=[
            {
                "role": "user",
                "content": f"Classify this support ticket as one of: {', '.join(CATEGORIES)}. Reply with the category only.\n\n{ticket_text}",
            }
        ],
    )
    return response.content[0].text.strip().lower()
