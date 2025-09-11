# 커스텀 예외 정의(ValidationError,ModelLoadError 등)
# 명확한 예외 계층
# 도메인별 예외를 정의
# except ValidationError처럼 타입별로 깔끔히 분기 가능-> 사용자 메세지/종료코드 제어 쉬움
# 검증 실패 시 raise ValidationEoor(""), 모델 로드실패시 ModelLoadError등에 사용
#ml/common/errors.py

class AppError(Exception):
    """모든 커스텀 예외의 베이스 클래스"""
    pass    
class ValidationError(AppError):
    """입력값 검증 실패"""
    pass
class ModelLoadError(AppError):
    """모델 로딩 실패"""
    pass
class InferenceError(AppError):
    """추론 실패"""
    pass