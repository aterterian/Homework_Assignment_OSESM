from utils import *

tree_height = 5
diamond_size = 6
diamond_edge = "*"
diamond_inner = "o"


def test_subtract():
    assert subtract(10, 2) == 8
    assert subtract(10, 5) == 5
    assert subtract(27, 9) == 18


# Unfortunately I only realized that I can't really check functions without a return part when they were already built
# So I now check the input of the functions to be correct


def test_tree_height_type():
    assert not isinstance(tree_height, str), "Tree height should not be a string"


def test_diamond_size_type():
    assert not isinstance(diamond_size, str), "Diamond size should not be a string"


def test_diamond_edge_type():
    assert isinstance(diamond_edge, str), "Diamond edge should be a string"


def test_diamond_inner_type():
    assert isinstance(diamond_inner, str), "Diamond inner should be a string"
