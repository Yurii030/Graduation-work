# 입력 타입/빈값/길이 체크를 "작고 확실한함수"들로 쪼개기
# 예측/학습/웹 레이어 어디서든 import 가능
# 에러는 errors.ValidationError로 통일
# 텍스트의 타입/공백/길이 체크
# 쓰기전에 한번 걸러서, 코어 로직이 깨끗한 입력만 받고록 보장하기 위해
# 사용 예 : text=limit_length(require_not_empty(require_str(incoming),name="text"),max_len=5000,name="text")
# 주의 : 길이 제한(기본 5000)은 필요에 따라 조정

# ml/common/validators.py
from .errors import ValidationError

def require_str(value,name="text"):
    if not isinstance(value,str):
        raise ValidationError(f"{name} must be a string")
    return value

def require_not_empty(value:str,name="text",strip=True):
    v= value.strip() if strip and isinstance(value, str)else value
    if not v:
        raise ValidationError(f"{name} must not be empty")
    return v
def limit_length(value: str, max_len=5000, name="text"):
    if len(value)>max_len:
        raise ValidationError(f"{name}exceeds max length{max_len}")
    return value