import pandas as pd
from mimesis import Fieldset
from mimesis.locales import Locale

fs = Fieldset(locale=Locale.EN, i=7)


def add_offset(augend: int, addend: int) -> int:
    return augend + addend


def make_dataframe():
    return pd.DataFrame.from_dict(
        {
            "ID": fs("increment"),
            "Name": fs("person.full_name"),
            "Email": fs("email"),
            "Phone": fs("telephone", mask="+1 (###) #5#-7#9#"),
        }
    )
