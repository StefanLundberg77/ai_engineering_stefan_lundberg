from constants import DATA_PATH
import pandas as pd
import json

df = pd.read_csv(DATA_PATH / "Iris.csv")

class Iris:
    def __init__(self, limit=100):
        self.df_full = df
        self.df = df.head(limit)

    #@property   
    def to_json(self):
            data = self.df.to_json(orient = "records")
            return json.loads(data)
        
    def filter_species(self, species: str):
            self.df = self.df_full.query(
                "Species.str.casefold() == @species.casefold()"
                )
            return self

    def kpis(self, country: str):
        """Filter out kpis based on species"""
        self.df = self._df_full.query(
            "Species.str.casefold() == @species.casefold()"
        )
        return {
            "Avg SepalLengthCm": str(self.df["SepalLengthCm"].avg()),
            # "total_cost": str(df_by_country["Cost"].sum()),
            # "number_of_purchases": str(len(df_by_country)),
        }#SepalLengthCm	SepalWidthCm	PetalLengthCm	PetalWidthCm