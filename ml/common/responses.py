# 성공/에러 응답 포맷을 단일 스키마로 고정
# 어떤 레이어도 같은 JSON모양 유지
# meta에 버전/엔진/추가정보를 넣되 키 이름 고정
# 모든 출력 JSON의 모양을 고정해주는 헬퍼
# meta는 엔진/버전/추가 힌트를 넣는 용도.

# ml/common/responses.py
from typing import Dict, Any, Optional

def success(label: str,confidence:float, meta: Optional[Dict[str,Any]]=None)->Dict[str,Any]:
    """성공 응답 포맷"""
    return{
        "ok":True,
        "result" :{"label":label,"confidence":confidence},
        "meta": meta or {}
    }
  
def error(message: str, code: int=400, meta: Optional[Dict[str,Any]]=None)->Dict[str,Any]:
    """에러 응답 포맷"""
    return{
        "ok":False,
        "error":{"message":message,"code":code},
        "meta": meta or {}
    }