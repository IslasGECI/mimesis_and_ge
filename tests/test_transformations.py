import mimesis_and_ge as dt


def test_add_offset():
    augend = 1
    addend = 2
    expected = augend + addend
    obtained = dt.add_offset(augend, addend)
    assert expected == obtained


def test_make_dataframe():
    dt.make_dataframe()
