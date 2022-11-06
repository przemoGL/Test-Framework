from pytest import mark


def test_string():
    assert isinstance('123', str)


def test_int():
    assert isinstance(123, int)


def test_float():
    assert isinstance(1.23, float)


def test_list():
    assert isinstance([1, 2, 3], list)


def test_dictionary():
    assert isinstance({1: 1, 2: 2, 3: 3}, dict)


def test_tuple():
    assert isinstance((1, 2, 3), tuple)


def test_set():
    assert isinstance({1, 2, 3}, set)


def test_range():
    assert isinstance(range(1, 3), range)


def test_boolean():
    assert isinstance(True, bool)


@mark.xfail
def test_xfail_string():
    assert isinstance(123, str)


@mark.xfail
def test_xfail_int():
    assert isinstance('123', int)


@mark.xfail
def test_xfail_float():
    assert isinstance(123, float)


@mark.xfail
def test_xfail_list():
    assert isinstance({1: 1, 2: 2, 3: 3}, list)


@mark.xfail
def test_xfail_dictionary():
    assert isinstance([1, 2, 3], dict)


@mark.xfail
def test_xfail_tuple():
    assert isinstance({1, 2, 3}, tuple)


@mark.xfail
def test_xfail_set():
    assert isinstance((1, 2, 3), set)


@mark.xfail
def test_xfail_range():
    assert isinstance(True, range)


@mark.xfail
def test_xfail_boolean():
    assert isinstance(range(1, 3), bool)
