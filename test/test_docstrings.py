import pytest

from docstrings import _add_docstring
import algorithm


@pytest.mark.docstring_test
def test_docstring_added():
    def function_without_docstring():
        return None

    function_with_docstring = _add_docstring(
        function_without_docstring, 'a docstring')

    assert function_with_docstring.__class__.__name__ == 'function'
    assert function_with_docstring.__doc__ == 'a docstring'


@pytest.mark.docstring_test
def test_calculate_weighted_value():
    assert algorithm.calculate_weighted_value.__doc__ is not None


@pytest.mark.docstring_test
def test_calculate_confidence_interval_has_docstring():
    assert algorithm.calculate_confidence_interval.__doc__ is not None


@pytest.mark.docstring_test
def test_convert_confidence_interval_into_probability_has_docstring():
    assert algorithm._convert_confidence_interval_into_probability.__doc__ is not None


@pytest.mark.docstring_test
def test_calculate_beta_distribution_mean_has_docstring():
    assert algorithm.calculate_beta_distribution_mean.__doc__ is not None


@pytest.mark.docstring_test
def test_place_mastery_in_band():
    assert algorithm._place_mastery_in_band.__doc__ is not None


@pytest.mark.docstring_test
def test_calculate_band_confidence_has_docstring():
    assert algorithm._calculate_band_confidence.__doc__ is not None


@pytest.mark.docstring_test
def test_calculate_confident_mastery_band_has_docstring():
    assert algorithm._calculate_confident_mastery_band.__doc__ is not None


@pytest.mark.docstring_test
def test_calculate_study_guide_weighting():
    assert algorithm.calculate_study_guide_weighting.__doc__ is not None


@pytest.mark.docstring_test
def test_calculate_confidence_intervals_list():
    assert algorithm.calculate_confidence_intervals_list.__doc__ is not None
