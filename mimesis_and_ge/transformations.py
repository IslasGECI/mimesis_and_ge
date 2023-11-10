import pandas as pd
from mimesis import Fieldset
from mimesis.locales import Locale

from pathlib import Path
from mimesis import BaseDataProvider

fieldset = Fieldset(locale=Locale.EN)


class CustomDataProvider(BaseDataProvider):
    class Meta:
        name = "custom_provider"
        datafile = "file_name.json"
        datadir = Path(__file__).parent / "custom_datadir"

    def my_method(self, i):
        return self.random.choices(self.extract(["Isla"]), k=i)


cdp = CustomDataProvider(Locale.ES)


def add_offset(augend: int, addend: int) -> int:
    return augend + addend


fs = Fieldset(locale=Locale.ES, i=7)


def make_dataframe():
    return pd.DataFrame.from_dict(
        {
            "Fecha": fs("increment"),
            "Isla": cdp.my_method(7),
            "Especie": fs("email"),
            "Temporada": fs("telephone", mask="+1 (###) #5#-7#9#"),
        }
    )
