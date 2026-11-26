import pytest

from hackathon_26.scoring import calculate


class TestCalculate:
    @pytest.mark.parametrize(
        ("predicted_keywords", "actual_keywords", "expected_score"),
        [
            pytest.param(1, 1, 1000, id="exact_match_is_full_score"),
            pytest.param(30, 20, 667, id="rounds_to_nearest"),
            pytest.param(100, 10, 100, id="ten_percent"),
            pytest.param(300, 1, 3, id="worst_case_near_zero"),
        ],
    )
    def test_correct_score_given(self, predicted_keywords: int, actual_keywords: int, expected_score: int) -> None:
        assert calculate(predicted_keywords, actual_keywords) == expected_score

    def test_same_ratio_gives_same_score(self) -> None:
        assert calculate(10, 5) == calculate(200, 100)


class TestCalculateInvalidInput:
    @pytest.mark.parametrize(
        ("predicted_keywords", "actual_keywords"),
        [
            pytest.param(5, 6, id="actual_exceeds_prediction"),
            pytest.param(5, -1, id="negative_actual"),
        ],
    )
    def test_raises_value_error(self, predicted_keywords: int, actual_keywords: int) -> None:
        with pytest.raises(ValueError, match="actual keywords must be between"):
            calculate(predicted_keywords, actual_keywords)
