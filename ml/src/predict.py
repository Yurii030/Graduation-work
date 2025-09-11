##추론 전용 파일
# 얇은 CLI 래퍼
# 입력 소스 선택: mutually_exclusive_group()로 --text,--input을 동시에 못쓰게 함
# 없으면 STDIN
# 검증 체인 : require_str->require_not_empty->limit_length(실패시 ValidationError)
# 코어 호출 : predict_core의 load_model, predict_text만 호출 ->IO와 비즈니스 로직 완전 분리.
# 응답 포맷 : 항상 responses.success/error 사용 -> JSON 모양 고정.
# 출력 옵션 : --pretty로 들여쓰기 옵션
# 오류 처리: 파일없음-> FILE_NOT_FOUND, 검증실패->VALIDATION_ERROR, 내부오류->INTERNAL_ERROR
# 내부오류는 raise 유지해 개발단계에선 트레이스 확인

# ml/src/predict.py
import sys       # STDIN/STDOUT 접근
import json      # 결과를 JSON으로 출력
import argparse  # 커맨드라인 인자 파싱을 위해 사용
from typing import Optional 

from ml.common.validators import require_str, require_not_empty, limit_length
from ml.common.responses import success, error
from ml.common.errors import ValidationError
from .predict_core import load_model, predict_text

def _read_all_stdin() -> str:
    if sys.stdin is None or sys.stdin.closed:
        return ""
    data = sys.stdin.read()
    return data if data is not None else ""

def main() -> None:
    parser = argparse.ArgumentParser(description="Diary classifier CLI")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--text", type=str, help="Input text to classify")
    group.add_argument("--input", type=str, help="Path to a UTF-8 text file")
    parser.add_argument("--pretty", action="store_true", help="Pretty-print JSON")
    args = parser.parse_args()

    # 입력 우선순위: --text > --input > STDIN
    incoming: Optional[str] = None
    if args.text and args.text.strip():
        incoming = args.text
    elif args.input:
        try:
            with open(args.input, "r", encoding="utf-8") as f:
                incoming = f.read()
        except FileNotFoundError:
            print(json.dumps(error(f"File not found: {args.input}", code="FILE_NOT_FOUND"),
                             ensure_ascii=False))
            sys.exit(2)
    else:
        incoming = _read_all_stdin()

    try:
        text = limit_length(require_not_empty(require_str(incoming), name="text"),
                            max_len=5000, name="text")

        model = load_model()
        pred = predict_text(model, text)  # {"label":..., "confidence":...}

        payload = success(pred["label"], pred["confidence"],
                          meta={"engine": "rules", "model_version": model.get("_version", "0.1.0")})
        print(json.dumps(payload, ensure_ascii=False, indent=2 if args.pretty else None))

    except ValidationError as ve:
        print(json.dumps(error(str(ve), code="VALIDATION_ERROR"), ensure_ascii=False))
        sys.exit(2)
    except Exception:
        # 개발 단계: 내부 에러 코드로 감추되, 트레이스는 콘솔에 남기고 싶다면 raise 유지
        print(json.dumps(error("Unexpected error occurred", code="INTERNAL_ERROR"),
                         ensure_ascii=False))
        raise

if __name__ == "__main__":
    main()