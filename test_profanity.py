import pytest

from profanity import mask_profanity


def test_single_banned_word_in_middle_of_sentence():
    #damn 하나만
	text = "This is damn bad."
	expected = "This is d*** bad."

	assert mask_profanity(text) == expected


def test_multiple_banned_words_in_one_sentence():
    # 스펙에 있는 단어만: damn, hell, crap
	text = "damn this hell is crap"
	expected = "d*** this h*** is c***"

	assert mask_profanity(text) == expected


def test_uppercase_and_mixed_case_banned_words():

	text = "Damn hElL CRAP"
	expected = "D*** h*** C***"

	assert mask_profanity(text) == expected


def test_banned_word_followed_by_punctuation():
	text = "What the hell!"
	expected = "What the h***!"

	assert mask_profanity(text) == expected


def test_sentence_with_no_banned_words_is_unchanged():
	text = "This sentence is perfectly acceptable."

	assert mask_profanity(text) == text


def test_empty_string_returns_empty_string():
	assert mask_profanity("") == ""


def test_none_input_raises_value_error():
	with pytest.raises(ValueError):
		mask_profanity(None)
