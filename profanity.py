"""
Profanity masking utility for educational TADD exercise.
"""

import re
from typing import Set

# Constants
BAN_WORDS: Set[str] = {"damn", "hell", "crap"}
WORD_PATTERN: str = r"\b([A-Za-z]+)\b"


def mask_profanity(text: str) -> str:
    """
    Masks banned words in text, preserving first letter and structure.
    
    Args:
        text: Input text to process
        
    Returns:
        Text with banned words masked (e.g., "damn" -> "d***")
        
    Raises:
        ValueError: If text is None
    """
    if text is None:
        raise ValueError("text cannot be None")
    
    if not text:  # Handles "" and other falsy strings
        return ""
    
    def _mask_match(match: re.Match[str]) -> str:
        word = match.group(1)
        if word.lower() in BAN_WORDS:
            return word[0] + "*" * (len(word) - 1)
        return word
    
    return re.sub(WORD_PATTERN, _mask_match, text)
