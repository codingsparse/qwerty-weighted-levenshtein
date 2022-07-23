from typing import Callable, Union
import numpy as np
from weighted_levenshtein import dam_lev, lev

# Source for NEIGHBORS_OF: A. Samuellson Master's Thesis
# https://kth.diva-portal.org/smash/get/diva2:1116701/FULLTEXT01.pdf
NEIGHBORS_OF = {}
NEIGHBORS_OF["q"] = ["w", "a"]
NEIGHBORS_OF["w"] = ["e", "s", "a", "q"]
NEIGHBORS_OF["e"] = ["r", "d", "s", "w"]
NEIGHBORS_OF["r"] = ["t", "f", "d", "e"]
NEIGHBORS_OF["t"] = ["y", "g", "f", "r"]
NEIGHBORS_OF["y"] = ["u", "h", "g", "t"]
NEIGHBORS_OF["u"] = ["i", "j", "h", "y"]
NEIGHBORS_OF["i"] = ["o", "k", "j", "u"]
NEIGHBORS_OF["o"] = ["p", "l", "k", "i"]
NEIGHBORS_OF["p"] = ["l", "o"]
NEIGHBORS_OF["a"] = ["q", "w", "s", "z"]
NEIGHBORS_OF["s"] = ["w", "e", "d", "x", "z", "a"]
NEIGHBORS_OF["d"] = ["e", "r", "f", "c", "x", "s"]
NEIGHBORS_OF["f"] = ["r", "t", "g", "v", "c", "d"]
NEIGHBORS_OF["g"] = ["t", "y", "h", "b", "v", "f"]
NEIGHBORS_OF["h"] = ["y", "u", "j", "n", "b", "g"]
NEIGHBORS_OF["j"] = ["u", "i", "k", "m", "n", "h"]
NEIGHBORS_OF["k"] = ["i", "o", "l", "m", "j"]
NEIGHBORS_OF["l"] = ["o", "p", "k"]
NEIGHBORS_OF["z"] = ["a", "s", "x"]
NEIGHBORS_OF["x"] = ["s", "d", "c", "z"]
NEIGHBORS_OF["c"] = ["d", "f", "v", "x"]
NEIGHBORS_OF["v"] = ["f", "g", "b", "c"]
NEIGHBORS_OF["b"] = ["g", "h", "n", "v"]
NEIGHBORS_OF["n"] = ["h", "j", "m", "b"]
NEIGHBORS_OF["m"] = ["j", "k", "n"]

QWERTY_COSTS = np.ones((128, 128), dtype=np.float64)

for ch in NEIGHBORS_OF:
    QWERTY_COSTS[ord(ch), ord(ch.upper())] = 0.6
    QWERTY_COSTS[ord(ch.upper()), ord(ch)] = 0.6
    for neighbor in NEIGHBORS_OF[ch]:
        QWERTY_COSTS[ord(ch), ord(neighbor)] = 0.7
        QWERTY_COSTS[ord(neighbor), ord(ch)] = 0.7

        QWERTY_COSTS[ord(ch.upper()), ord(neighbor.upper())] = 0.7
        QWERTY_COSTS[ord(neighbor.upper()), ord(ch.upper())] = 0.7


def _base_distance_similarity(
    distance_fn: Callable, text_1: str, text_2: str, similarity: bool
) -> Union[int, float]:
    if text_1 == text_2:
        return 1.0 if similarity else 0.0

    text_1 = text_1.encode("ascii", errors="ignore").decode()
    text_2 = text_2.encode("ascii", errors="ignore").decode()

    distance = distance_fn(text_1, text_2, substitute_costs=QWERTY_COSTS)
    if not similarity:
        return distance
    len1, len2 = len(text_1), len(text_2)

    max_distance = max(len1, len2)
    similarity = (max_distance - distance) / max_distance
    return similarity


def qwerty_weighted_levenshtein(
    text_1: str, text_2: str, similarity: bool = False
) -> Union[int, float]:
    return _base_distance_similarity(lev, text_1, text_2, similarity)


def qwerty_weighted_damerau_levenshtein(
    text_1: str, text_2: str, similarity: bool = False
) -> Union[int, float]:
    return _base_distance_similarity(dam_lev, text_1, text_2, similarity)
