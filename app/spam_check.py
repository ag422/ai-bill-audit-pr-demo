import anthropic

client = anthropic.Anthropic()


def is_spam(message: str) -> bool:
    """Returns True if an incoming support message is spam."""
    response = client.messages.create(
        model="claude-opus-5-5",
        max_tokens=5,
        messages=[{"role": "user", "content": f"Is this message spam? Answer only yes or no.\n\n{message}"}],
    )
    return response.content[0].text.strip().lower().startswith("yes")
