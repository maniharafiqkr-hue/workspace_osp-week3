# OSP_03 TADD 

## TADD 사이클 완성
1. **profanity.py**: Compile→RED→GREEN→REFACTOR 
2. **Web API**: Interface→RED→GREEN→REFACTOR 

## 실행 방법
```bash
pip install -r requirements.txt
uvicorn main:app --reload
```
## 테스트 
```bash
python -m pytest
# 또는
python -m pytest test_main.py
```
API Docs: http://127.0.0.1:8000/docs

## OSP_04: AI-Driven Refactoring

### 1. Identified Code Smells
1. **Primitive Obsession (Hardcoded Configuration):** `BAN_WORDS` is hardcoded as a primitive `Set[str]` directly in `profanity.py`. This makes the code rigid and hard to extend if we want to support dynamic lists or different languages.
2. **Global Data / Hidden Dependency:** Functions in `profanity.py` rely on the `BAN_WORDS` global variable. This makes unit testing difficult because we cannot easily inject a temporary mock list of banned words for a specific test.
3. **Single Responsibility Principle (SRP) Violation:** The `mask_profanity` function is doing too much. It handles input validation, defines the masking logic (via a nested function), and executes the regex replacement all at once.
4. **Inappropriate Intimacy (Nested Function):** The `_mask_match` function is nested inside `mask_profanity`. This prevents it from being unit-tested in isolation and clutters the scope of the parent function.
5. **Dependency Inversion Principle (DIP) Violation:** In `main.py`, the API route directly depends on the concrete `mask_profanity` function implementation rather than an abstraction. This makes the components tightly coupled.

### 2. AI Collaboration & Decision Process
* **AI Analysis:** AI identified 5 code smells focusing on SOLID principle violations and proposed two refactoring paths: a Functional Injection approach and an Object-Oriented (Strategy Pattern) approach.
* **Decision:** We chose to implement Strategy [A or B] because [Reason to be filled in].