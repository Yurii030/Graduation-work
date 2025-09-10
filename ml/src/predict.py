##추론 전용 파일
#ml/src/predict.py
import sys       # STDIN/STDOUT 접근
import json      # 결과를 JSON으로 출력
import argparse  # 커맨드라인 인자 파싱을 위해 사용
from typing import Dict # 타입힌트(가독성)

# (1) 더미 모델 로딩 자리 : 나중에 실제 모델 로딩 코드로 교체)
def load_model():
    """
    Todo : 실제모델/벡터라이저/토크나이저 로드.
    에: joblib.load('models/tfidf_svm.joblib')또는 HF 토크나이저/모델
    """
    return{"_dummy":True}

# (2) 더미 예측 로직 : 나중에 실제 추론으로 교체
def real_predict(model, text: str) -> Dict:
    """
    Todo : 실제 모델을 사용한 예측으로 대체
    지금은 키워드 기반의 간단한 규칙으로 label/confidence 생성
    """
    t= text.lower()
    # 아주 간단한 규칙
    if any(k in t for k in["그림","색칠","미술","paint","draw"]):
        label = "미술"
        conf = 0.85
    elif any(k in t for k in["뛰","달리","체육","운동","몸"]):
        label = "신체"
        conf = 0.8
    elif any(k in t for k in["책","말","읽기","동화","story"]):
        label = "언어"
        conf = 0.82
    elif any(k in t for k in["탐구","실험","관찰","자석","bug"]):
        label = "과학"
        conf = 0.78
    else:
        label = "기타"
        conf = 0.5

    return{"label":label,"confidence":conf}


# (3) 엔트리 포인트 : 인자 처리 -> 예측 -> JSON 출력
def main() :
    # ArgumentParser 생성,--text 옵션정의
    parser = argparse.ArgumentParser(description="Diary classifier(dummy)")
    # 'text'를 선택인자로: 없으면 STDIN 또는 예시 문장 사용
    parser.add_argument("text",nargs="?",type=str,help="Input text to classify")
    args = parser.parse_args() ##인자파싱

    # 입력은 두 경로 중 하나로 받음 : --text 또는 STDIN
    if args.text and args.text.strip():
        incoming = args.text.strip()
    else : ##없을땐 sys.stdin.read()로 표준입력에서 읽음
        # 파이프나 shell_exec에서 STDIN으로 들어온 텍스트 자리
        incoming = sys.stdin.read().strip() 

    if not incoming :
        # 비어 있으면 예시 텍스트 사용(디버깅 편의)
        incoming = "예시 문장"

    model = load_model()  # (1) 모델로드(현재는 더미)
    result = real_predict(model, incoming) #(2) 예측 실행

    # JSON으로 표준출력에 결과 출력
    # ensure_aascii=False 한글이 \ud55c같은 이스케이프가 아니라 그대로 출력되게 함
    print(json.dumps(result,ensure_ascii=False))
    
## 이 파일을 스크립트로 실행했을 때만 main()을 호출
## 모듈로 임포트될 때는 실행되지 않음->테스트/재사용에 유리
if __name__ == "__main__":
    main()