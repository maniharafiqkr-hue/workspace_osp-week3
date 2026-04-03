"""
Profanity masking utility for educational TADD exercise.
"""
import re
from typing import Set, Optional

class ProfanityFilter:
    def __init__(self, banned_words: Optional[Set[str]] = None):
        # Fixes Smells 1 & 2: No more global/hardcoded variables. 
        # Banned words are now injected, defaulting to our standard list.
        self.banned_words = banned_words or {"damn", "hell", "crap"}
        self.word_pattern = re.compile(r"\b([A-Za-z]+)\b")

    # Fixes Smell 4: Extracted the nested function into a proper method.
    def mask_match(self, match: re.Match) -> str:
        word = match.group(1)
        if word.lower() in self.banned_words:
            return word[0] + "*" * (len(word) - 1)
        return word

    # Fixes Smell 3: This method now only coordinates the masking.
    def mask_profanity(self, text: str) -> str:
        if text is None:
            raise ValueError("text cannot be None")
        
        if not text: 
            return ""
        
        return self.word_pattern.sub(self.mask_match, text)