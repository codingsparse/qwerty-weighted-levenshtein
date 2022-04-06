from qwerty_weighted_levenshtein.qwerty_weighted_levenshtein import (
    qwerty_weighted_damerau_levenshtein,
    qwerty_weighted_levenshtein,
)


def test_basic_levenshtein_same_text_is_zero():
    text_1 = "test"
    text_2 = "test"
    distance = qwerty_weighted_levenshtein(text_1, text_2)

    assert distance == 0.0


def test_basic_levenshtein():
    text_1 = "test"
    text_2 = "rest"
    distance = qwerty_weighted_levenshtein(text_1, text_2)

    assert distance > 0.0


def test_basic_levenshtein_similarity():
    text_1 = "test"
    text_2 = "rest"
    distance = qwerty_weighted_levenshtein(text_1, text_2, similarity=True)

    assert distance > 0.0
    assert distance < 1.0


def test_basic_damerau_levenshtein_same_text_is_zero():
    text_1 = "test"
    text_2 = "test"
    distance = qwerty_weighted_damerau_levenshtein(text_1, text_2)

    assert distance == 0.0


def test_basic_damerau_levenshtein():
    text_1 = "test"
    text_2 = "rest"
    distance = qwerty_weighted_damerau_levenshtein(text_1, text_2)

    assert distance > 0.0


def test_basic_damerau_levenshtein_similarity():
    text_1 = "test"
    text_2 = "rest"
    distance = qwerty_weighted_damerau_levenshtein(text_1, text_2, similarity=True)

    assert distance > 0.0
    assert distance < 1.0
