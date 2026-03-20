from fastapi.testclient import TestClient

from main import app


client = TestClient(app, raise_server_exceptions=False)


def test_post_mask_returns_unmodified_text_for_clean_input():
	response = client.post("/mask", json={"text": "hello"})

	assert response.status_code == 200
	assert response.json() == {"masked_text": "hello"}


def test_post_mask_returns_masked_text_for_banned_word_input():
	response = client.post("/mask", json={"text": "damn you"})

	assert response.status_code == 200
	assert response.json() == {"masked_text": "d*** you"}


def test_post_mask_returns_empty_string_for_empty_input():
	response = client.post("/mask", json={"text": ""})

	assert response.status_code == 200
	assert response.json() == {"masked_text": ""}


def test_post_mask_with_null_text_returns_422():
	response = client.post("/mask", json={"text": None})

	assert response.status_code == 422


def test_post_mask_with_no_body_returns_422():
	response = client.post("/mask")

	assert response.status_code == 422
