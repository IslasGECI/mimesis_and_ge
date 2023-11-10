import mimesis_and_ge as dt


def test_add_offset():
    augend = 1
    addend = 2
    expected = augend + addend
    obtained = dt.add_offset(augend, addend)
    assert expected == obtained


def test_make_dataframe():
    obtained = dt.make_dataframe()
    obtained_n_cols = len(obtained.columns)
    expected_n_cols = 4
    assert obtained_n_cols == expected_n_cols
    obtained_n_rows = len(obtained)
    expected_n_rows = 7
    assert obtained_n_rows == expected_n_rows
    obtained_column_names = obtained.columns
    expected_column_names = ["Fecha", "Isla", "Especie", "Temporada"]
    assert (obtained_column_names == expected_column_names).all()
    obtained_islet = obtained["Isla"]
    all_posible_islet = ["Todos Santos", "Socorro", "Guadalupe", "Natividad"]
    assert obtained_islet.isin(all_posible_islet).all()
