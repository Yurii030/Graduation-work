# 유아일지 자동 분류 웹 애플리케이션

⚠️ 현재 리팩토링 진행 중입니다.  
기존 졸업작품 코드를 구조화하여 **도메인별 폴더 분리, 네이밍 통일, 공통 모듈 분리**를 진행했습니다.  
아직 일부 공통 함수 및 ML 연동 부분은 작업 예정입니다.

---

## 📌 프로젝트 개요
이 프로젝트는 유치원/어린이집에서 작성되는 **유아일지**를 분야별(신체, 미술, 언어, 과학 등)로 자동 분류하고,  
웹 애플리케이션을 통해 **일지 작성 / 조회 / 분석(차트)** 기능을 제공하는 시스템입니다.

- **웹 프론트엔드**: PHP + HTML + CSS + JS  
- **백엔드 로직**: PHP includes (도메인별로 분리)  
- **머신러닝 모델(이미 있음+구조화/연동 예정)**: Python (TF-IDF, BERT, LLM Zero-shot/Few-shot)

---

## 📂 현재 폴더 구조 (리팩토링 후)

web/
├─ assets/ # 정적 파일(css, js, img)
├─ config/ # 환경 설정
│ ├─ db.php
│ └─ session.php
├─ includes/ # 도메인별 로직 처리
│ ├─ activity/
│ │ ├─ act_book.php
│ │ ├─ act_info.php
│ │ └─ act_toy.php
│ ├─ auth/
│ │ ├─ login_action.php
│ │ ├─ signup_action.php
│ │ ├─ profile_update.php
│ │ ├─ logout.php
│ │ └─ withdrawal.php
│ ├─ chart/
│ │ ├─ data_action.php
│ │ └─ diary_chart.php
│ ├─ diary/
│ │ ├─ diary.php
│ │ ├─ diary_list.php
│ │ ├─ diary_view.php
│ │ ├─ diary_write.php
│ │ └─ diary_write_update.php
│ ├─ kind/
│ │ ├─ create_action.php
│ │ ├─ update_action.php
│ │ ├─ kind_insert.php
│ │ ├─ kind_update.php
│ │ ├─ kind_delete.php
│ │ ├─ kind_view.php
│ │ └─ kind_inq.php
│ └─ common/ # (공통 함수 예정)
└─ public/ # 사용자 진입 페이지
├─ index.php
├─ login.php
├─ sign_up.php
├─ my_info.php
└─ ...

---

## ✨ 리팩토링 내용
- [x] **config 분리** → DB 연결(`db.php`), 세션 관리(`session.php`)를 `web/config/`로 이동  
- [x] **도메인별 includes 폴더 생성** → `auth`, `diary`, `kind`, `chart`, `activity`  
- [x] **네이밍 정리** → `_db.php` 접미사 제거, `*_action.php` 또는 의미 있는 이름으로 변경  
- [x] **public / includes 분리** → `public`은 화면/폼, `includes`는 데이터 처리/로직 전담  
- [x] **머신러닝 모델 코드 포함** → `train.py`, `Classf.py`, `2Vec.py` 등 Python 기반 분류기 이미 존재  
- [ ] **ML 코드 구조화** → `ml/src/`, `ml/configs/`, `ml/reports/`로 정리 예정  
- [ ] **웹 연동** → PHP → Python(FastAPI) API 호출 방식으로 통합 예정  
- [ ] **LLM 실험** → Zero-shot/Few-shot 분류 및 성능 비교 계획


---

## 🚀 실행 방법 (개발 단계)
1. PHP 내장 서버 실행 (테스트용)
   ```bash
   cd web
   php -S localhost:8000 -t public
2. 브라우저에서 http://localhost:8000 접속

## 🗺️향후 계획

 공통 유틸(common): 입력 검증, JSON 응답, 보안 유틸 정리

 로그/예외 처리: 공통 에러 핸들러 추가

 ML API 연동: includes/common/ml_client.php 추가 → Python FastAPI 모델 호출

 LLM 적용: Zero-shot/Few-shot 분류 실험 및 성능 비교

## 👤 작성자

이름: 김유리

목적: 졸업작품 리팩토링 + 포트폴리오용 정리
