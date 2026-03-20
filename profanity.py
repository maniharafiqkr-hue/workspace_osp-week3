import re


def mask_profanity(text: str) -> str:
    if text is None:
        raise ValueError("text cannot be None")

    if text == "":
        return ""

    banned_words = {"damn", "hell", "crap"}
    pattern = r"\b([A-Za-z]+)\b"

    def _mask_match(match: re.Match[str]) -> str:
        word = match.group(1)
        if word.lower() in banned_words:
            return word[0] + "*" * (len(word) - 1)
        return word

    return re.sub(pattern, _mask_match, text)
