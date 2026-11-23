import pytest

from hackathon_26.scoring import calculate_score


class TestCalculateScore:
    @pytest.mark.parametrize(
        ("predicted_keywords", "actual_keywords", "expected_score"),
        [
            pytest.param(1, 1, 1000, id="perfect_score_minimum"),
            pytest.param(5, 5, 1000, id="exact_small"),
            pytest.param(100, 100, 1000, id="exact_large"),
            pytest.param(6, 5, 833, id="one_off_small"),
            pytest.param(30, 20, 667, id="two_thirds"),
            pytest.param(100, 10, 100, id="ten_percent"),
            pytest.param(300, 290, 967, id="many_keywords_close_prediction"),
            pytest.param(300, 10, 33, id="many_keywords_found_quickly"),
            pytest.param(300, 1, 3, id="worst_case_near_zero"),
        ],
    )
    def test_correct_score_given(self, predicted_keywords: int, actual_keywords: int, expected_score: int) -> None:
        assert calculate_score(predicted_keywords, actual_keywords) == expected_score

    @pytest.mark.parametrize(
        ("small", "large"),
        [
            pytest.param((10, 5), (200, 100), id="half"),
            pytest.param((15, 5), (300, 100), id="third"),
        ],
    )
    def test_same_ratio_gives_same_score(self, small: tuple[int, int], large: tuple[int, int]) -> None:
        assert calculate_score(*small) == calculate_score(*large)

    def test_closer_prediction_scores_higher(self) -> None:
        scores = [calculate_score(predicted, 10) for predicted in (10, 12, 20, 50, 100)]
        assert scores == sorted(scores, reverse=True)
        assert len(set(scores)) == len(scores)

    @pytest.mark.parametrize(
        ("predicted_keywords", "actual_keywords"),
        [
            pytest.param(300, 1, id="max_spread"),
            pytest.param(1, 1, id="minimum"),
            pytest.param(1000, 999, id="large_values"),
        ],
    )
    def test_score_stays_within_range(self, predicted_keywords: int, actual_keywords: int) -> None:
        assert 0 <= calculate_score(predicted_keywords, actual_keywords) <= 1000


class TestCalculateScoreInvalidInput:
    @pytest.mark.parametrize(
        ("predicted_keywords", "actual_keywords"),
        [
            pytest.param(5, 6, id="actual_exceeds_prediction"),
            pytest.param(1, 2, id="actual_exceeds_minimum_prediction"),
            pytest.param(5, 0, id="zero_actual"),
            pytest.param(5, -1, id="negative_actual"),
            pytest.param(0, 0, id="zero_prediction"),
        ],
    )
    def test_raises_value_error(self, predicted_keywords: int, actual_keywords: int) -> None:
        with pytest.raises(ValueError, match="actual keywords must be between 1 and the prediction"):
            calculate_score(predicted_keywords, actual_keywords)
