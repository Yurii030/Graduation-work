# 🧸 유아일지 자동 분류 프로젝트

⚠️ 현재 **리팩토링 진행 중**입니다.  
코드 구조와 실행 방식이 변경되고 있으며, 일부 기능은 안정화되지 않았습니다.  
(예상 완료: 2025년 11월 말)

---

## 📖 프로젝트 소개
유치원/어린이집에서 작성되는 **유아일지**를  
자연어처리 기법을 통해 분야별(신체, 미술, 언어, 과학 등)로 자동 분류하는 모델입니다.  

현재는 **규칙 기반 분류기**와 **TF-IDF + SVM baseline 모델**을 지원하며,  
향후 BERT 및 LLM 기반 분류 실험까지 확장할 예정입니다.

---

## 📂 프로젝트 구조
ml/
├── common/ # 공통 유틸 (validators, responses, errors)
├── configs/ # 설정 파일 (baseline.yaml, bert.yaml)
└── src/ # 실행 코드
├── predict_core.py # 순수 예측 로직
├── predict.py # CLI 실행 진입점
├── train.py # 학습 스크립트
└── utils.py
web/ # 웹 관련 코드 (프론트/백엔드)
reports/ # 실험 로그/리포트


---

## ✅ 리팩토링 진행 상황
- [x] 프로젝트 구조 재정리 (`src/`, `configs/`, `reports/`)
- [x] TF-IDF + SVM baseline 구현
- [x] 테스트 자동화 환경 구축 (pytest)
- [ ] 로깅 및 실험 기록 자동화
- [ ] BERT 기반 모델 적용
- [ ] FastAPI 추론 서버 배포
- [ ] **LLM 기반 Zero-shot/Few-shot 분류 실험**

---

## 🛣 로드맵
1. 데이터 파이프라인 정리  
2. Baseline 모델 → BERT 모델 확장  
3. 실험 관리 자동화 (로그/리포트)  
4. 추론 서버화 (FastAPI)  
5. **LLM 기반 실험**
   - Zero-shot/Few-shot 프롬프트 분류  
   - 한국어 LLM (예: KoAlpaca, LLaMA2-ko) 시범 적용  
   - 성능 비교 및 한계 분석  

---

## ⚙️ 설치 방법

권장: Python 3.10+

```bash
pip install -r requirements.txt
```
## 🚀 실행 방법

### 1) CLI 추론 (규칙 기반)
```bash
단일 문장 분류
python -m ml.src.predict --text "아이들이 동화를 읽고 이야기를 나눴다"
```
### STDIN 입력
```bash
echo "자석을 관찰하며 실험을 진행했다" | python -m ml.src.predict
```

### 파일 입력
```bash
python -m ml.src.predict --input samples/sample.txt
```
### Pretty JSON 출력
```bash
python -m ml.src.predict --text "색칠 활동" --pretty
```
## 📚 학습 (Baseline)
```bash
python ml/src/train.py --config ml/configs/baseline.yaml
```

💡 현재는 baseline 모델만 지원됩니다.
리팩토링이 끝나면 BERT 기반 학습 및 추론 코드도 추가될 예정입니다.

## ⚙️ 설정

규칙 기반 키워드는 ml/configs/baseline.yaml에 정의되어 있습니다.

rules:
  미술: ["그림", "색칠", "미술", "paint", "draw"]
  신체: ["뛰", "달리기", "운동", "체육", "몸"]
  언어: ["책", "말", "읽기", "동화", "story"]
  과학: ["탐구", "실험", "관찰", "자석", "bug"]
  기타: []

## 🧪 테스트
pytest tests/

테스트 종류:
✅ 정상 입력 케이스 (각 카테고리별 문장 분류)
✅ 에러 케이스 (빈 입력, 문자열이 아님, 과도하게 긴 입력 등)

## 🚀 향후 계획

리팩토링 완료 이후 단계적으로 다음 작업을 진행할 예정입니다.

### 1. 모델 고도화
- [ ] 📝 Zero-shot / Few-shot 프롬프트 엔지니어링  
- [ ] 🇰🇷 한국어 특화 LLM 적용 (예: KoAlpaca, LLaMA2-ko 등)  
- [ ] ⚡ Fine-tuning / LoRA 기반 경량 학습 시도  

### 2. 성능 및 비용 분석
- [ ] 📊 기존 BERT 모델과 LLM 성능 비교  
- [ ] 💰 추론 비용 및 자원 효율성 분석  

### 3. 시스템화
- [ ] 🌐 FastAPI 기반 추론 서버 배포  
- [ ] 📑 실험 로그/리포트 자동화 및 대시보드 구축  

