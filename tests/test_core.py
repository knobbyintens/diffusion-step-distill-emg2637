from src.distill import build_model


def test_build_model():
    assert build_model()["status"] == "release"
