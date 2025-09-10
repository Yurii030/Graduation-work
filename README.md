# 유아일지 자동 분류 웹 애플리케이션

> ✅ **1차 리팩토링 머지 완료** (2025-09-10)  
> 기존 졸업작품을 도메인 기반으로 구조화하고, PHP ↔ Python 추론 브릿지(`predict.py`)까지 연결했습니다.

---

## 📌 프로젝트 개요
유치원/어린이집의 **유아일지**를 분야별(신체·미술·언어·과학 등)로 자동 분류하고,  
웹에서 **일지 작성 / 조회 / 분석(차트)** 기능을 제공합니다.

- **웹 프론트엔드**: PHP + HTML + CSS + JS  
- **백엔드 로직**: PHP includes (도메인별 분리)  
- **머신러닝**: Python (기본 분류기 + 확장 예정: TF-IDF, BERT, LLM Zero/Few-shot)

---

## 🔧 변경 하이라이트
- `web/` 구조 정리: `config/`, `public/`(뷰) ↔ `public/includes/`(로직)
- 도메인 분리: `includes/{activity, auth, chart, diary, kind, common}`
- 네이밍 통일: `*_db.php` → 의미 있는 `*_action.php`/기능명
- `ml/` 디렉토리 신설: `configs/`, `src/{predict, train, utils, models}`, `requirements.txt`
- PHP에서 Python 스크립트 호출(`ml_client.php`) → JSON 반환 확인

---
## 폴더 스냅샷
<img width="251" height="598" alt="image" src="https://github.com/user-attachments/assets/0321bf06-95f9-46f6-975a-a7d4f8f5253d" />
<img width="264" height="509" alt="image" src="https://github.com/user-attachments/assets/e4934387-b0bb-4f7d-8e21-7c88adce8459" />

<sub>예: 터미널 예측 결과</sub> 
<img width="715" height="31" alt="image" src="https://github.com/user-attachments/assets/cc2955ca-76b1-46e8-8030-6c8439d171a4" />

## 빠른 시작
### 1) ML 환경
```bash
conda activate diary-ml
python -m pip install -r ml/requirements.txt
python ml/src/predict.py "오늘은 책을 읽었어요"   # ⇒ {"label":"언어","confidence":0.82}

### 2) PHP 개발 서버
cd web
php -S localhost:8000 -t public
# 브라우저: http://localhost:8000/ml_test.php  (테스트 페이지가 있는 경우)
참고: web/public/includes/common/ml_client.php에서 Python 경로를 환경에 맞게 수정
(현재 예시: C:\Users\taddy\anaconda3\envs\diary-ml\python.exe)

## 개발 메모
DB 스키마 변경 없음
진입점은 web/public/*로 통일 (직접 접근 경로 변경 주의)
Windows 줄바꿈(CRLF) 경고는 .gitattributes/core.autocrlf로 정리 예정
---

🧭 진행 내역

 - config 분리 (db.php, session.php)

 - 도메인별 includes 생성 (activity, auth, chart, diary, kind, common)

 - 네이밍 정리 (*_db.php → *_action.php/기능명)

 - public(화면) / includes(로직) 분리

 - ML 디렉토리 구성 및 기본 추론 브릿지 연결(predict.py)

## 로드맵

 - [ ] FastAPI /predict로 전환(프로세스 호출 → HTTP 호출)

 - [ ] includes/common 유틸(입력 검증, 공통 JSON 응답) 정리

 - [ ] LLM zero/few-shot 실험 및 성능 비교 리포트

 - [ ] .gitignore 보강 및 산출물 디렉토리 표준화(ml/models, ml/reports, web/public/uploads 등)

---

## 개발 메모

- DB 스키마 변경 없음

- 진입점은 web/public/*로 통일(직접 접근 경로 변경 주의)

- Windows 줄바꿈(CRLF) 경고는 .gitattributes/core.autocrlf로 정리 예정


## 👤 작성자

이름: 김유리

목적: 졸업작품 리팩토링 + 포트폴리오용 정리
