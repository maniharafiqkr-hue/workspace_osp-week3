# OSP_03 TADD Hands-on Lab

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