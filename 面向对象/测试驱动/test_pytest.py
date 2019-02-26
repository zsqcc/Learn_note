def add_x(x):
    return x + 2


def test_py_demo1():
    assert add_x(1) == 1


def test_py_demo2():
    assert add_x(1) == 2


test_py_demo1()
test_py_demo2()
