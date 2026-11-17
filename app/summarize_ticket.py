import anthropic

client = anthropic.Anthropic()


def summarize_ticket(ticket_text: str) -> str:
    """Shown to the agent the moment they open a ticket, so it must be fast."""
    response = client.messages.create(
        model="claude-haiku-5-5",
        max_tokens=150,
        messages=[{"role": "user", "content": f"Summarize this support ticket in two sentences:\n\n{ticket_text}"}],
    )
    return response.content[0].text
