# ml/src/predict_core.py
# 순수 비즈니스 로직
# 텍스트-> 라벨/신뢰도" 핵심 추론만 담당.
# 여기만 바꾸면 규칙->Sklearn->HuggingFace등 자유롭게 교체 가능(입출력 레이어는 건드릴 필요x)
# 사용 예) model=load_model() -> predict_text(model,text)
# 주의 : 지금은 더미 규칙 실제 모델 연결 시에도 리턴 스키마는 유지해주면 상위 레이어 더 안정적.


from typing import Dict, Any

def load_model() -> Dict[str,Any]:
    # ToDo : 실제모델 로딩(hf/sklearn)로 교체가능
    return {"kind":"rules","_version":"0.1.0"}

def predict_text(model:Dict[str,Any],text:str)->Dict[str,Any]:
    # ToDo : 실제모델 예측코드로 교체가능
    t= text.lower()
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

    return {"label":label,"confidence":conf}