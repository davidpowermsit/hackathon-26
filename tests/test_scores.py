import pytest

from hackathon_26.scoring import calculate


class TestCalculate:
    @pytest.mark.parametrize(
        ("keywords", "steps", "expected_score"),
        [
            pytest.param(2, 2, 1000, id="all_keywords_used_is_full_score"),
            pytest.param(3, 2, 667, id="rounds_to_nearest"),
            pytest.param(10, 1, 100, id="few_keywords_used"),
            pytest.param(0, 0, 1000, id="no_keywords_besides_target"),
        ],
    )
    def test_found_target(self, keywords: int, steps: int, expected_score: int) -> None:
        assert calculate(True, keywords, steps) == expected_score

    def test_stuck_scores_zero(self) -> None:
        assert calculate(False, 3, 2) == 0

    @pytest.mark.parametrize(
        ("keywords", "steps"),
        [
            pytest.param(5, 6, id="steps_exceed_keywords"),
            pytest.param(5, -1, id="negative_steps"),
        ],
    )
    def test_invalid_input_raises(self, keywords: int, steps: int) -> None:
        with pytest.raises(ValueError, match="steps must be between"):
            calculate(True, keywords, steps)
