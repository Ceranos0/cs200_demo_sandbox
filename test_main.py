import main
import pytest

@pytest.mark.parametrize(
('input_x','input_y','expected'),
(
    (0, 0, 1),
    (1, 0, 1),
    (0, 1, 1),
    (1, 1, 2),
)
)
def test_foo(input_x, input_y, expected):
    assert main.foo(input_x, input_y) == expected

def test_boo():
    assert main.boo(4, 2) == 7
    assert main.boo(0, 0) == 2

def test_bar():
    assert main.bar(24, 6) == 6
    assert main.bar(10, 2) == 7


