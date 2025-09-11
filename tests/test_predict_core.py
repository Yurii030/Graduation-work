import pytest
from ml.src import predict_core
from ml.common import errors, validators # common 모듈에서 에러와 검증기능 임포트

@pytest.fixture(scope="module")
def model():
    return predict_core.load_model()

@pytest.mark.parametrize("text,expected", [
    ("그림을 그리고 색칠했다", "미술"),
    ("달리기와 체육 활동을 했다", "신체"),
    ("책을 읽고 이야기를 나눴다", "언어"),
    ("자석을 관찰하며 실험을 진행했다", "과학"),
])
def test_labels(model, text, expected):
    out = predict_core.predict_text(model, text)
    assert out["label"] == expected
    assert 0.0 <= out["confidence"] <= 1.0

def test_empty_text_error():
    model = predict_core.load_model()
    with pytest.raises(errors.ValidationError):  # 우리가 validators에서 던지도록 만든 예외
        validators.require_not_empty("", name="text")

def test_non_string_input_error():
    with pytest.raises(errors.ValidationError):
        validators.require_str(1234, name="text")

def test_overlength_input_error():
    long_text = "a" * 10000  # 가짜로 매우 긴 문자열
    with pytest.raises(errors.ValidationError):
        validators.limit_length(long_text, max_len=1000)